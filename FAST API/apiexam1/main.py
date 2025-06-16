from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

students = {}
# {"name":"김철수", "age":"20세", "major":"컴퓨터공학과", "grade":"2학년"}
# {"name":"이영희", "age":"21세", "major":"경영학과"}
# {"name":"박민수", "age":"19세", "major":"전자공학과", "grade":"1학년"}

class StudentCreate(BaseModel):
    name: str
    age : int
    major: str
    grade: Optional[str] = "(학년 정보 없음)"

class StudentResponse(BaseModel):
    name: str
    age : int
    major: str
    grade: Optional[str] = "(학년 정보 없음)"

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    age : Optional[int] = None
    major: Optional[str] = None
    grade: Optional[str] = None


@app.get("/")
def get_system():
    system_data = {
        "message": "학생 정보 관리 시스템 API",
        "total_students": len(students),
        "available_endpoints": ["/students", "students/{id}"]
    }
    return system_data

@app.get("/students", response_model=List[StudentResponse])
def get_students():
    if len(students) == 0:
        raise HTTPException(status_code=400, detail="등록된 학생이 없습니다.")
    return list(students.values())

@app.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id : int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="찾을 수 없는 id 입니다.")
    return students[student_id]

@app.post("/students", response_model=StudentResponse)
def create_student(student : StudentCreate):
    student_num = len(students) + 1
    students[student_num] = student
    return student

@app.put("/students/{student_id}")
def update_student(student_id: int, update : StudentUpdate):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="찾을 수 없는 id입니다.")
    stored_student: StudentCreate = students[student_id]
    update_data = update.model_dump(exclude_unset=True)
    update_student = stored_student.model_copy(update=update_data)
    students[student_id] = update_student
    return update_student

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="찾을 수 없는 id입니다.")
    students.pop(student_id)
    return f"{student_id}번 학생이 삭제되었습니다."

@app.get("/students/major/{major_name}")
def get_major(major_name: str):
    major_in = False
    students_major = list(students.values())
    for major_find in students_major:
        if major_find["major"] == major_name:
            major_in = True
    if major_in == False:
        raise HTTPException(status_code=404, detail="찾을 수 없는 전공입니다.")
    return list(students.values[major_name])