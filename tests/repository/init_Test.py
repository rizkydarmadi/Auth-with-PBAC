from src.repository import Crud
from unittest import IsolatedAsyncioTestCase


class TestRepositoryInit(IsolatedAsyncioTestCase):
    async def test_create(self):
        test_model = Crud(table="users")
        result = test_model.create(
            params={
                "password": "12qwaszx",
                "email": "rizkydarmadi@gmail.com",
                "username": "rizkycc",
            }
        )
        self.assertEqual(None, result)

    async def test_read_all(self):
        test_model = Crud(table="users")
        result = test_model.read_all()
        self.assertEqual(list, type(result))

    async def test_speccific_get(self):
        test_model = Crud(table="users")
        result = test_model.specific_get(pk=1)
        self.assertIsNotNone(result)

    async def test_update(self):
        test_model = Crud(table="users")
        test_model.update(
            pk=1,
            set="""
                password = '34256hj#',
                email='garynavvile@gmail.com',
                username='navvile' """,
        )
