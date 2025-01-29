from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
import os
from tools.TransportTool import TransportTool
from tools.WeatherTool import WeatherTool
from tools.HotelTool import HotelTool
from tools.AttractionTool import AttractionTool
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
    def accommodation_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['accommodation_agent'],
            llm=self.openai_llm,
            tools=[HotelTool()]
        )

    @task
    def accommodation_task(self) -> Task:
        return Task(
            config=self.tasks_config['accommodation_task'],
            agent=self.accommodation_agent()
        )

    @agent
    def attractions_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['attractions_agent'],
            llm=self.openai_llm,
            tools=[AttractionTool()]
        )

    @task
    def attractions_task(self) -> Task:
        return Task(
            config=self.tasks_config['attractions_task'],
            agent=self.attractions_agent(),
        )

    @agent
    def transport_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['transport_agent'],
            llm=self.openai_llm,
            tools=[TransportTool()]
        )

    @task
    def transport_task(self) -> Task:
        return Task(
            config=self.tasks_config['transport_task'],
            agent=self.transport_agent(),
        )

    @agent
    def summarize_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['summarize_agent'],
            llm=self.openai_llm
        )

    @task
    def summarize_task(self) -> Task:
        return Task(
            config=self.tasks_config['summarize_task'],
            agent=self.summarize_agent(),
            context=[ #kontekst
                self.weather_task(),
                self.accommodation_task(),
                self.attractions_task(),
                self.transport_task(),
            ]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the traveling crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
