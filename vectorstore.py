import json
from langchain_community.document_loaders import TextLoader
from langchain_core.documents.base import Document
from langchain_community.vectorstores import FAISS
from typing import List
from embedings import get_embeddings

# 배운 내용 위주로 구현, 어짜피 나중에 처음부터 다시 짜라고 하면 손으로 절대 못짤듯함,,

def load_documents() -> List[Document]:
    # 인코딩 깨짐 방지를 위해 TextLoader 사용
    loader = TextLoader('dataset/data.json', encoding='utf-8')
    loaded_doc = loader.load()
    
    # 텍스트로 불러온 뒤 JSON 파싱
    json_docs = json.loads(loaded_doc[0].page_content)
   
   # 여기 중요 효율적인 부분 
    return [
        Document(
            page_content=f"주제: {doc['title']}\n내용: {doc['content']}",
            metadata={
                'id': doc['id'],
                'category': doc['category'],
                'sub_category': doc['sub_category']
            }
        )
        for doc in json_docs
    ]

def embedding(docs: List[Document]):
    embeddings = get_embeddings()
    vectorstore = FAISS.from_documents(
        documents=docs,
        embedding=embeddings
    )
    return vectorstore


def save_vector_to_local(vectorstore):
    path_str = './exp-faiss'    
    vectorstore.save_local(path_str)


def load_vector_from_local():
    path_str = './exp-faiss'
    return FAISS.load_local(
        path_str,
        get_embeddings(),
        allow_dangerous_deserialization=True
    )

def init_vectorstore():
    docs = load_documents()
    vectorstore = embedding(docs)
    save_vector_to_local(vectorstore)
    return vectorstore


