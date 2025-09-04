# models/project.py
from sqlalchemy import Column, Integer, String, Text, Date, Table, ForeignKey
from sqlalchemy.orm import relationship
from database.session import Base  # поправь путь

# таблица связей многие-ко-многим
project_skills = Table(
    "project_skills",
    Base.metadata,
    Column("project_id", ForeignKey("projects.id", ondelete="CASCADE"), primary_key=True),
    Column("skill_id", ForeignKey("skills.id", ondelete="CASCADE"), primary_key=True),
)

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False, index=True)
    description = Column(Text, nullable=True)
    url = Column(String(300), nullable=True)        # ссылка на GitHub/дему
    started_on = Column(Date, nullable=True)
    finished_on = Column(Date, nullable=True)

    skills = relationship("Skill", secondary=project_skills, back_populates="projects")
