# app.py
import uvicorn
from fastapi import FastAPI
from routing.book import router as books_routing
from database.session import init_db

# 👉 Импортируем модели, чтобы SQLAlchemy их знал до create_all()
from models import author, book

app = FastAPI(openapi_url="/core/openapi.json", docs_url="/core/docs")

# Создаём таблицы в базе
init_db()

# Подключаем роуты
app.include_router(books_routing)

@app.get("/")
def root():
    return {"message": "Сервер работает! Откройте /core/docs чтобы посмотреть API"}


if __name__ == "__main__":
    uvicorn.run("app:app",reload=True)