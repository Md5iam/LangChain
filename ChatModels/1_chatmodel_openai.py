from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-5.4-mini', temperature=0.5, max_completion_tokens=100)
result = model.invoke("What is my name ?");

print(result.content)