from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


text = """
In Express.js, when a client sends a request to the server, the server processes that 
request and sends a response back to the client. For a single HTTP request, the server
is expected to send only one response. In our code, we use res.status(404).json() to
send a response when the requested user is not found in the database. For example,
when we try to delete a user whose ID does not exist, the database returns rowCount = 0
, which means no row was deleted. Inside the if condition, we send a 404 status code
with the message "User not found!". However, sending a response does not automatically.
"""

splitter = RecursiveCharacterTextSplitter(
  chunk_size=20,
  chunk_overlap=0,
)

result = splitter.split_text(text)
print(len(result))
print(result)
