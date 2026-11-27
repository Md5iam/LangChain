from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite", temperature = 0.2)
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

## Step 1a - Indexing (Document Ingestion )
video_id = "Gfr50f6ZBvo"  # only the ID, not the full URL

try:
    ytt_api = YouTubeTranscriptApi()
    fetched = ytt_api.fetch(video_id, languages=["en"])

    # Flatten it to plain text
    transcript = " ".join(chunk.text for chunk in fetched)
    # print(transcript)

except TranscriptsDisabled:
    print("No captions available for this video.") 

## Step 1b - Indexing (Text Splitting)
splitter = RecursiveCharacterTextSplitter(chunk_size=3000, chunk_overlap=200)
chunks = splitter.create_documents([transcript])
# print(len(chunks)) 
# print(chunks[0])

## Step 1c & 1d - Indexing (Embedding Generation and Storing in Vector Store)
vector_store = FAISS.from_documents(chunks, embeddings)
# print(vector_store.index_to_docstore_id)

## Step 2 - Retrieval
retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 2}
)
# print(retriver)
ans = retriever.invoke("Whay is deepmind")
# print(ans)

## Step 3 - Augmentation
prompt = PromptTemplate(
    template="""
      You are a helpful assistant.
      Answer ONLY from the provided transcript context.
      If the context is insufficient, just say you don't know.

      {context}
      Question: {question}
    """,
    input_variables = ['context', 'question']
)

question          = "is the topic of nuclear fusion discussed in this video? if yes then what was discussed in using numerical point"
retrieved_docs    = retriever.invoke(question)
# print(retrieved_docs)

context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
# print(context_text)

final_prompt = prompt.invoke({
    'context': context_text,
    'question': question
})

# print(final_prompt)

## Step 4 - Generation
answer = llm.invoke(final_prompt)
# print(answer.text)



