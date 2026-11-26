from langchain_community.document_loaders import CSVLoader

loader = CSVLoader('Social_Network_Ads.csv')

data = loader.load()

print(len(data))
print(data[0].page_content)
