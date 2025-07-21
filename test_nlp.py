print("Script iniciado")

from app.core.nlp import chat_with_gpt_mock

print("Função importada")

if __name__ == "__main__":
    print("Enviando pergunta...")
    pergunta = "Quais são os produtos prontos que vocês têm?"
    resposta = chat_with_gpt_mock(pergunta)
    print("Resposta:", resposta)
