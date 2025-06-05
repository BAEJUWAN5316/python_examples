from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

students = []
# {"name":"김철수", "age":"20세", "major":"컴퓨터공학과", "grade":"2학년"}
# {"name":"이영희", "age":"21세", "major":"경영학과"}
# {"name":"박민수", "age":"19세", "major":"전자공학과", "grade":"1학년"}

class StudentCreate(BaseModel):
    name: str
    age : str
    major: str
    grade: Optional[str] = "(학년 정보 없음)"

class StudentResponse(BaseModel):
    name: str
    age : str
    major: str
    grade: Optional[str] = "(학년 정보 없음)"
    id = Optional[int]


@app.get("/")
def get_system():
    system_data = {
        "message": "학생 정보 관리 시스템 API",
        "total_students": len(students),
        "available_endpoints": ["/students", "students/\{id\}"]
    }
    return system_data

@app.get("/students")
def get_students():
    return students

@app.get("/students/{student_id}", response_model=StudentResponse)
def get_student():
    pass

@app.post("/students", response_model=StudentResponse)
def create_student(student : StudentCreate):
    students.append(student)
    return students
