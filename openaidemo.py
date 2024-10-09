import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Access the API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI object using LangChain
llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name="gpt-4")

# Define the prompt template
# Modify the single_chain function to include custom memory
def single_chain(question, memory):
    prompt_template = """
    You are a knowledgeable and friendly assistant. This is the conversation so far:
    {history}

    Please provide a clear and concise answer to the following question:
    {question}
    """

    # Fill the template with the combined memory and the new question
    prompt = prompt_template.format(history=memory, question=question)

    # Create a prompt template object for LangChain to use
    prompt_obj = PromptTemplate(input_variables=["history", "question"], template=prompt_template)

    # Generate response using LLMChain
    chain = LLMChain(llm=llm, prompt=prompt_obj)
    response = chain.run({"history": memory, "question": question})

    return response
