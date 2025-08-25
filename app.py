# app.py
import uvicorn
from fastapi import FastAPI
from routing.book import router as books_routing
from database.session import init_db
from fastapi.middleware.cors import CORSMiddleware

# 👉 Импортируем модели, чтобы SQLAlchemy их знал до create_all()
from models import author, book

app = FastAPI(openapi_url="/core/openapi.json", docs_url="/core/docs")

# Создаём тaблицы в бaзеуууууу
init_db()

# Подключаем роутыыыыыыы
app.include_router(books_routing)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # для обучения можно поставить "*"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Сервер работает! Откройте /core/docs чтобы посмотреть API"}


if __name__ == "__main__":
    uvicorn.run("app:app",reload=True)