# Multi-Agent Financial Analyst

A comprehensive multi-agent financial analysis system built using Python, CrewAI framework, and Streamlit for interactive user interfaces. This project uses multiple agents to analyze market data, develop trading strategies, execute trades, and manage risks.

---

## **Features**
- **Data Analysis Agent**: Monitors and analyzes real-time market data to identify trends and predict movements.
- **Trading Strategy Agent**: Develops optimized trading strategies using statistical modeling, machine learning, and technical analysis.
- **Execution Agent**: Provides execution plans for optimal trading strategies based on market conditions.
- **Risk Management Agent**: Evaluates risks associated with trading strategies and suggests mitigation techniques.

---

## **Technologies Used**
- **Python**: Core programming language.
- **CrewAI Framework**: For implementing multi-agent collaboration.
- **Streamlit**: For creating an interactive web interface.
- **Environment Variables**: For securely storing sensitive API keys and credentials.

---

## **Setup Instructions**

### **Clone the Repository**
To clone this repository to your local machine:
```bash
git clone https://github.com/dinesh-cchow/Multi-Agent-FinancialAnalyst.git
cd Multi-Agent-FinancialAnalyst
Install Dependencies
Install all required libraries and dependencies listed in the requirements.txt file:
pip install -r requirements.txt
##Environment Setup
Create a .env file in the root directory and add your API keys:
OPENAI_API_KEY=<your-openai-api-key>
SERPER_API_KEY=<your-serper-api-key>
Run the Application
Launch the Streamlit application:
streamlit run app.py
