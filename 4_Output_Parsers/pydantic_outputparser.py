from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import Field , BaseModel

load_dotenv()

model = ChatGoogleGenerativeAI( model="gemini-3.5-flash-lite" )

class Person(BaseModel):
  name: str = Field(description='Name of the person ')
  age: int = Field(description= 'Age of the person')
  city: str = Field(description= 'Name of the city the person belongs to')

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Generate the name, age and city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser 

result = chain.invoke({
  'place': 'bangladeshi'
})
print(result)


# prompt = template.invoke({
#   'place': 'bangladeshi'
# })
# # print(prompt)
# result = model.invoke(prompt)
# final_result = parser.parse(result.text)
# # print(final_result)