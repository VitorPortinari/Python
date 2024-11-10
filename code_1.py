from langchain.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain_core.output_parsers import StrOutputParser

# Define the prompt template
mensagens_template = """Questions: {question}

Answer: """

# Initialize the prompt as a ChatPromptTemplate
prompt = ChatPromptTemplate.from_template(mensagens_template)

# Initialize the model (e.g., Ollama LLM)
modelo = OllamaLLM(model="llama3")

# Initialize the output parser
parser = StrOutputParser()

# Set up the chain by combining prompt, model, and parser
chain = prompt | modelo | parser

# Invoke the chain with the question
response = chain.invoke({"question": "what are you?"})

print(response)
