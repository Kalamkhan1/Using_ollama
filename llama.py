# Import necessary modules
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
import streamlit as st
st.title('Langchain Chatbot With Different Models') 
options = ["llama2", "Gemma:2B", "Moondream","phi3"]
selection = st.selectbox("Choose an option:", options)

# Display the selection
st.write("You have selected:", selection)

input_text=st.text_input("Ask your question!")  
# Get the user's selection


llm=Ollama(model=selection)

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the questions"),
        ("user","Question:{question}")
    ]
)
chain=prompt|llm
if input_text:
    st.write(chain.invoke({"question":input_text}))