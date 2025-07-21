#from openai import OpenAI
#from dotenv import load_dotenv
#import os

# Carrega as variáveis do .env
#load_dotenv()

# Cria o cliente OpenAI usando a chave que está no .env
#client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

#def chat_with_gpt(message: str):
 #   response = client.chat.completions.create(
  #      model="gpt-3.5-turbo",
   #     messages=[
    #        {"role": "system", "content": "Você é uma atendente virtual de farmácia de manipulação chamada Ophelia."},
     #       {"role": "user", "content": message}
      #  ]
    #)
    #return response.choices[0].message.content

import random

def chat_with_gpt_mock(message: str):
    respostas_mock = [
        "Claro! Temos vários produtos prontos para você escolher.",
        "Olá! Atualmente temos suplementos, vitaminas e cosméticos prontos para entrega.",
        "Oi! Confira nossa linha de produtos prontos em nosso catálogo online.",
        "Temos diversas opções de produtos prontos para atender suas necessidades."
    ]
    return random.choice(respostas_mock)

