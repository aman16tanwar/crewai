from dotenv import load_dotenv
import os
from crewai_tools import SerperDevTool

load_dotenv()

# Set the Serper API key environment variable
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")

# Initialize the Serper development tool for financial data
tool = SerperDevTool()
