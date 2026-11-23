from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
  repo_id="meta-llama/Llama-3.1-8B-Instruct",
  task="text-generation",
  # huggingfacehub_api_token=None,  # Reads the environment variable
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What BD means?")

print(result.content)