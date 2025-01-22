from crewai import Agent
from dotenv import load_dotenv
from tools import tool
import os
from langchain.chat_models import ChatOpenAI

load_dotenv()

# Initialize the Chat model with OpenAI API key
llm = ChatOpenAI(
    model="gpt-4o",
    verbose=True,
    temperature=0.5,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# Financial Advisor Agent
pricing_strategist = Agent(
    role="Financial Advisor",
    goal="Suggest stocks or portfolios for users to maximize earnings. Please make sure that all research should be for latest date. Current date is November 2024.",
    verbose=True,
    memory=True,
    backstory="Experienced financial advisor aiding users in wealth growth.",
    llm=llm,
    tools=[tool],
    allow_delegation=True,
)

# Market Researcher Agent
market_researcher = Agent(
    role="Market Researcher",
    goal="Conduct stock research and predictions for North America.",
    verbose=True,
    memory=True,
    backstory="Expert in analyzing market data, focused on finance.",
    llm=llm,
    tools=[tool],
    allow_delegation=False,
)
