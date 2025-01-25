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
    def hotel_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['hotel_researcher'],
            llm = self.openai_llm
        )

    @task
    def hotel_researcher_task(self) -> Task:
        return Task(
            config=self.tasks_config['hotel_researcher_task'],
            agent=self.hotel_researcher()
        )

    @agent
    def transport_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['transport_agent'],
            llm = self.openai_llm
        )

    @task
    def transport_agent_task(self) -> Task:
        return Task(
            config=self.tasks_config['transport_agent_task'],
            agent=self.transport_agent()
        )

    @agent
    def sumerizer(self) -> Agent:
        return Agent(
            config=self.agents_config['sumerizer'],
            llm = self.openai_llm
        )

    @task
    def sumerizer_task(self) -> Task:
        return Task(
            config=self.tasks_config['sumerizer_task'],
            agent=self.sumerizer()
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
        
    