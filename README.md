# Crew AI - Financial Advisory and Investment Research

This project leverages Crew AI to build a system for financial advisory and investment research. It uses agents specialized in market research and investment strategy to provide data-driven recommendations.

## Overview

This Crew AI setup utilizes two agents:

* **Market Researcher:** Conducts research on profitable stocks and investment opportunities in the USA and Canada markets. Analyzes sectors, recent trends, and top-performing stocks.
* **Financial Advisor (Pricing Strategist):** Provides strategic recommendations for a diversified investment portfolio based on the market research. Suggests asset allocations and risk levels to optimize returns for clients.

The agents interact with each other sequentially: the Market Researcher first gathers data, and then the Financial Advisor uses this data to create an investment strategy.  This process aims to provide a comprehensive and informed approach to investment planning.

## Key Features

* **Automated Research:** Automates the process of market research and investment strategy development.
* **Data-Driven Insights:** Leverages real-time financial data for accurate and up-to-date recommendations.
* **Sequential Workflow:** Ensures a structured and logical flow of information from research to strategy.
* **Customizable Agents:** Agents are configured with specific roles, goals, and backstories to enhance their performance.

## Setup and Usage

1. **Environment Variables:** Set the required environment variables in a `.env` file:
    * `OPENAI_API_KEY`: Your OpenAI API key.
    * `SERPER_API_KEY`: Your Serper API key.

2. **Installation:** Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. **Execution:** Run the main script:
    ```bash
    python crew.py
    ```

## Output

The final investment strategy recommendations are saved in `investment-strategy-report.md`.

## Future Enhancements

* **Dynamic Task Generation:** Allow for more flexible task creation based on user input.
* **User Interface:** Develop a user interface for easier interaction with the system.
* **Expanded Market Coverage:** Extend research capabilities to other global markets.
* **Backtesting:** Implement backtesting capabilities to evaluate the performance of suggested strategies.


## Architecture

The project follows a sequential agent-based architecture.  The `crew.py` file orchestrates the interaction between the `Market Researcher` and `Financial Advisor` agents. Each agent is defined in `agents.py` with their respective roles, goals, and tools. The tasks they perform are defined in `tasks.py`. The `tools.py` file defines the Serper search tool used for accessing real-time financial data.  The vertex-ai directory holds the flask application and streamlit application that interact with the VertexAI Model.



## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.
