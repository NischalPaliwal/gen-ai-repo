from llama_index.llms.openai import OpenAI
from llama_index.readers.web import SimpleWebPageReader
from llama_index.core import VectorStoreIndex
import llama_index
import os
from dotenv import load_dotenv

load_dotenv()

def main(url : str) -> None:
    document = SimpleWebPageReader(html_to_text=True).load_data(urls=[url])
    index = VectorStoreIndex.from_documents(documents=document)
    query_engine = index.as_query_engine()
    response = query_engine.query("What is Gen AI?")
    print(response)

if __name__ == "__main__":
    main(url="https://learn.microsoft.com/en-us/training/paths/create-custom-copilots-ai-studio")