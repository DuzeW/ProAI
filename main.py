from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from crew import TravelingCrew

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def home():
    return render_template('survey.html')

@app.route('/submit_survey', methods=['POST'])
def submit_survey():
    data = request.json
    inputs = {
        "city": data.get("city"),
        "answer_language": data.get("answer_language"),
        "budget": data.get("budget"),
        "preferred_transportation": data.get("preferred_transportation"),
        "point_of_interest": data.get("point_of_interest"),
        "preferred_accommodation": data.get("preferred_accommodation"),
    }
    response = TravelingCrew().crew().kickoff(inputs=inputs)
    
 
    print("Response object:", response)
    print("Response dict:", response.__dict__)
    
    # Konwersja CrewOutput na słownik na podstawie dostępnych atrybutów
    response_dict = {
        "weather": response.raw.split('\n\n')[0],
        "attractions": response.raw.split('\n\n')[1],
        "accommodation": response.raw.split('\n\n')[2],
        "transport": response.raw.split('\n\n')[3]
    }
    
    return jsonify(response_dict)

if __name__ == '__main__':
    app.run(debug=True)
