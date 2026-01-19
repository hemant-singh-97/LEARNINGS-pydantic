from pydantic import BaseModel, field_validator, Field
from typing import Annotated, Any, Dict
from uuid import UUID
from datetime import date, datetime, timedelta

from data import data1, DepartmentEnum

class Student(BaseModel):
    id: UUID
    name: str
    date_of_birth: date
    GPA: Annotated[float, Field(ge=0.0, le=5.0)]
    course: str | None
    department: DepartmentEnum
    fees_paid: bool

    @field_validator("date_of_birth")
    def ensure_16_or_older(cls, value: date) -> date:
        sixteen_years_ago = datetime.now() - timedelta(days=16*365)
        sixteen_years_ago = sixteen_years_ago.date()
        
        if value > sixteen_years_ago:
            raise ValueError("Student must be at least 16 years old.")
        return value

for item in data1:
    student = Student(**item)
    print("Object:", student)               # Pydantic model object -> Direct object
    print("Dict:", student.model_dump())          # Dictionary representation -> A Dictionary with values as python objects
    print("JSON:", student.model_dump_json())    # JSON representation -> A JSON string
    print("-"*20)

wrong_gpa_student : Dict[str, Any] = {
    "id": "d15782d9-3d8f-4624-a88b-c8e836569df8",
    "name": "Eric Travix",
    "date_of_birth": "1995-05-25",
    "GPA": "5.1",
    "course": "Computer Science",
    "department": "Science and Engineering",
    "fees_paid": False
}
try :
    student = Student(**wrong_gpa_student)
except Exception as e:
    print(f"Error: {e}")
    print("-"*20)

underage_student : Dict[str, Any] = {
    "id": "d15782d9-3d8f-4624-a88b-c8e836569df8",
    "name": "Eric Travix",
    "date_of_birth": "2020-05-25",
    "GPA": "3.0",
    "course": "Computer Science",
    "department": "Science and Engineering",
    "fees_paid": False
}
try :
    student = Student(**underage_student)
except Exception as e:
    print(f"Error: {e}")
    print("-"*20)

wrong_department_student : Dict[str, Any] = {
    "id": "d15782d9-3d8f-4624-a88b-c8e836569df8",
    "name": "Eric Travix",
    "date_of_birth": "1995-05-25",
    "GPA": "3.0",
    "course": "Computer Science",
    "department": "Engineering",
    "fees_paid": False
}
try :
    student = Student(**wrong_department_student)
except Exception as e:
    print(f"Error: {e}")
    print("-"*20)