# AI Assistant Chatbot 🤖

A Streamlit-based AI chatbot powered by **LangChain** and **ChatTogether**, designed to maintain multi-turn conversations with memory and provide contextual responses.

---

## 📝 Features

- Multi-turn chat with conversation memory.
- Multiple chat sessions with sidebar management.
- Clear and intuitive Streamlit UI.
- Powered by advanced LLMs via `ChatTogether`.
- Easy to extend with new LLM models and prompts.

---

## Technologies Used

- **Python 3.11**
- **Streamlit** – for the web interface
- **LangChain** – LLM integration and conversation memory
- **ChatTogether** – connecting to large language models
- **dotenv** – manage API keys
- **LangChain Core** – AIMessage and HumanMessage handling

---

## 📂 Project Structure
```
ذذ
ai-chatbot/
│
├── chatbot/
│ ├── chatbot_function.py # Main logic to generate responses
│ └── init.py
│
├── pages/ # Optional: Streamlit multi-page support
│
├── app.py # Main Streamlit app
├── .env # API key storage (example: api_key=YOUR_KEY)
├── requirements.txt # Project dependencies
└── README.md
```
ذذ
ذذذ
