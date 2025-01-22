from crewai import Crew, Process
from agents import pricing_strategist, market_researcher
from tasks import market_research_task, investment_strategy_task

# Configure the crew for financial advisory and investment research
crew = Crew(
    agents=[pricing_strategist, market_researcher],
    tasks=[market_research_task, investment_strategy_task],
    process=Process.sequential,
)

# Start task execution
result = crew.kickoff(inputs={})
print(result)
