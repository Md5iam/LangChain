from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_classic.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda


# Basic Example
def word_count(text):
  return len(text.split())

# runnable_word_counter = RunnableLambda(word_count)

# cnt = runnable_word_counter.invoke('Hi how are me ?')
# print(cnt)


load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

parser = StrOutputParser()

prompt = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

joke_gen_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(word_count)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({
  'topic':'AI'
  })

final_result = """{} \n word count - {}""".format(result['joke'], result['word_count'])

print(final_result)