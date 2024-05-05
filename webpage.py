from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain.document_loaders import WebBaseLoader
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI


def webpage_chat(question, url, openai_api_key):

# Load content from a webpage
    loader = WebBaseLoader(url)
    pages = loader.load()

    text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=150)
    docs = text_splitter.split_documents(pages)
    print(docs)

    embedding = OpenAIEmbeddings(openai_api_key=openai_api_key)

    # Create a vector store, here I'm using chromadb
    persist_directory = 'docs/chroma/'
    vectordb = Chroma.from_documents(documents=docs, embedding=embedding, persist_directory=persist_directory)
    
    # Similarity search
    context = vectordb.similarity_search(question,k=2)
    # context_1 = "\n".join(result["text"] for result in context_results)
    print(context)

    # Building prompt template
    template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. Use three sentences maximum. Keep the answer as concise as possible. Always say "thanks for asking!" at the end of the answer. 
    {context}
    Question: {question}
    Helpful Answer:"""
    
    QA_CHAIN_PROMPT = PromptTemplate.from_template(template)

    # Initialize ChatOpenAI for question-answering
    llm = ChatOpenAI(temperature=0, openai_api_key=openai_api_key)

    # Initialize question-answering chain
    qa_chain = RetrievalQA.from_chain_type(llm, retriever=vectordb.as_retriever(), return_source_documents=True, chain_type_kwargs={"prompt": QA_CHAIN_PROMPT})

    result = qa_chain({"query": question})
    answer = result["result"]
    return answer
