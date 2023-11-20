import os
from dotenv import load_dotenv
from langchain.vectorstores.redis import Redis
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA, ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory

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

retriever = rds.as_retriever()
model = ChatOpenAI(
    temperature= 0,
    model_name= 'gpt-3.5-turbo',
)

# Add conversational memory to our chat bot
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
qa = ConversationalRetrievalChain.from_llm(llm=model, retriever=retriever, memory=memory)

print("Ask any question regarding The Four Corners in California book:")
# keep the bot running in a loop to simulate a conversation
while True:
    question = input()
    result = qa({"question": question})
    print (result["answer"])
