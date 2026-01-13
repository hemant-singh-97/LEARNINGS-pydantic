from pydantic import BaseModel, field_validator, Field
from typing import Annotated, Any, Dict, List, Literal
from uuid import UUID
from datetime import date, datetime, timedelta
import json


from data import data2, DepartmentEnum

class Module(BaseModel):
    id: int | UUID
    name: str
    professor: str
    credits: Literal[10, 20] # Only 10 or 20 allowed
    registration_code: str

class Student(BaseModel):
    id: UUID
    name: str
    date_of_birth: date
    GPA: Annotated[float, Field(ge=0.0, le=5.0)]
    course: str | None
    department: DepartmentEnum
    fees_paid: bool
    modules: List[Module] = [] # Default empty list if no modules provided
 
    @field_validator("date_of_birth")
    def ensure_16_or_older(cls, value: date) -> date:
        sixteen_years_ago = datetime.now() - timedelta(days=16*365)
        sixteen_years_ago = sixteen_years_ago.date()
        
        if value > sixteen_years_ago:
            raise ValueError("Student must be at least 16 years old.")
        return value
    
    @field_validator("modules")
    def validate_module_length(cls, value: List[Module]) -> List[Module]:
        if len(value) > 0 and len(value) != 3:
            raise ValueError("Students can only register for exactly 3 modules.")
        return value

for item in data2:
    student = Student(**item)
    print("Object:", student)
    
    for module in student.modules:
        print(module.id)
    
    print("-"*20)

wrong_credits_student : Dict[str, Any] = {
    "id": "7ffe2ceb-562b-4edd-b74c-3741e1b08453",
    "name": "Michelle Thompson",
    "date_of_birth": "1995-08-05",
    "GPA": "3.9",
    "course": "Film Studies",
    "department": "Arts and Humanities",
    "fees_paid": True,
    "modules": [
        {
            "id": 101,
            "name": "Japanese Cinema",
            "professor": "Prof. Travis Hudson",
            "credits": 30,
            "registration_code": "abc"
        },
        {
            "id": 102,
            "name": "South Korean Cinema",
            "professor": "Prof. Todd Black",
            "credits": 20,
            "registration_code": "abc"
        },
        {
            "id": 103,
            "name": "French New Wave Cinema",
            "professor": "Prof. Bailey Stanley",
            "credits": 40,
            "registration_code": "abc"
        }
    ]
}
try :
    student = Student(**wrong_credits_student)
except Exception as e:
    print(f"Error: {e}")
    print("-"*20)


wrong_num_modules_student: Dict[str, Any] = {
    "id": "7ffe2ceb-562b-4edd-b74c-3741e1b08453",
    "name": "Michelle Thompson",
    "date_of_birth": "1995-08-05",
    "GPA": "3.9",
    "course": "Film Studies",
    "department": "Arts and Humanities",
    "fees_paid": True,
    "modules": [
        {
            "id": 101,
            "name": "Japanese Cinema",
            "professor": "Prof. Travis Hudson",
            "credits": 10,
            "registration_code": "abc"
        },
        {
            "id": 102,
            "name": "South Korean Cinema",
            "professor": "Prof. Todd Black",
            "credits": 20,
            "registration_code": "abc"
        },
    ]
}

try :
    student = Student(**wrong_num_modules_student)
except Exception as e:
    print(f"Error: {e}")
    print("-"*20)


print(
    json.dumps(
        Student.model_json_schema(),    # Json Schema, can be used to share pydantic models
        indent = 2
    )  # Json Schema
)
print("-"*20)


# Writing the schema to a file
with open("json_schema.json", "w") as f:
    f.write(
        json.dumps(
            Student.model_json_schema(),
            indent = 2
        )
    )
    
# Run this in terrminal : datamodel-codegen --input json_schema.json --output models_from_schema.py --formatters ruff-format --input-file-type jsonschema
# Above command will generate models_from_schema.py file but won't be able to add custom validators

from models_from_schema import Student as StudentFromSchema
for item in data2:
    student = StudentFromSchema(**item)
    print("Object from Schema:", student)
    print("-"*20)