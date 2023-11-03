# install streamlit
# install streamlit-chat
# install openai


import streamlit as st
import openai
from streamlit_chat import message

# panggil API_key di code mike

# openai.api_key = st.secrets["api_secret"]
openai.api_key = "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"

# create a function which will generate the calls from the API
def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = [{"role" : "user", "content" : prompt}],
        temperature=0,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
    message = response.choices[0].message["content"]
    return message


st.title("QUERIER")

# Storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def get_text():
    input_text = st.text_input("User: ", "Hello, how are you?", key="input")
    return input_text

user_input = get_text()

if user_input:
    output = generate_response(user_input) # panggil fungsi generate dari API(user_input)
    # store the output
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key = str(i))
        message(st.session_state['past'][i], is_user = True, key = str(i) + '_user')