from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
import os
from tools.WeatherTool import WeatherTool
from dotenv import load_dotenv

load_dotenv()

@CrewBase
class TravelingCrew():
    """Creating crew for traveling"""

    
    def __init__(self) -> None:
        self.openai_llm = LLM(
        api_key=os.getenv("OPENAI_KEY"),
        model="gpt-4o-mini",
        )
    
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def weather_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['weather_agent'],
            llm=self.openai_llm,
            tools=[WeatherTool()],
        )

    @task
    def weather_task(self) -> Task:
        return Task(
            config=self.tasks_config['weather_task'],
            agent=self.weather_agent(),
        )

    @agent
    def attractions_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['attractions_agent'],
            llm=self.openai_llm,
        )

    @task
    def attractions_task(self) -> Task:
        return Task(
            config=self.tasks_config['attractions_task'],
            agent=self.attractions_agent(),
        )

    @agent
    def accommodation_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['accommodation_agent'],
            llm = self.openai_llm
        )

    @task
    def accommodation_task(self) -> Task:
        return Task(
            config=self.tasks_config['accommodation_task'],
            agent=self.accommodation_agent()
        )

    @agent
    def transport_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['transport_agent'],
            llm = self.openai_llm
        )

    @task
    def transport_task(self) -> Task:
        return Task(
            config=self.tasks_config['transport_task'],
            agent=self.transport_agent()
        )

    @agent
    def summarizer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['summarizer_agent'],
            llm = self.openai_llm
        )

    @task
    def summarizer_task(self) -> Task:
        return Task(
            config=self.tasks_config['summarizer_task'],
            agent=self.summarizer_agent()
        )

    @agent
    def translator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['translator_agent'],
            llm = self.openai_llm
        )

    @task
    def translator_task(self) -> Task:
        return Task(
            config=self.tasks_config['translator_task'],
            agent=self.translator_agent()
        )

    @crew
    def crew(self) -> Crew:
        """Creates the traveling crew"""
        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            process = Process.sequential,
            verbose = True
        )
        
    