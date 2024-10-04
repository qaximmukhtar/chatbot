'''from openai import OpenAI
from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv()

# Access the variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "how to plant a tree"}
    ]
)

# Access the content from the response object
content = response.choices[0].message.content

# Print the content
print(content)'''



from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv()

# Access the API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI object using LangChain
llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name="gpt-4o")

# Define the prompt template
prompt = PromptTemplate(
    input_variables=["question"],
    template="You are a helpful assistant. {question}"
)

# Create an LLM chain using the prompt and OpenAI object
chain = LLMChain(llm=llm, prompt=prompt)

# Execute the chain by passing the user question
response = chain.invoke("who ia christiano ronaldo")

# Print the response
print(response)
print(response["text"])


