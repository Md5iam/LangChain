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

# print(multiply.invoke({
#   'a':3,
#   'b':4
# }))

res1 = llm.invoke('hello this is siam')
# print(ans.text)

# tool binding
llm_with_tools = llm.bind_tools([multiply])

#tool calling 
res2 = llm_with_tools.invoke('hi how are you ?')
# print(res2)

res3 = llm_with_tools.invoke('multiply 2 with 3 ')
# print(res3)

#tool executions

x = res3.tool_calls[0]['args']
# print(multiply.invoke(x))

# It print a ToolMessage
# print(multiply.invoke(
#   {'name': 'multiply', 'args': {'b': 3, 'a': 2}, 'id': 'call_14921671241841112838', 'type': 'tool_call'}
# ))

y = res3.tool_calls[0]
multiply.invoke(y)






