from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

prompt = PromptTemplate(
  template='Answer the {question} from this {text}',
  input_variables=['question', 'text']
)

parser = StrOutputParser()

url = 'https://codeforces.com/'
loader = WebBaseLoader(url)

docs = loader.load()
# print(docs[0].page_content)

chain = prompt | model | parser

result = chain.invoke({
  'question': 'What is the upcoming round and who is the problem setter',
  'text': docs
})

print(result)