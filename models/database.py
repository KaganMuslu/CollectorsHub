from models.model import Gender, User
from typing import List


db: List[User] = [
    User(id=0, username="DualPatroll", password="asdqwe", gender=Gender.female),
    User(id=1, username="NinjaSaizo", password="jutsu21", gender=Gender.male)
]