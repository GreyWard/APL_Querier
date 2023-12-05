# chatGPT client
# Cara pakai:
# import .py ini ke program yang ingin menggunakannya
# inisiasi variabel baru dengan kelas chatClient
# contoh: client = databaseClient('api_keynya')
import os
import openai

class chatClient:
    # Menginisiasikan client ke chatGPT, masukan api_key sebagai string disini
    def __init__(self,api_key):
        self.openai.api_key = api_key
        self.content_string = "Given the following SQL tables, your job is to write queries given a user's request.\n\n"
        self.query_prompt =  "Write a SQL query which "
       
    # Kirim metadata dari database hasil generate pada bigquery disini
    def sendMeta(self,table_meta):
        try:
            for table in table_meta:
                self.content_string += table
            return "meta saved!"
        except Exception as e:
            print(f"An error occured: {e}")
            return None
        

    # Fungsi generate query baru, return dalam bentuk string
    def generate(self,prompt):
        finished_prompt = self.query_prompt + prompt
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
            "role": "system",
            "content": self.content_string
            },
            {
            "role": "user",
            "content": finished_prompt
            }
        ],
        temperature=0,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        return response.choices[0].message["content"]