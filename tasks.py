from crewai import Task
from tools import tool
from agents import pricing_strategist, market_researcher

# Task: Market research for investment opportunities
market_research_task = Task(
    description=(
        "Conduct research on profitable stocks and investment opportunities, focusing on USA and Canada markets. "
        "Analyze sectors, recent trends, and top-performing stocks to identify potential investments."
    ),
    expected_output='Detailed report on recommended stocks and sectors in USA and Canada.',
    tools=[tool],
    agent=market_researcher,
)

# Task: Investment strategy recommendations
investment_strategy_task = Task(
    description=(
        "Based on market research, provide strategic recommendations for a diversified investment portfolio. "
        "Suggest asset allocations and risk levels to optimize returns for clients."
    ),
    expected_output='Comprehensive investment strategy with portfolio recommendations for optimal growth.',
    tools=[tool],
    agent=pricing_strategist,
    async_execution=False,
    output_file='investment-strategy-report.md'
)
