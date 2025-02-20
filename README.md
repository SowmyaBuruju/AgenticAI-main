# AgenticAI - Multi-Agent AI Financial Insights System

## Overview
AgenticAI is an advanced **multi-agent AI system** designed to provide **real-time financial insights** through multiple AI agents. The system retrieves **stock market trends, sentiment analysis, earnings reports, and AI-driven insights** from various sources like Yahoo Finance and DuckDuckGo.

---
## Features
✅ **Web Search Agent** - Fetches financial data from the web using DuckDuckGo.  
✅ **Financial Insights Agent** - Retrieves stock prices, analyst recommendations, and company financials.  
✅ **Sentiment Analysis Agent** - Analyzes sentiment of financial news and stock reports.  
✅ **Earnings Report Agent** - Summarizes earnings reports for companies.  
✅ **Crypto Market Agent** - Provides real-time cryptocurrency price updates.  
✅ **AI Market Trends Agent** - Identifies stock trends in AI-related companies.  

---
## Agents and Their Roles
### **1️⃣ Web Search Agent**
🔹 **Purpose**: Searches the web for the latest financial news and stock updates.  
🔹 **Functionality**: Uses DuckDuckGo to gather financial information.  
🔹 **Used In**: Fetching general stock market insights.

### **2️⃣ Financial Insights Agent**
🔹 **Purpose**: Fetches stock prices, analyst ratings, and financial summaries.  
🔹 **Functionality**: Uses Yahoo Finance tools for real-time data.  
🔹 **Used In**: Analyzing stock fundamentals and trends.

### **3️⃣ Sentiment Analysis Agent**
🔹 **Purpose**: Conducts sentiment analysis on AI and tech stock news.  
🔹 **Functionality**: Analyzes tweets, news headlines, and articles.  
🔹 **Used In**: Predicting market movements based on public sentiment.

### **4️⃣ Earnings Report Agent**
🔹 **Purpose**: Retrieves and summarizes company earnings reports.  
🔹 **Functionality**: Extracts key financial figures like revenue, net income, and EPS.  
🔹 **Used In**: Understanding financial performance of stocks.

### **5️⃣ Crypto Market Agent**
🔹 **Purpose**: Provides real-time cryptocurrency market insights.  
🔹 **Functionality**: Fetches crypto prices, trends, and sentiment.  
🔹 **Used In**: Crypto investment analysis and decision-making.

### **6️⃣ AI Market Trends Agent**
🔹 **Purpose**: Identifies AI-related stock trends.  
🔹 **Functionality**: Uses Nasdaq and NYSE data for AI company stocks.  
🔹 **Used In**: Tracking AI industry growth and stock performance.

---
## Installation Guide
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourgithub/AgenticAI.git
cd AgenticAI
```
### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```
### **3️⃣ Set Up Environment Variables**
Create a `.env` file in the project root and add:
```plaintext
GROQ_API_KEY=your_actual_api_key_here
```
### **4️⃣ Run AI Agents**
```bash
python financial_agent.py
```
### **5️⃣ Start the Web UI**
```bash
python playground.py
```
Or for API hosting:
```bash
uvicorn playground:app --reload
```

---
## **Expected Output**
When running `financial_agent.py`, the system processes AI stock trends, sentiment analysis, and earnings reports. Sample output:
```
AI Stock Trends:
  - Top Gainers: NVDA, MSFT, GOOGL
  - Top Losers: IBM, CSCO, INTC
  - Emerging Trends: AI cybersecurity, Cloud AI, Autonomous Vehicles

Sentiment Analysis:
  - Overall Sentiment: Neutral
  - Positive: 45%, Negative: 30%, Neutral: 25%
  - Key Topics: AI, Cloud Computing, Cybersecurity

Earnings Reports:
  - NVDA: EPS $1.34, Revenue $8.29B, Net Income $2.43B
  - GOOGL: EPS $1.53, Revenue $76.05B, Net Income $13.62B
```

---
## **Use Cases of Agents**
✔ **Stock Market Predictions** – Helps investors make informed decisions.  
✔ **Cryptocurrency Analysis** – Provides real-time updates for crypto traders.  
✔ **AI Industry Tracking** – Monitors emerging AI market trends.  
✔ **Sentiment-Based Investment** – Uses social sentiment to guide investment strategies.  
✔ **Financial Research** – Summarizes earnings reports for data-driven analysis.  

---
## **Contributing**
🔹 Fork the repository.  
🔹 Create a new branch (`git checkout -b feature/YourFeature`).  
🔹 Commit changes (`git commit -m 'Add feature'`).  
🔹 Push (`git push origin feature/YourFeature`).  
🔹 Open a pull request.  

---
## **Next Steps**
🚀 **Deploy as a web app** using FastAPI.  
📈 **Enhance AI agents** with machine learning models.  
💼 **Showcase on LinkedIn** to demonstrate your AI project.  

Let me know if you need help with GitHub deployment or writing a LinkedIn post! 🚀
