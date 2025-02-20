from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv
from agno.playground import Playground, serve_playground_app
import os
import agno.api

# Load API keys
load_dotenv()
agno.api = os.getenv("AGNO_API_KEY")

# Import AI Agents
from financial_agent import (
    web_search_agent, finance_agent, sentiment_agent,
    earnings_agent, crypto_agent, ai_trends_agent
)

# Web Playground App
app = Playground(agents=[
    finance_agent, web_search_agent, sentiment_agent,
    earnings_agent, crypto_agent, ai_trends_agent
]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)
