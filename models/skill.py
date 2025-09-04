# models/skill.py
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from database.session import Base  # поправь путь, если у тебя иначе

class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True, nullable=False)
    level = Column(String(50), nullable=True)  # например: Beginner/Middle/Senior
    description = Column(Text, nullable=True)

    # связь с Project через таблицу связей (объявим в project.py)
    projects = relationship("Project", secondary="project_skills", back_populates="skills")
