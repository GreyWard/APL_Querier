import os
import openai

# ubah api key sesuai yang bisa dipakai
openai.api_key = "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"
content_string = "Given the following SQL tables, your job is to write queries given a user's request.\n\n"
query_prompt =  "Write a SQL query which "

# Menginisiasikan tabel pada prompt sehingga chatbot mengerti konten tabel
def initiate_table(table_content):
    global content_string
    content_string += table_content
    # example input: CREATE TABLE Orders (\n  OrderID int,\n  CustomerID int,\n  OrderDate datetime,\n  OrderTime varchar(8),\n  PRIMARY KEY (OrderID)\n);\n\nCREATE TABLE OrderDetails (\n  OrderDetailID int,\n  OrderID int,\n  ProductID int,\n  Quantity int,\n  PRIMARY KEY (OrderDetailID)\n);\n\nCREATE TABLE Products (\n  ProductID int,\n  ProductName varchar(50),\n  Category varchar(50),\n  UnitPrice decimal(10, 2),\n  Stock int,\n  PRIMARY KEY (ProductID)\n);\n\nCREATE TABLE Customers (\n  CustomerID int,\n  FirstName varchar(50),\n  LastName varchar(50),\n  Email varchar(100),\n  Phone varchar(20),\n  PRIMARY KEY (CustomerID)\n);
    

# Fungsi generate query baru, return dalam bentuk string
def generate(prompt):
    global query_prompt
    query_prompt = query_prompt + prompt
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
        "role": "system",
        "content": content_string
        },
        {
        "role": "user",
        "content": query_prompt
        }
    ],
    temperature=0,
    max_tokens=1024,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    return response.choices[0].message["content"]