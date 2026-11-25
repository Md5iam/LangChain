from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI( model="gemini-3.5-flash-lite" )

chat_template = ChatPromptTemplate([
  ('system', 'You are a helpful {domain} expert'),
  ('human', 'Explain in simple terms, what is {topic}')
  # SystemMessage(content='You are a helpful {domain} expert'),
  # HumanMessage(content='Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain':'cricket', 'topic':'ML' });

print(prompt)