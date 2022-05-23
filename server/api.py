from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from .routes import router as NoteRouter

app = FastAPI(    
    title="FastApi Hosted on Vercel",
    description="Teste de API com deploy na vercel, CRUD inserção de notas sem persistência em BD",
    version="0.0.1",
    contact={
        "name": "Robinson Enedino",
        "url": "https://www.enedino.com.br",
        "email": "robinsonbrz@gmail.com",
        },
    )


@app.get("/", tags=["Root"])
async def read_root() -> dict:
    # response = RedirectResponse(url='https://www.enedino.com.br')
    response = RedirectResponse(url='/docs')
    return response

app.include_router(NoteRouter, prefix="/note")
