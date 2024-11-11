import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA

st.set_page_config(page_title="Gemini Chatbot", layout="wide", page_icon='🍊')
gemini_api_key = 'AIzaSyAnuaftcLvEgrnZYbutTmnX3XnUde0WU4Q'


st.title("🍊 Chat with Orange bot...")

if "history" not in st.session_state:
    st.session_state.history = []

def initialize_qa_chain(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as file:
        text = file.read()


    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_text(text)

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=gemini_api_key)

    vector_store = Chroma.from_texts(chunks, embeddings)

    model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=gemini_api_key)
    qa_chain = RetrievalQA.from_chain_type(
        llm=model,
        chain_type="stuff",
        retriever=vector_store.as_retriever()
    )

    return qa_chain

txt_path = 'corrected_output.txt' 
if gemini_api_key and txt_path:
    qa_chain = initialize_qa_chain(txt_path)

chatbox = st.empty()

if st.session_state.history:
    for item in st.session_state.history:
        st.chat_message(name="user", avatar="🧑").markdown(f"You: {item['query']}")
        st.chat_message(name="bot", avatar="🤖").markdown(f"Hey! bot: {item['answer']}")

query = st.chat_input("Type your question here...", key="query")

if query:
    with st.spinner("Finding the answer..."):
        answer = qa_chain.run(query)
        st.session_state.history.append({"query": query, "answer": answer})
        st.chat_message(name="user", avatar="🧑").markdown(f"{query}")
        st.chat_message(name="bot", avatar="🤖").markdown(f"{answer}")

