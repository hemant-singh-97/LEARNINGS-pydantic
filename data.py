from typing import Any, Dict, List
from enum import Enum

class DepartmentEnum(Enum) :
    ARTS_AND_HUMANITIES = "Arts and Humanities"
    SCIENCE_AND_ENGINEERING = "Science and Engineering"
    LIFE_SCIENCES = "Life Sciences"

data1: List[Dict[str, Any]] = [
    {
        "id": "d15782d9-3d8f-4624-a88b-c8e836569df8",
        "name": "Eric Travis",
        "date_of_birth": "1995-05-25",
        "GPA": "3.0",
        "course": "Computer Science",
        "department": "Science and Engineering",
        "fees_paid": False
    },
    {
        "id": "4c7b4c43-c863-4855-abc0-3657c078ce23",
        "name": "Mark Smith",
        "date_of_birth": "1996-02-10",
        "GPA": "2.5",
        "course": None,
        "department": "Science and Engineering",
        "fees_paid": True
    },
    {
        "id": "5cd9ad59-fcf1-462c-8863-282a9fb693e4",
        "name": "Marissa Barker",
        "date_of_birth": "1996-10-01",
        "GPA": "3.5",
        "course": "Biology",
        "department": "Life Sciences",
        "fees_paid": False
    },
    {
        "id": "48dda775-785d-41e3-b0dd-26a4a2f7722f",
        "name": "Justin Holden",
        "date_of_birth": "1994-08-22",
        "GPA": "3.23",
        "course": "Philosophy",
        "department": "Arts and Humanities",
        "fees_paid": True
    },
    {
        "id": "7ffe2ceb-562b-4edd-b74c-3741e1b08453",
        "name": "Michelle Thompson",
        "date_of_birth": "1995-08-05",
        "GPA": "3.9",
        "course": "Film Studies",
        "department": "Arts and Humanities",
        "fees_paid": True
    }
]