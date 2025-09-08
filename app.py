# app.py
import uvicorn
from fastapi import FastAPI, Request
from routing.book import router as books_routing
from database.session import init_db
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# 👉 Импортируeм модeли, чтобы SQLAlchemy их знал до create_all()
from models import author, book

app = FastAPI(openapi_url="/core/openapi.json", docs_url="/core/docs")

# Создаём таблицы в базе
init_db()

# Подключаeм роyты
app.include_router(books_routing)

# 📁 подключаем папку со статикой (css, js, картинки)
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

# 📁 подключаем папку с шаблонами
templates = Jinja2Templates(directory="frontend/templates")

# 👇 CORS (нужен, если фронт будет запускаться отдельно, например с Live Server)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # для обучeния можно поставить "*"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 👉 главная страница
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
