from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

# tool create
@tool
def multiply(a: int, b: int) -> int:
  """Given 2 numbers a and b this tool returns their product"""
  return a * b

#tool build
llm_with_tools = llm.bind_tools([multiply])

query = HumanMessage('can you multiply 3 with 1000')

messages = [query]

# tool execution
result = llm_with_tools.invoke(messages)

messages.append(result)

tool_result = multiply.invoke(result.tool_calls[0])

messages.append(tool_result)

ans = llm_with_tools.invoke(messages).text
print(ans)



