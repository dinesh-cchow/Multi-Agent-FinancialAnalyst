import streamlit as st
import pandas as pd
from PyPDF2 import PdfReader
import os

from crew_manager import financial_trading_crew


# Function to handle file uploads and extract data
def process_uploaded_file(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        # Extract text from PDF
        pdf_reader = PdfReader(uploaded_file)
        text_data = ""
        for page in pdf_reader.pages:
            text_data += page.extract_text()
        return {"type": "text", "content": text_data}

    elif uploaded_file.name.endswith(".txt"):
        # Read text from TXT
        text_data = uploaded_file.read().decode("utf-8")
        return {"type": "text", "content": text_data}

    elif uploaded_file.name.endswith(".xlsx"):
        # Read Excel file
        excel_data = pd.ExcelFile(uploaded_file)
        return {"type": "excel", "content": excel_data}

    else:
        st.error("Unsupported file format! Please upload a PDF, TXT, or XLSX file.")
        return None


# Streamlit App Title
st.title("Multi-Agent Financial Analysis System")

# Sidebar for Inputs
st.sidebar.header("User Input Parameters")
stock_selection = st.sidebar.text_input("Stock Selection", "AAPL")
initial_capital = st.sidebar.number_input("Initial Capital ($)", min_value=1000, step=1000, value=100000)
risk_tolerance = st.sidebar.selectbox("Risk Tolerance", ["Low", "Medium", "High"], index=1)
trading_strategy_preference = st.sidebar.selectbox("Trading Strategy Preference", ["Day Trading", "Swing Trading", "Long-Term"])
news_impact_consideration = st.sidebar.checkbox("Consider News Impact", value=True)

# File Upload Section
uploaded_file = st.sidebar.file_uploader("Upload Market Data or Relevant Documents (PDF, TXT, XLSX)", type=["pdf", "txt", "xlsx"])

if uploaded_file:
    processed_file = process_uploaded_file(uploaded_file)

    if processed_file:
        if processed_file["type"] == "text":
            st.write("### Uploaded Document Content (Text)")
            st.text(processed_file["content"])
        elif processed_file["type"] == "excel":
            st.write("### Uploaded Excel File Content")
            st.write(processed_file["content"].sheet_names)  # Display sheet names
            selected_sheet = st.selectbox("Select a sheet to view", processed_file["content"].sheet_names)
            st.dataframe(processed_file["content"].parse(selected_sheet))  # Display selected sheet

# Run Financial Analysis
if st.sidebar.button("Run Financial Analysis"):
    st.write("### Running Multi-Agent Financial Analysis...")

    # Prepare input for CrewAI system
    financial_trading_inputs = {
        "stock_selection": stock_selection,
        "initial_capital": initial_capital,
        "risk_tolerance": risk_tolerance,
        "trading_strategy_preference": trading_strategy_preference,
        "news_impact_consideration": news_impact_consideration,
    }

    # Run CrewAI system
    with st.spinner("Executing tasks with agents..."):
        result = financial_trading_crew.kickoff(inputs=financial_trading_inputs)

    # Display Results
    st.write("## Analysis Results")
    st.markdown(result)
