from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

# Default store in C Drive ( We can do customization)
# os.environ['HF_HOME'] = 'D:/hugginface_cache' 

llm = HuggingFacePipeline.from_model_id(
  model_id='model_id_dibo',
  task='text-generation',
  pipeline_kwargs=dict(
    temperature=0.5,
    max_new_tokens=100
  )
)

model = ChatHuggingFace(llm=llm)

model.invoke("What is the BD means ?")