from llama_index import VectorStoreIndex, SimpleDirectoryReader
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

reader = SimpleDirectoryReader(input_files=[Path('/Users/baptistepugnaire/Documents/Projects/Local/llm101/data/paul_graham_essay.txt')])
index = VectorStoreIndex.from_documents(reader.load_data())

query_engine = index.as_query_engine()
response = query_engine.query('Where did the author do growing up?')
print(response)

chat_engine = index.as_chat_engine()
response = chat_engine.chat("Tell me a joke.")
print(response)
