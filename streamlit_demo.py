import os
import streamlit as st
import openai
from dotenv import load_dotenv
from sequential_chain import run_sequential_chain

# Load environment variables from a .env file
load_dotenv()

# Access OpenAI API key from the .env file
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

# Set the page layout of the Streamlit app
st.set_page_config(page_title="Chatbot", layout="wide")

# Title of the app
st.title("Simple Chatbot with OpenAI")

# User input area
def get_user_input():
    return st.text_input("You: ", "")

# Main logic of the chatbot
def chat():
    # Store the chat history in session state
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # Display chat messages from the session state
    for message in st.session_state["messages"]:
        st.write(f"{message['role']}: {message['content']}")

    # Get user input and display it
    user_input = get_user_input()
    if user_input:
        st.session_state["messages"].append({"role": "User", "content": user_input})
        # Generate a response from OpenAI and display it
        bot_response = run_sequential_chain(user_input)
        st.write(f"bot: {bot_response}")
        # st.success(user_input)

# Run the chat function
chat()
#
# import streamlit as st
#
# st.title("Message Display App")
#
# # Input field
# user_input = st.text_input("Enter your message:")
#
# # Output field
# if user_input:
#     st.write("Your message:")
#     st.success(user_input)