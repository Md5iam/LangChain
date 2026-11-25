from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
  name: str = 'Default Name'
  age: Optional[int] = None
  email: EmailStr
  cgpa: float = Field(gt=0, lt=10, default=5)

new_student = {
  # 'name': 'siam'
  'age': 10,
  'email': 'abc@gmail.com',
  'cgpa': 9
}

student = Student(**new_student)
# print(student)
# print(type(student))

student_json = student.model_dump_json()
print(student_json)