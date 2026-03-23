🌌 SmartSaver Pro: Autonomous AI Procurement Agent
SmartSaver Pro is a high-performance Autonomous AI Agent designed to automate the decision-making process in e-commerce. It doesn't just track prices; it "thinks" like a procurement expert to secure the best deals.

🚀 Key Capabilities (Technical Skills)
Web Intelligence: Automated real-time scraping of product metadata and stock availability.

LLM Decision Logic: Implementation of Llama 3.3 (via Groq) to analyze price-to-target ratios.

Automated SMTP Execution: Instant notification system using Python's smtplib for real-time alerts.
Full-Stack UI/UX: A custom-styled, dark-themed dashboard built with Streamlit and Injected CSS.

🧠 Project Workflow
The system operates in a streamlined execution cycle:

Ingestion: User defines the product and a strategic "Target Budget."

Live Extraction: The agent pulls current market data from the source.

AI Reasoning: The Llama 3.3 70B model evaluates if current conditions meet the "BUY" criteria.

Instant Notification: If the verdict is BUY, the agent triggers a secure email alert.
Gemini said
Mubarak Khan, galti ho gayi! Maine .env aur README mein wo sensitive details miss kar di thin. Ab maine sab kuch cover kar diya hai.

Ye rahi aapki Updated English README. Is mein maine "App Password" ka zikr bhi kiya hai aur aapki skills (Python, AI, Ubuntu, Automation) ko bohot smartly highlight kiya hai taake parhne wala impress ho jaye.

🌌 SmartSaver Pro: Autonomous AI Procurement Agent
SmartSaver Pro is a high-performance Autonomous AI Agent designed to automate the decision-making process in e-commerce. It doesn't just track prices; it "thinks" like a procurement expert to secure the best deals.

🚀 Key Capabilities (Technical Skills)
Web Intelligence: Automated real-time scraping of product metadata and stock availability.

LLM Decision Logic: Implementation of Llama 3.3 (via Groq) to analyze price-to-target ratios.

Automated SMTP Execution: Instant notification system using Python's smtplib for real-time alerts.

Full-Stack UI/UX: A custom-styled, dark-themed dashboard built with Streamlit and Injected CSS.

🧠 Project Workflow
The system operates in a streamlined execution cycle:

Ingestion: User defines the product and a strategic "Target Budget."

Live Extraction: The agent pulls current market data from the source.

AI Reasoning: The Llama 3.3 70B model evaluates if current conditions meet the "BUY" criteria.

Instant Notification: If the verdict is BUY, the agent triggers a secure email alert.

🛠️ Setup & Environment Configuration
1. Generate App Password
Since this project uses Gmail for alerts, you must use a Google App Password (Standard passwords won't work due to 2FA):

Go to your Google Account -> Security -> 2-Step Verification.

Scroll to "App passwords" at the bottom.

Generate a password for "Mail" on your "Linux" device.

2. Configure .env File
Create a .env file in the root directory and add your credentials:

# AI Model Configuration
GROQ_API_KEY=your_groq_api_key_here
MODEL_NAME=llama-3.3-70b-versatile

# SMTP/Email Configuration
EMAIL_USER=your_gmail@gmail.com
EMAIL_PASS=your_16_digit_app_password  # The code uses this for secure login
ALERT_RECEIVER=receiver_email@gmail.com
Gemini said
Mubarak Khan, galti ho gayi! Maine .env aur README mein wo sensitive details miss kar di thin. Ab maine sab kuch cover kar diya hai.

Ye rahi aapki Updated English README. Is mein maine "App Password" ka zikr bhi kiya hai aur aapki skills (Python, AI, Ubuntu, Automation) ko bohot smartly highlight kiya hai taake parhne wala impress ho jaye.

🌌 SmartSaver Pro: Autonomous AI Procurement Agent
SmartSaver Pro is a high-performance Autonomous AI Agent designed to automate the decision-making process in e-commerce. It doesn't just track prices; it "thinks" like a procurement expert to secure the best deals.

🚀 Key Capabilities (Technical Skills)
Web Intelligence: Automated real-time scraping of product metadata and stock availability.

LLM Decision Logic: Implementation of Llama 3.3 (via Groq) to analyze price-to-target ratios.

Automated SMTP Execution: Instant notification system using Python's smtplib for real-time alerts.

Full-Stack UI/UX: A custom-styled, dark-themed dashboard built with Streamlit and Injected CSS.

🧠 Project Workflow
The system operates in a streamlined execution cycle:

Ingestion: User defines the product and a strategic "Target Budget."

Live Extraction: The agent pulls current market data from the source.

AI Reasoning: The Llama 3.3 70B model evaluates if current conditions meet the "BUY" criteria.

Instant Notification: If the verdict is BUY, the agent triggers a secure email alert.

🛠️ Setup & Environment Configuration
1. Generate App Password
Since this project uses Gmail for alerts, you must use a Google App Password (Standard passwords won't work due to 2FA):

Go to your Google Account -> Security -> 2-Step Verification.

Scroll to "App passwords" at the bottom.

Generate a password for "Mail" on your "Linux" device.

2. Configure .env File
Create a .env file in the root directory and add your credentials:

Code snippet
# AI Model Configuration
GROQ_API_KEY=your_groq_api_key_here
MODEL_NAME=llama-3.3-70b-versatile

# SMTP/Email Configuration
EMAIL_USER=your_gmail@gmail.com
EMAIL_PASS=your_16_digit_app_password  # The code uses this for secure login
ALERT_RECEIVER=receiver_email@gmail.com
3. Execution
Bash
# Install dependencies
pip install -r requirements.txt

# Launch the Agent on Ubuntu
streamlit run app.py

🚀 Summary & Future Roadmap

This project demonstrates the integration of LLM reasoning with Web Automation to solve real-world procurement challenges. By combining Llama 3.3 for decision-making and Python for execution, SmartSaver Pro acts as a reliable autonomous assistant for budget-conscious consumers.

Planned Update: Integrating Facebook Prophet for predictive price forecasting based on historical data.

Architecture: Scalable Multi-Agent design for cross-platform vendor comparison.

Project Metadata
Developer: Mubara Khaqan

Specialization: AI Engineering (Self-Learner)

Environment: Ubuntu Linux | Python 3.9+

Core Tech: LangChain | Groq | Streamlit