from pydantic import BaseModel
# from dataclasses import dataclass
#
#
# @dataclass
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int


data = {"first_name": "test", "last_name": "test", "age": 32}
person = Person(**data)
print(person)