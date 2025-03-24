import streamlit as st
import google.generativeai as genai
from datetime import date

# Streamlit app configuration
st.set_page_config(page_title="ChatBot", page_icon='🤖', layout='wide', initial_sidebar_state='expanded')

# Initialize session state
if 'chat' not in st.session_state:
    api_key = "AIzaSyDu7xASPL8PYzwOV4gPu3HakdjpLp3e-KQ"
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-pro')
    st.session_state.chat = model.start_chat(history=[])
    st.session_state.history = []
    st.session_state.model = model
    st.session_state.chat_sessions = []

if 'today_date' not in st.session_state:
    st.session_state.today_date = date.today().strftime("%d %B %Y")

# Custom CSS for dark theme and modern UI
st.markdown("""
    <style>
        /* Background styling */
        .stApp {
            background: linear-gradient(135deg, #0a0b0e, #00210b);
            color: white;
        }

        /* Sidebar styling */
        .sidebar .sidebar-content {
            background: #0f0f0f;
            color: #ddd;
        }

        .sidebar .sidebar-content .stButton>button {
            border-radius: 10px;
            background-color: #00b150;
            color: white;
        }

        /* Header styling */
        .chat-header {
            text-align: center;
            font-size: 24px;
            margin-bottom: 20px;
            color: #fff;
        }

        /* Chat bubbles */
        .user-message {
            border-radius: 12px;
            padding: 10px;
            margin: 10px 0;
            max-width: 80%;
            align-self: flex-end;
            background: #00b150;
            color: white;
        }

        .bot-message {
            border-radius: 12px;
            padding: 10px;
            margin: 10px 0;
            max-width: 80%;
            align-self: flex-start;
            background: #1a1a1a;
            border: 1px solid #333;
            color: white;
        }

        /* Date label */
        .chat-date {
            text-align: center;
            margin: 10px 0;
            padding: 5px 10px;
            border-radius: 10px;
            background: #222;
            color: #aaa;
            display: inline-block;
        }

        .message-container {
            display: flex;
            flex-direction: column;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar layout
with st.sidebar:
    st.markdown("### 📁 My Chats")

    # Display chat history links with delete button
    for i, chat in enumerate(st.session_state.chat_sessions):
        col1, col2 = st.columns([0.8, 0.2])
        with col1:
            if st.button(f"Chat {i + 1}", key=f"chat_{i}", use_container_width=True):
                st.session_state.chat = st.session_state.model.start_chat(history=[{"role": "user", "parts": [m["user"]]} if 'user' in m else {"role": "model", "parts": [m["bot"]]} for m in chat])
                st.session_state.history = chat
                st.rerun()
        with col2:
            if st.button("❌", key=f"delete_{i}", use_container_width=True):
                del st.session_state.chat_sessions[i]
                st.rerun()

    # New chat button
    if st.button("New Chat", use_container_width=True):
        if st.session_state.history:
            st.session_state.chat_sessions.append(st.session_state.history)
        st.session_state.chat = st.session_state.model.start_chat(history=[])
        st.session_state.history = []
        st.rerun()

# Main content
st.markdown('<div class="chat-header">🤖 ChatBot</div>', unsafe_allow_html=True)

# Display chat history
st.markdown(f'<div class="chat-date">{st.session_state.today_date}</div>', unsafe_allow_html=True)
for message in st.session_state.history:
    if 'user' in message:
        st.markdown(f'<div class="message-container"><div class="user-message">{message["user"]}</div></div>', unsafe_allow_html=True)
    if 'bot' in message:
        st.markdown(f'<div class="message-container"><div class="bot-message">{message["bot"]}</div></div>', unsafe_allow_html=True)

# Function to add message
def add_message(user, bot):
    st.session_state.history.append({"user": user, "bot": '🤖\n\n' + bot})

# Handle input
question = st.chat_input("Type your prompt here...")
if question:
    try:
        response = st.session_state.chat.send_message(question)
        add_message(question, response.text)
        st.rerun()
    except Exception as e:
        st.error(f"Error generating response: {e}")
