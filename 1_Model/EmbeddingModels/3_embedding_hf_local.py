from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
  model_name='sentence-transformers/all-MiniLM-L6-v2'
)

documents=[
  "My name is Siam",
  "I am 6 years old",
  "I love playing cricket"
]

query_text = "This is BD"
# vector = embedding.embed_query(query_text);
vector = embedding.embed_documents(documents);

print(str(vector))