from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from langchain_community.tools import ShellTool
import platform


## Built in Tool - DuckDuckDo Search
wrapper = DuckDuckGoSearchAPIWrapper(region="us-en", max_results=5)
search_tool = DuckDuckGoSearchRun(api_wrapper=wrapper)

results = search_tool.invoke("top news in USA today")
# print(results)

# print(search_tool.name)
# print(search_tool.description)
# print(search_tool.args)

## Built in Tool - Shell Tool
shell_tool = ShellTool()
command = "dir" if platform.system() == "Windows" else "ls"

results = shell_tool.invoke({
  "commands": command
})
print(results)

