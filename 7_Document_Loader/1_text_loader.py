from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

parser = StrOutputParser()


loader = TextLoader('cricket.txt', encoding='utf-8')

docs = loader.load()

prompt = PromptTemplate(
    template='Write a summary for the following poem in 50 word - \n {poem}',
    input_variables=['poem']
)

# output will be list of document

# print(type(docs))
# print(docs[0].page_content)
# print(docs[0].metadata)

chain = prompt | model | parser

print(chain.invoke({'poem':docs[0].page_content}))