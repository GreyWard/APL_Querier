# .py untuk interface web app Querier
# integrasi Front-End dan Back-End

import streamlit as st
import openai
import random
import query_gen as qg
import bigquery_wrapper as bq
from google.oauth2 import service_account
from google.cloud import bigquery

#------------------INITIATE CREDENTIALS FOR DEV-----------------------------------------------------------
api_key = st.secrets["OPENAI_API_KEY"]
credentials = "querier-test-01-a8cea750269c.json"


#------------------INITIATE QUERY GEN & BIGQUERY WRAPPER--------------------------------------------------
query_gpt = qg.chatClient(api_key)
client = bq.databaseClient(credentials)
metadata = client.fetch_metadata()
response = query_gpt.sendMeta(metadata)

#------------------------------------STREAMLIT------------------------------------------------------------
st.set_page_config(page_title="Querier",
                   initial_sidebar_state="collapsed", 
                   layout="wide")
st.title("Querier")

# function for streamlit
def button_resp():
    if st.session_state.button1:
        q_resp = st.chat_message("assistant")
        # Assistant's message with the result
        q_resp.write(client.send_query(query_gpt.generate(prompt)))
        #st.table()
        #st.session_state.messages.append({"role": "assistant", "content": result})

    elif st.session_state.button2:
        st.session_state.messages.append({"role": "assistant", "content": "Let's try another prompt."})
    
    # Clear button states after processing
    st.session_state.button1 = False
    st.session_state.button2 = False

# ---SIDEBAR---
with st.sidebar:
    st.text_input("Username")
    st.text_input("Password")

    tab1, tab2 = st.tabs(["Tutorial", "About Us"])
    
    with tab1:
        st.markdown("All you need is insert prompt")
    
    with tab2:
        st.markdown("A project to help people play with SQL without any prior knowledge!")

# ---CHAT ELEMENT---
prompt = st.chat_input("Insert your prompt here", key='prompt')

# inisiasi chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Interaksi Dalam Chat
if prompt:
    # user side
    st.session_state.messages.append({"role":"user", "content":prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # assistant side
    with st.chat_message("assistant"):
        response = query_gpt.generate(prompt)
        st.session_state.messages.append({"role":"assistant", "content":response})
        st.markdown(f"{response}. Do you want to execute?")

        # button to execute
        col1, col2 = st.columns([1,1])
        
        with col1:
            button1 = st.button('✅ Yes', key = 'button1', use_container_width=True, on_click= button_resp)

        with col2:
            button2 = st.button('❌ No', key = 'button2', use_container_width = True, on_click= button_resp)