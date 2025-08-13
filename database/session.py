# database/session.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import logging

logger = logging.getLogger(__name__)

# Подключение к SQLite (можно заменить на PostgreSQL/MySQL)
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# Создаем движок БД
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},  # Только для SQLite!
    echo=True  # Лог SQL-запросов (в продакшене можно выключить)
)

# Создаём фабрику сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей
Base = declarative_base()

def init_db():
    """Создание всех таблиц в БД (аналог миграций для простых проектов)"""
    try:
        logger.info("Creating database tables")
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables created successfully")
    except Exception as e:
        logger.error(f"Error creating database tables: {str(e)}", exc_info=True)
        raise

# Зависимость для получения сессии БД
def get_db():
    """Генератор, отдающий сессию БД и закрывающий её после использования"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
