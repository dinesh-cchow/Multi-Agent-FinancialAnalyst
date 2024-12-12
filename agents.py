from crewai import Agent
from crewai_tools import ScrapeWebsiteTool, SerperDevTool

# Tools for agents
search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

# Data Analyst Agent
data_analyst_agent = Agent(
    role="Data Analyst",
    goal="Monitor and analyze market data in real-time to identify trends and predict market movements.",
    backstory="Specializing in financial markets, this agent uses statistical modeling and machine learning to provide insights.",
    allow_delegation=True,
    verbose=True,
    tools=[search_tool, scrape_tool]
)

# Trading Strategy Agent
trading_strategy_agent = Agent(
    role="Trading Strategy Developer",
    goal="Develop and test various trading strategies based on insights from the Data Analyst Agent.",
    backstory="This agent devises and refines trading strategies, evaluating profitability and risk.",
    allow_delegation=True,
    verbose=True,
    tools=[search_tool, scrape_tool]
)

# Execution Agent
execution_agent = Agent(
    role="Trade Advisor",
    goal="Suggest optimal trade execution strategies based on approved trading strategies.",
    backstory="Specializes in analyzing timing, price, and logistical details of potential trades.",
    allow_delegation=True,
    verbose=True,
    tools=[search_tool, scrape_tool]
)

# Risk Management Agent
risk_management_agent = Agent(
    role="Risk Advisor",
    goal="Evaluate and provide insights on risks associated with potential trading activities.",
    backstory="Scrutinizes potential risks of trades and offers mitigation strategies.",
    allow_delegation=True,
    verbose=True,
    tools=[search_tool, scrape_tool]
)
