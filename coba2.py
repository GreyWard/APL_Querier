# install streamlit
# install streamlit-chat
# install openai


import streamlit as st
import openai
from streamlit_chat import message
import query_gen as qg

# panggil API_key di code mike

# openai.api_key = st.secrets["api_secret"]
openai.api_key = "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"

# create a function which will generate the calls from the API
# Struktur kode query_gen
# inisiasi terlebih dahulu struktur dari tabel database yang dimaksud
qg.initiate_table("CREATE TABLE Orders (\n  OrderID int,\n  CustomerID int,\n  OrderDate datetime,\n  OrderTime varchar(8),\n  PRIMARY KEY (OrderID)\n);\n\nCREATE TABLE OrderDetails (\n  OrderDetailID int,\n  OrderID int,\n  ProductID int,\n  Quantity int,\n  PRIMARY KEY (OrderDetailID)\n);\n\nCREATE TABLE Products (\n  ProductID int,\n  ProductName varchar(50),\n  Category varchar(50),\n  UnitPrice decimal(10, 2),\n  Stock int,\n  PRIMARY KEY (ProductID)\n);\n\nCREATE TABLE Customers (\n  CustomerID int,\n  FirstName varchar(50),\n  LastName varchar(50),\n  Email varchar(100),\n  Phone varchar(20),\n  PRIMARY KEY (CustomerID)\n);")
# masukan prompt yang akan diminta oleh user, diawali kalimat perintah
generated_query = qg.generate("computes the average total order value for all orders on 2023-04-01.")


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