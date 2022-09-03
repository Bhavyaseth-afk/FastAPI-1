from typing import Optional,List
from uuid import UUID, uuid4
from pydantic import BaseModel
from typing import Optional
from enum import Enum

class Gender(str, Enum):
    male="male"
    female = "female"

class Roles(str, Enum):
    admin="admin"
    user = "user"
    student = "student"


class User(BaseModel):
    id : Optional[int]
    first_name : str
    last_name : str
    mid_name : Optional[str]
    gender : Gender
    roles : List[Roles]
