from sqlalchemy import Column, Integer, String, Float, ForeignKey
from .db import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Skill(Base):
    __tablename__ = "skills"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String)

class SkillScore(Base):
    __tablename__ = "skill_scores"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    skill = Column(String)
    score = Column(Float)
