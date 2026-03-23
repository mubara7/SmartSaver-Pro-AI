SmartSaver Pro
**SmartSaver Pro** is a high-performance Autonomous AI Agent designed to automate complex decision-making in e-commerce. It doesn't just track prices; it **"thinks"** like a procurement expert to secure the best deals in real-time.

> **🚀 Live Demo:** (https://smartsaver-pro-ai-8loy9ngp7xmsf43sj3lanm.streamlit.app/)

---

## 🧠 The "Brain" Behind the Agent
Traditional price trackers only notify you of changes. **SmartSaver Pro** uses the **Llama 3.3 70B model (via Groq)** to perform a multi-factor analysis:
1. **Price-to-Target Evaluation:** Does the current price meet the user's strategic budget?
2. **Stock Intelligence:** Is the item available for immediate procurement?
3. **Strategic Verdict:** Should the user buy now or wait for a better market entry?

---

## 🚀 Key Technical Capabilities
* **Web Intelligence:** Real-time extraction of product metadata and stock status using optimized scraping logic.
* **LLM Decision Logic:** Implementation of advanced reasoning chains to evaluate market conditions.
* **Automated SMTP Execution:** Instant notification system using Python’s `smtplib` for secure, real-time email alerts.
* **High-End UI/UX:** A custom-styled, dark-themed "Intelligence Dashboard" built with **Streamlit** and injected CSS.

---

## 🛠️ System Architecture & Workflow


1.  **Ingestion:** User defines a product and a strategic "Target Budget."
2.  **Extraction:** The agent pulls live market data from the source URL.
3.  **Reasoning:** The Llama 3.3 model evaluates if conditions meet the "BUY" criteria.
4.  **Execution:** If verified, the agent triggers a secure email alert automatically.

---

## ⚙️ Setup & Configuration

### 1. Configure Environment Variables
Create a `.env` file in the root directory:
```env
# AI Model Configuration
GROQ_API_KEY=your_groq_api_key_here
MODEL_NAME=llama-3.3-70b-versatile

# SMTP/Email Configuration
EMAIL_USER=your_gmail@gmail.com
EMAIL_PASS=your_16_digit_app_password  # Google App Password
ALERT_RECEIVER=receiver_email@gmail.com

2. Installation (Linux/Ubuntu)
Bash

# Clone the repository
git clone [https://github.com/mubara7/SmartSaver-Pro-AI.git](https://github.com/mubara7/SmartSaver-Pro-AI.git)

# Install dependencies
pip install -r requirements.txt

# Launch the Dashboard
streamlit run app.py

Future Roadmap
Price Forecasting: Integrating Facebook Prophet for historical trend analysis and predictive budgeting.

Multi-Agent Scaling: Expanding into a multi-agent system for cross-platform vendor comparison.

👨‍💻 Project Metadata
Developer: Mubara Khaqan 

Specialization: AI Engineering (Self-Learner)

Environment: Ubuntu Linux | Python 3.9+

Core Tech: LangChain | Groq | Streamlit | Llama 3.3