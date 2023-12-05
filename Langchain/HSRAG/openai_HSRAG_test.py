from timing_deco import time_deco



# HYBRID SEARCH
"""
BM25 Embedding Test
Required for hybrid searches, testing BM25 and Faiss Ensemble Retrieval
Dependencies:
    OpenAI API
    FAISS
    Langchain
    BM25 Retriever
"""



import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


from langchain.retrievers import BM25Retriever, EnsembleRetriever

from langchain.schema import Document

from langchain.vectorstores import Chroma
from langchain.vectorstores import FAISS


from langchain.embeddings.openai import OpenAIEmbeddings

embedding = OpenAIEmbeddings()

doc_list = [
    "I like apples",
    "I like oranges",
    "Apples and oranges are fruits",
    "I like computers by Apple",
    "I love fruit juice"
]



# BM25 RETRIEVER - SPARSE RETRIEVER
bm25_retriever = BM25Retriever.from_texts(doc_list)
bm25_retriever.k=2

retrieve01 = bm25_retriever.get_relevant_documents("Apple")
print(f"Semantic search results for 'Apple' is {retrieve01}")


retrieve02= bm25_retriever.get_relevant_documents("a green fruit")
print(f"Semantic search results for 'Apple' is {retrieve02}")


bm25_dict = bm25_retriever.dict
print(bm25_dict)




# EMBEDDINGS - DENS RETRIEVERS FAISS

faiss_vectorstore = FAISS.from_texts(doc_list, embedding)
faiss_retriever = faiss_vectorstore.as_retriever(search_kwargs={"k": 2})
faiss_retrieve01=faiss_retriever.get_relevant_documents("A green fruit")
print(f"Faiss Dense Retriever for 'a green fruit': {faiss_retrieve01}")




# ---------------------------------------- #
# ENSEMBLE RETRIEVER from LANGCHAIN
# initialize the ensemble retriever
ensemble_retriever = EnsembleRetriever(retrievers=[bm25_retriever, faiss_retriever], weights=[0.5,0.5])

docs = ensemble_retriever.get_relevant_documents("an orange fruit")
print(f"Results from Ensemble Retriever: {docs}")


docs02 = ensemble_retriever.get_relevant_documents("Apple Phones")
print(docs02)
