from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

## Web Search Agent
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for the latest market and financial insights",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGoTools()],
    instructions=["Always include sources and verify data integrity"],
    show_tool_calls=True,
    markdown=True
)

## Financial Insights Agent
finance_agent = Agent(
    name="Finance AI Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[
        YFinanceTools(stock_price=True, 
                      analyst_recommendations=True, 
                      stock_fundamentals=True, 
                      company_news=True)
    ],
    instructions=["Use structured tables to present financial data clearly"],
    show_tool_calls=True,
    markdown=True
)

## Sentiment Analysis Agent
sentiment_agent = Agent(
    name="Sentiment Analysis Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=["Analyze sentiment of financial news and stock reports"],
    show_tool_calls=True,
    markdown=True
)

## Earnings Report Analyzer
earnings_agent = Agent(
    name="Earnings Report Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=["Fetch and summarize the latest earnings reports for stocks"],
    show_tool_calls=True,
    markdown=True
)

## Cryptocurrency Market Agent
crypto_agent = Agent(
    name="Crypto Market Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=["Provide real-time cryptocurrency prices and trends"],
    show_tool_calls=True,
    markdown=True
)

## AI Market Trends Agent
ai_trends_agent = Agent(
    name="AI Market Trends Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=["Identify market trends in AI-related stocks and technologies"],
    show_tool_calls=True,
    markdown=True
)

# Multi-Agent System
multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent, sentiment_agent, earnings_agent, crypto_agent, ai_trends_agent],
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=["Provide structured, well-researched financial insights"],
    show_tool_calls=True,
    markdown=True
)

# Run Sample Query
if __name__ == "__main__":
    try:
        multi_ai_agent.print_response("Provide the latest AI stock trends, sentiment analysis, and earnings reports.", stream=True)
    except Exception as e:
        print(f"An error occurred: {e}")
