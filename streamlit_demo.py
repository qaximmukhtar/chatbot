import os
import streamlit as st
import openai
from dotenv import load_dotenv
from sequential_chain import run_sequential_chain
from openaidemo import single_chain

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


# Custom memory management without built-in functions
def get_combined_memory():
    # If there's no previous memory, return an empty string
    if "messages" not in st.session_state or not st.session_state["messages"]:
        return ""

    # Combine the conversation history into a single string to serve as memory
    memory = ""
    for message in st.session_state["messages"]:
        memory += f"{message['role']}: {message['content']}\n"

    return memory


# Main logic of the chatbot
def chat():
    # Initialize the chat history in session state if not present
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # Display the previous chat messages
    for message in st.session_state["messages"]:
        st.write(f"{message['role']}: {message['content']}")

    # Get user input
    user_input = get_user_input()

    if user_input:
        # Append user input to session state memory
        st.session_state["messages"].append({"role": "User", "content": user_input})

        # Get the combined memory (chat history so far)
        memory = get_combined_memory()

        # Generate bot response based on memory
        bot_response = single_chain(user_input, memory)

        # Append the bot's response to the session state memory
        st.session_state["messages"].append({"role": "bot", "content": bot_response})

        # Display the bot response
        st.write(f"bot: {bot_response}")


# Run the chat function
chat()

