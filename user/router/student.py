from typing import List
from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session

from .. import models, schema
from .. import database
from passlib.context import CryptContext

router = APIRouter(
    prefix="/students",
    tags=['Student']
)





# class Hash():
#     def bcrypt(password: str):
#         return pwd_cxt.hash(password)

#     def verify(hashed_password,plain_password):
#         return pwd_cxt.verify(plain_password,hashed_password)


get_db = database.get_db
  
pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/", tags=["Student"])
def create_student(student: schema.StudentCreate, db: Session = Depends(get_db)):
    db_student = models.Student(
        name=student.name,  
        email=student.email,
        password = pwd_cxt.hash(student.password),
        enrollment_date=student.enrollment_date
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


@router.get("/{student_id}", tags=["Student"])
def read_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.put("/{student_id}", tags=["Student"])
def update_student(student_id: int, student: schema.StudentCreate, db: Session = Depends(get_db)):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    db_student.name = student.name
    db_student.email = student.email
    db_student.password = student.password
    db_student.enrollment_date = student.enrollment_date
    db.commit()
    db.refresh(db_student)
    return db_student


@router.delete("/{student_id}", tags=["Student"])
def delete_student(student_id: int, db: Session = Depends(get_db)):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(db_student)
    db.commit()
    return {"message": f"Student with id {student_id} deleted successfully"}
