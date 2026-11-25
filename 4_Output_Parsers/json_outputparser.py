from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI( model="gemini-3.5-flash-lite" )

parser = JsonOutputParser()

template = PromptTemplate(
  template='Give me 3 fact about {topic} \n {format_instruction}',
  input_variables=['topic'],
  partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser
result = chain.invoke({
  'topic': 'Transformer'
})

print(result)