from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from ..aiinvestadvisor.tools.custom_tools import SearchTools, ReadTools


# model = ChatGroq(model="llama3-8b-8192")


@CrewBase
class AIInvestAdvisorCrew():

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def financial_results_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['financial_results_researcher'],
            tools=[SearchTools.web_search,
                   ReadTools.read_url, ReadTools.read_pdf],
            verbose=True,
            # llm=model,
        )

    @agent
    def financial_results_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['financial_results_analyst'],
            verbose=True,
            # llm=model
        )

    @ agent
    def email_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['email_writer'],
            verbose=True,
            # llm=model
        )

    @ task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
            agent=self.financial_results_researcher()
        )

    @ task
    def analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['analysis_task'],
            agent=self.financial_results_analyst(),
            context=[self.research_task()],
            output_file='output/final_advice_report.md',
        )

    # @task
    # def write_email_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['write_email_task'],
    #         agent=self.email_writer(),
    #         context=[self.analysis_task()],
    #         output_file='output/email_to_your_customer.txt'
    #     )

    @crew
    def crew(self) -> Crew:
        """Creates the Crewailab crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=2,
            # memory=True,
            cache=True,
            output_log_file='crew_execution.log'
        )
