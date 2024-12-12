import os
from dotenv import load_dotenv
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")"

from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from agents import (
    data_analyst_agent,
    trading_strategy_agent,
    execution_agent,
    risk_management_agent
)
from tasks import (
    data_analysis_task,
    strategy_development_task,
    execution_planning_task,
    risk_assessment_task
)

# Define the Crew
financial_trading_crew = Crew(
    agents=[
        data_analyst_agent,
        trading_strategy_agent,
        execution_agent,
        risk_management_agent,
    ],
    tasks=[
        data_analysis_task,
        strategy_development_task,
        execution_planning_task,
        risk_assessment_task,
    ],
    verbose=True,
    process=Process.hierarchical,
    manager_llm=ChatOpenAI(model="gpt-4-turbo", temperature=0.7)
)
