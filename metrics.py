import time
import json
import yaml
import os
import pandas as pd
from crew import TravelingCrew
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy, context_precision

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = "your_api_key_here"


def load_expected_outputs():
    """Loads expected outputs from tasks.yaml."""
    with open("config/tasks.yaml", "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def evaluate_response(task_name, response, expected_output):
    """Evaluates the response based on expected output criteria."""
    if expected_output.lower() in str(response).lower():
        return "Correct"
    return "Incorrect"


def compute_ragas_metrics(response, expected_output):
    """Computes RAGAS metrics for the response."""
    try:
        df = pd.DataFrame([{
            "question": "Evaluate response",
            "answer": response,
            "contexts": [expected_output]  # Ensure it's a list
        }])

        scores = evaluate(
            dataset=df,
            metrics=[faithfulness, answer_relevancy, context_precision]
        )

        if scores.empty:
            return {"error": "RAGAS evaluation returned an empty DataFrame"}

        return {
            "faithfulness": scores.iloc[0].get("faithfulness", "N/A"),
            "answer_relevancy": scores.iloc[0].get("answer_relevancy", "N/A"),
            "context_precision": scores.iloc[0].get("context_precision", "N/A")
        }

    except Exception as e:
        return {"error": str(e)}




def collect_metrics(city="Gdansk"):
    """Collects metrics for the TravelingCrew agents."""
    metrics = {
        "model": "gpt-4o-mini",
        "execution_time": 0,
        "total_tokens_used": 0,
        "tasks": {}
    }

    crew_instance = TravelingCrew()
    crew = crew_instance.crew()
    expected_outputs = load_expected_outputs()

    start_time = time.time()

    inputs = {"city": city}

    crew_start = time.time()
    responses = crew.kickoff(inputs=inputs)
    crew_end = time.time()

    if isinstance(responses, list):
        for i, response in enumerate(responses):
            task_name = f"task_{i + 1}"
            task_time = round(crew_end - crew_start, 2)
            tokens_used = len(str(response)) // 4

            expected_output = expected_outputs.get(task_name, {}).get("expected_output", "")
            correctness = evaluate_response(task_name, response, expected_output)
            ragas_scores = compute_ragas_metrics(str(response), str(expected_output))

            metrics["tasks"][task_name] = {
                "response": response,
                "execution_time": task_time,
                "tokens_used": tokens_used,
                "correctness": correctness,
                "ragas_scores": ragas_scores
            }
            metrics["total_tokens_used"] += tokens_used
    else:
        summary_task_name = "summary"
        task_time = round(crew_end - crew_start, 2)
        tokens_used = len(str(responses)) // 4

        expected_output = expected_outputs.get(summary_task_name, {}).get("expected_output", "")
        correctness = evaluate_response(summary_task_name, responses, expected_output)
        ragas_scores = compute_ragas_metrics(responses, expected_output)

        metrics["tasks"][summary_task_name] = {
            "response": str(responses),
            "execution_time": task_time,
            "tokens_used": tokens_used,
            "correctness": correctness,
            "ragas_scores": ragas_scores
        }
        metrics["total_tokens_used"] += tokens_used

    metrics["execution_time"] = round(time.time() - start_time, 2)

    with open("metrics.json", "w") as f:
        json.dump(metrics, f, indent=4)

    return metrics


if __name__ == "__main__":
    results = collect_metrics()
    print(json.dumps(results, indent=4))