# install streamlit
# install streamlit-chat
# install openai


import streamlit as st
import openai
from streamlit_chat import message

# panggil API_key di code mike
# openai.api_key = st.secrets["api_secret"]

# create a function which will generate the calls from the API
# panggil code mike

st.title("QUERIER")

# Storing the chat
if 'generated' not in st.session_state:
    st.session-state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def get_text():
    input_text = st.text_input("User: ", "Hello", key="input")
    return input_text

user_input = get_text()

if user_input:
    output = # panggil fungsi generate dari API(user_input)
    # store the output
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    for i range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key = str(i))
        message(st.session_state['past'][i], is_user = True, key = str(i) + '_user')