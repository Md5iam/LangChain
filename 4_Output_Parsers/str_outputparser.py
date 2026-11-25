from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI( model="gemini-3.5-flash-lite" )

#1st prompt -> detailed report -> 2nd prmpt -> summary
template1 = PromptTemplate(
  template='Write a detailed report on {topic}',
  input_variables={'topic'}
)

template2 = PromptTemplate(
  template='Write 5 line summary on following text {text}',
  input_variables={'text'}
)

prompt1 = template1.invoke({
  'topic': 'black hole'
})
result1 = model.invoke(prompt1)

prompt2 = template2.invoke({
  'text': result1
})

result2 = model.invoke(prompt2)

print(result2.text)

