# Main Logic of our Chatbot
# ================================
# Library 
import os
# Lang Chain
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory  
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain_core.messages import AIMessage , HumanMessage
from langchain_core.output_parsers import StrOutputParser
# Chat Toghther
from langchain_together import ChatTogether
######### API Key ############
from dotenv import load_dotenv
load_dotenv()
# =========================================
# =========================================
#### Build Chatbot Model Use LangChain
# =========================================
# =========================================
def get_response(user_query , chat_history):
    # =========================================
    # LLM
    llm = ChatTogether(
        model="ServiceNow-AI/Apriel-1.6-15b-Thinker",
        temperature=0.6,
        api_key=os.getenv("api_key")
    )
    # =========================================

    # Memory
    # memory = ConversationBufferMemory(
    # memory_key="chat_history",
    # return_messages=True # to return conversation list of AI Message and Human Meassage 
    # )
    # Prompt
    template = """
    You are a helpful AI assistant Answer the following questions considering in the history of the conversation:
    Chat history{chat_history}      
    User Question: {user_question}
    """
    prompt = ChatPromptTemplate.from_template(template) 
    # ===============================================
    # Build Custom Chain 
    chain = prompt | llm | StrOutputParser()

    return chain.stream({"chat_history":chat_history , "user_question" : user_query})
