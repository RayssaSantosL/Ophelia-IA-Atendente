# 💊🤖 Ophelia - Atendente Virtual para Farmácia de Manipulação

Ophelia é uma **API inteligente** desenvolvida em Python com FastAPI, integrada ao ChatGPT, criada para atender clientes de farmácias de manipulação via chatbot.  
O objetivo é responder orçamentos, dúvidas sobre manipulação, prazos, produtos e muito mais, de forma rápida, natural e personalizada.

---

## 📌 **Funcionalidades atuais**

✅ Detecta e responde mensagens dos clientes usando IA (ChatGPT)  
✅ Estrutura pronta para integração com WhatsApp  
✅ Endpoint único para processar mensagens  
✅ Código modular, limpo e fácil de evoluir

---

## 🛠 **Tecnologias utilizadas**

- Python 3.11+
- FastAPI
- OpenAI SDK
- python-dotenv
- Uvicorn (servidor ASGI)
- Postman (para testes)

---

## 📂 **Estrutura do projeto**

```
app/
├── api/
│   └── routes.py          # Rotas da API
├── core/
│   └── nlp.py             # Integração com ChatGPT
├── models/
│   └── schemas.py         # Schemas Pydantic
└── main.py                # Inicialização FastAPI
.env                       # Variáveis de ambiente (NÃO subir no git)
.env.example               # Exemplo do .env
requirements.txt           # Dependências
README.md                  # Documentação
```

---

## 🚀 **Como rodar localmente**

1️⃣ Clone o projeto e entre na pasta:

```bash
git clone https://github.com/seu-usuario/ophelia-bot.git
cd ophelia-bot
```

2️⃣ Crie um ambiente virtual e ative:

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate    # Windows
```

3️⃣ Instale as dependências:

```bash
pip install -r requirements.txt
```

4️⃣ Copie o arquivo `.env.example` para `.env` e insira sua chave da OpenAI:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
```

5️⃣ Rode a aplicação:

```bash
uvicorn app.main:app --reload
```

---

## 🧪 **Como testar**

- Abra o navegador e acesse a documentação automática:
```
http://127.0.0.1:8000/docs
```

- Use o endpoint `POST /process_message/` com um JSON:
```json
{
  "text": "Quero saber o preço do colágeno"
}
```

- Você receberá a resposta gerada pela IA.

- Também é possível testar via Postman:
  - Método: POST
  - URL: http://127.0.0.1:8000/process_message/
  - Body → raw → JSON

---

## 🧠 **Como funciona**

O endpoint chama a função `chat_with_gpt` que:
- Envia a mensagem do cliente para o ChatGPT
- Retorna a resposta da IA de forma natural, pronta para ser enviada ao cliente

---

## 🌱 **Possíveis evoluções**

✅ Salvar histórico de conversas em banco de dados  
✅ Integração com API do WhatsApp (ex.: Twilio, Zenvia, WhatsApp Cloud API)  
✅ Detectar e tratar intents específicas (ex.: orçamento, produtos prontos, etc.)  
✅ Implementar fila de atendimento ou escalonamento para atendente humano  
✅ Deploy em nuvem (Render, Vercel, Railway, etc.)

---

## ✨ **Créditos**

Desenvolvido por Rayssa Santos Lima ❤️

---

## 📄 **Licença**

Este projeto é privado ou protegido. Para uso comercial, consulte os autores.