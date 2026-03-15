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
# def get_response(user_query , chat_history):
#     # =========================================
#     # LLM
#     llm = ChatTogether(
#         model="ServiceNow-AI/Apriel-1.6-15b-Thinker",
#         temperature=0.6,
#         api_key=os.getenv("api_key")
#     )
#     # =========================================

#     # Memory
#     # memory = ConversationBufferMemory(
#     # memory_key="chat_history",
#     # return_messages=True # to return conversation list of AI Message and Human Meassage 
#     # )
#     # Prompt
#     template = """
#     You are a helpful AI assistant Answer the following questions considering in the history of the conversation:
#     Chat history{chat_history}      
#     User Question: {user_question}
#     """
#     prompt = ChatPromptTemplate.from_template(template) 
#     # ===============================================
#     # Build Custom Chain 
#     chain = prompt | llm | StrOutputParser()

#     return chain.stream({"chat_history":chat_history , "user_question" : user_query})
def get_response(user_query, chat_history):
    from langchain_together import ChatTogether
    from langchain.prompts import ChatPromptTemplate
    from langchain_core.output_parsers import StrOutputParser

    # تأكد من مفتاح API موجود
    api_key = os.getenv("api_key")
    if not api_key:
        raise ValueError("API Key not found. Please set it in .env as api_key=YOUR_KEY")

    # LLM
    llm = ChatTogether(
        model_name="gpt-3.5-turbo",  # استخدم نموذج معروف لتجربة
        temperature=0.6,
        api_key=api_key
    )

    # Prompt
    template = """
    You are a helpful AI assistant. Answer the following question considering the history of the conversation:
    Chat history: {chat_history}      
    User Question: {user_question}
    """
    prompt = ChatPromptTemplate.from_template(template)

    # Build Chain
    chain = prompt | llm | StrOutputParser()

    return chain.stream({"chat_history": chat_history, "user_question": user_query})
