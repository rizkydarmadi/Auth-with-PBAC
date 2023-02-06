from src.repository import Crud

user = Crud(table="users")

input = {"password": "12qwaszx", "email": "rizkydarmadi@gmail.com", "username": "rizky"}

user.create(params=input)
print(user.read_all())
