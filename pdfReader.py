import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA

st.set_page_config(page_title="pdfAI", layout="wide", page_icon='🧠')
st.title("🍊 Hello I'm under the water...")

 
gemini_api_key = 'AIzaSyCyqvqdoZuqM7X-QYvMpQxt0wMixzXPH04' # gneugneu don't push the api key
uploaded_pdf = 'resume_Damien-1.pdf'

if uploaded_pdf and gemini_api_key:
    pdf_reader = PdfReader(uploaded_pdf)
    text = ""
    
    for page in pdf_reader.pages:
        text += page.extract_text()

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

    query = st.text_input("ask your quiestion:")
    
    if query:
        with st.spinner("Finding the answer..."):
            answer = qa_chain.run(query)
            st.write("### Answer:")
            st.write(answer)
