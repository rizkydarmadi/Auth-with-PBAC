# from src.repository import Crud

# user = Crud(table="users")

# input = {"password": "12qwaszx", "email": "rizkydarmadi@gmail.com", "username": "rizky"}

# user.create(params=input)
# print(user.read_all())
from src.repository import Crud

test_model = Crud(table="users")
test_model.update(
    pk=1,
    set="""
        password = '34256hj#',
        email='garylineker@gmail.com',
        username='lineker' """,
)

print(test_model.read_all())
