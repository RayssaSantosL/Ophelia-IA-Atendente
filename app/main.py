from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="IA Ophelia - Atendente Virtual")

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "API da IA Ophelia está online!"}
