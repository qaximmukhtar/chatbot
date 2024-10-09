# conversation_memory.py
from langchain.memory import ConversationBufferMemory

# Function to initialize conversation buffer memory
def initialize_memory():
    # Initialize the ConversationBufferMemory
    memory = ConversationBufferMemory()

    # Return the memory object to be used in the chat
    return memory
