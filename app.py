import streamlit as st
from chatbot.chatbot_function import get_response
from langchain_core.messages import AIMessage, HumanMessage

# ---------------------------------
# Page Config
# ---------------------------------

st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------------
# Move title up (reduce top padding)
# ---------------------------------

st.markdown("""
<style>
.block-container {
    padding-top: 1.5rem;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------
# Session State
# ---------------------------------

if "chats" not in st.session_state:
    st.session_state.chats = {"Chat 1": []}

if "current_chat" not in st.session_state:
    st.session_state.current_chat = "Chat 1"

# ---------------------------------
# Sidebar
# ---------------------------------

with st.sidebar:

    st.markdown("## 🤖 AI Chats")

    st.divider()

    st.markdown("### 💬 Chats")

    for chat in st.session_state.chats.keys():

        if st.button(chat, use_container_width=True):
            st.session_state.current_chat = chat
            st.rerun()

    st.divider()

    if st.button("➕ New Chat", use_container_width=True):
        new_chat = f"Chat {len(st.session_state.chats) + 1}"
        st.session_state.chats[new_chat] = []
        st.session_state.current_chat = new_chat
        st.rerun()

    if st.button("🗑 Clear Current Chat", use_container_width=True):
        st.session_state.chats[st.session_state.current_chat] = []
        st.rerun()

# ---------------------------------
# Main Chat UI
# ---------------------------------

st.markdown("## 💬 AI Chatbot")

chat_history = st.session_state.chats[st.session_state.current_chat]

for message in chat_history:

    if isinstance(message, HumanMessage):
        with st.chat_message("user", avatar="🧑"):
            st.markdown(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(message.content)

# ---------------------------------
# Chat Input
# ---------------------------------

user_input = st.chat_input("Type your message...")

if user_input:

    chat_history.append(HumanMessage(content=user_input))

    with st.chat_message("user", avatar="🧑"):
        st.markdown(user_input)

    with st.chat_message("assistant", avatar="🤖"):
        response = st.write_stream(get_response(user_input, chat_history))

    chat_history.append(AIMessage(content=response))