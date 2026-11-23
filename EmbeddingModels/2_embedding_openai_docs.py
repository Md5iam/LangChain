from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-small', dimensions=32)

documents=[
  "My name is Siam",
  "I am 6 years old",
  "I love playing cricket"
]

result = embedding.embed_documents(documents)

print(str(result))
