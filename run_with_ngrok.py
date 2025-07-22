from pyngrok import ngrok
import uvicorn

# Se seu app estiver no arquivo app/main.py e a variável app for chamada 'app':
from app.main import app

if __name__ == "__main__":
    port = 8000
    public_url = ngrok.connect(port).public_url
    print(f"ngrok tunnel URL: {public_url}")
    uvicorn.run(app, host="0.0.0.0", port=port)
