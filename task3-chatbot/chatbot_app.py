import streamlit as st

st.title("Simple AI Chatbot")

st.write("This is a basic AI chatbot created as part of Task 3.")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
user_input = st.chat_input("Type your message here")

def bot_reply(user_text):
    user_text = user_text.lower()

    if "hello" in user_text or "hi" in user_text:
        return "Hello! How can I help you today?"
    elif "your name" in user_text:
        return "I am a simple AI chatbot created for an internship task."
    elif "help" in user_text:
        return "Sure! You can ask me basic questions."
    elif "bye" in user_text:
        return "Goodbye! Have a nice day 😊"
    else:
        return "I'm still learning. Please ask something simple."

# When user sends message
if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    reply = bot_reply(user_input)

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    st.rerun()
