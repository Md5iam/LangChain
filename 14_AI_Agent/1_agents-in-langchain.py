from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
import requests
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from langchain_classic.agents import create_react_agent, AgentExecutor
from langchain_classic import hub
from langsmith import Client
import os

load_dotenv()
weather_api_key = os.getenv("WEATHER_API_KEY")

wrapper = DuckDuckGoSearchAPIWrapper(region="us-en", max_results=5)


search_tool = DuckDuckGoSearchRun(api_wrapper=wrapper)

@tool
def get_weather_data(city: str) -> str:
    """
    This function fetches the current weather data for a given city.
    """
    url = "https://api.weatherstack.com/current"

    params = {
        "access_key": weather_api_key,
        "query": city
    }

    response = requests.get(url, params=params, timeout=10)
    data = response.json()

    return str(data)

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite", temperature=0.2)

# Step 2: Pull the ReAct prompt from LangChain Hub
prompt = Client().pull_prompt("hwchase17/react", dangerously_pull_public_prompt=True)  # pulls the standard ReAct agent prompt

# Step 3: Create the ReAct agent manually with the pulled prompt
agent = create_react_agent(
    llm=llm,
    tools=[search_tool, get_weather_data],
    prompt=prompt
)


# Step 4: Wrap it with AgentExecutor
agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool, get_weather_data],
    verbose=True
)


# Step 5: Invoke
response = agent_executor.invoke({
  "input": "what is the capital of Indian and what is the current weather status there ?"
})
print(response)





