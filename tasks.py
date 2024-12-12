from crewai import Task
from agents import (
    data_analyst_agent,
    trading_strategy_agent,
    execution_agent,
    risk_management_agent
)

# Task for Data Analyst Agent
data_analysis_task = Task(
    description=(
        "Continuously monitor and analyze market data for the selected stock ({stock_selection}). "
        "Use statistical modeling and machine learning to identify trends and predict market movements."
    ),
    expected_output=(
        "Insights and alerts about significant market opportunities or threats for {stock_selection}."
    ),
    agent=data_analyst_agent,
)

# Task for Trading Strategy Agent
strategy_development_task = Task(
    description=(
        "Develop and refine trading strategies based on insights from the Data Analyst Agent and "
        "user-defined risk tolerance ({risk_tolerance}). Consider trading preferences ({trading_strategy_preference})."
    ),
    expected_output=(
        "A set of potential trading strategies for {stock_selection} that align with the user's risk tolerance."
    ),
    agent=trading_strategy_agent,
)

# Task for Execution Agent
execution_planning_task = Task(
    description=(
        "Analyze approved trading strategies to determine the best execution methods for {stock_selection}, "
        "considering current market conditions and optimal pricing."
    ),
    expected_output=(
        "Detailed execution plans suggesting how and when to execute trades for {stock_selection}."
    ),
    agent=execution_agent,
)

# Task for Risk Management Agent
risk_assessment_task = Task(
    description=(
        "Evaluate the risks associated with the proposed trading strategies and execution plans for {stock_selection}. "
        "Provide a detailed analysis of potential risks and suggest mitigation strategies."
    ),
    expected_output=(
        "A comprehensive risk analysis report detailing potential risks and mitigation recommendations for {stock_selection}."
    ),
    agent=risk_management_agent,
)
