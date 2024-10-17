
import google.generativeai as genai
import streamlit as st

genai.configure(api_key='AIzaSyB20I_q31ElpEr3TxP0sI0tdKF8iwOZrEA')
model = genai.GenerativeModel('gemini-1.5-flash')

def role_to_streamlit(role):
  if role == "model":
    return "assistant"
  else:
    return role

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history = [])

st.title("Chat with mamadou Ben!")

for message in st.session_state.chat.history:
    with st.chat_message(role_to_streamlit(message.role)):
        st.write(message)

if prompt := st.chat_input("What would you like to know?"):
    st.chat_message("user").markdown(prompt)
    
    response = st.session_state.chat.send_message(prompt) 
    
    with st.chat_message("assistant"):
        st.markdown(response.text)