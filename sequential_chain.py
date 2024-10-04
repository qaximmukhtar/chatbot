from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain
from dotenv import load_dotenv
import os


# Load the environment variables from the .env file
def load_api_key():
    load_dotenv()
    return os.getenv("OPENAI_API_KEY")


# Initialize the LLM model
def initialize_llm(api_key):
    return ChatOpenAI(openai_api_key=api_key, model_name="gpt-4")


# Create the first chain to summarize the problem
def create_problem_summary_chain(llm):
    template = """
    You are a problem-solving expert. Given the description of an issue, summarize the main problem briefly.

    Issue Description: {description} 
    Problem Summary:"""

    prompt_template = PromptTemplate(input_variables=["description"], template=template)
    return LLMChain(llm=llm, prompt=prompt_template)


# Create the second chain to suggest a solution
def create_solution_suggestion_chain(llm):
    template = """
    You are an expert consultant. Based on the problem summary provided, suggest a clear solution.

    Problem Summary:
    {summary}
    Proposed Solution:"""

    prompt_template = PromptTemplate(input_variables=["summary"], template=template)
    return LLMChain(llm=llm, prompt=prompt_template)


# Create the sequential chain
def create_sequential_chain(chain_1, chain_2):
    return SimpleSequentialChain(
        chains=[chain_1, chain_2], verbose=True
    )


# Run the sequential chain
def run_sequential_chain(description):
    # Load API key and initialize LLM
    api_key = load_api_key()
    llm = initialize_llm(api_key)

    # Create individual chains
    problem_summary_chain = create_problem_summary_chain(llm)
    solution_suggestion_chain = create_solution_suggestion_chain(llm)

    # Create and run the sequential chain
    overall_chain = create_sequential_chain(problem_summary_chain, solution_suggestion_chain)

    return overall_chain.run(description)


# Example usage
# description = "i am having problem with python print statement."
# result = run_sequential_chain(description)
# print(result)
