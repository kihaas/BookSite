import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routing.book import router as books_router

# Инициализация приложения FastAPI с настройками для документации
app = FastAPI(
    title="Bookstore API",
    description="API для управления книгами и авторами",
    version="1.0.0",
    openapi_url="/api/openapi.json",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

# Настройка CORS (Cross-Origin Resource Sharing) для безопасности
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # В продакшене нужно указать конкретные домены
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение роутеров С ПРЕФИКСОМ http://127.0.0.1:8000/api/v1/books
app.include_router(books_router, prefix="/api/v1")

# Точка входа для запуска сервера
if __name__ == "__main__":
    # В продакшене лучше использовать конфигурацию из переменных окружения
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # Только для разработки!
        workers=4,    # Для продакшена нужно подбирать оптимальное количество
    )