from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from user.database import Base

class Student(Base):
    __tablename__ = "student"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)  
    email = Column(String)
    password = Column(String)
    enrollment_date = Column(String)

    games = relationship("Game", back_populates="student")


class Game(Base):
    __tablename__ = "game"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    game_type = Column(String)
    date_of_game = Column(String)
    max_participants = Column(Integer)
    stud_id = Column(Integer, ForeignKey("student.id"))  

    student = relationship("Student", back_populates="games")
