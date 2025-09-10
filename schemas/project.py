# schemas/project.py
from pydantic import BaseModel, HttpUrl
from typing import Optional, List
from datetime import date
from .skill import SkillOut, SkillBase

class ProjectBase(BaseModel):
    title: str
    description: Optional[str] = None
    url: Optional[str] = None  # можно сузить до HttpUrl, если всегда полноценный URL
    started_on: Optional[date] = None
    finished_on: Optional[date] = None

class ProjectCreate(ProjectBase):
    # список имен скиллов, которые нужно привязать при создании
    skills: List[SkillBase] = []

class ProjectOut(ProjectBase):
    id: int
    skills: List[SkillOut] = []
    class Config:
        from_attributes = True
