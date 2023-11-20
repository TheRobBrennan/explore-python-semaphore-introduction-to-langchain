import os
from dotenv import load_dotenv
from langchain.vectorstores.redis import Redis
from langchain.embeddings import OpenAIEmbeddings

# Load environment variables from .env file
load_dotenv()

embeddings = OpenAIEmbeddings()

# Define the schema based on the Redis hash structure
schema = {
    "content": "String",
    "content_vector": "Binary",  # Replace with the specific type if needed
    "source": "String",
}

rds = Redis.from_existing_index(

    embeddings, redis_url="redis://localhost:6379", index_name="chunk", schema=schema
)

results = rds.similarity_search("where does mrs ruan live")

print(results[0].page_content)