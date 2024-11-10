from code_1 import chain
from fastapi import FastAPI
from langserve import add_routes

app = FastAPI(title="Meu app api", description="responda minhas duvidas")


add_routes(app, chain, path="/conversa")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)