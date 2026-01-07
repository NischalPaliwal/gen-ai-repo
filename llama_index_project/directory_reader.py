from llama_index.core import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex
import os
import sys
from dotenv import load_dotenv

load_dotenv()

def main(url : str) -> None:
    documents = SimpleDirectoryReader(input_dir="").load_data()
    index = VectorStoreIndex.from_documents(documents=documents)
    query_engine = index.as_query_engine()
    response = query_engine.query("What is Gen AI?")
    print(response)

if __name__ == "__main__":
    main(url="")