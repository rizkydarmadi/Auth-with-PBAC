from db import engine
from sqlalchemy import text


class Crud:
    def __init__(self, table: str) -> None:
        self.table = table

    @staticmethod
    def __commit(stmt: str) -> None:
        conn = engine.connect()
        conn.execute(text(stmt))
        conn.commit()

    @staticmethod
    def __fetchall(stmt: str):
        conn = engine.connect()
        return conn.execute(text(stmt)).fetchall()

    @staticmethod
    def __fetchone(stmt: str):
        conn = engine.connect()
        return conn.execute(text(stmt)).fetchone()

    @staticmethod
    def __key_val(text: dict):
        columns = [column for column in text.keys()]
        values = [value for value in text.values()]

        return tuple(columns), tuple(values)

    def create(self, params: dict) -> None:
        columns, values = Crud.__key_val(text=params)
        stmt = f"INSERT INTO {self.table} {columns}"
        _stmt = stmt.replace("'", "")
        _stmt += f" VALUES {values};"

        Crud.__commit(stmt=_stmt)

    def read_all(self, condition: str = None):
        if condition is None:
            stmt = f"SELECT * FROM {self.table};"
        else:
            stmt = f"SELECT * FROM {self.table} {condition};"
        result = Crud.__fetchall(stmt=stmt)
        return result

    def read_all_w_page(self, limit: int, page_number: int, condition: str = None):
        if condition is None:
            stmt = f"""SELECT * FROM {self.table}
                    LIMIT {limit} OFFSET {page_number * limit}
                    ;"""
        else:
            stmt = f"""SELECT * FROM {self.table}
                    {condition}
                    LIMIT {limit} OFFSET {page_number * limit}
                    ;"""

        result = Crud.__fetchall(stmt=stmt)
        return result

    def specific_get(self, pk: int, condition: str = None):
        if condition is None:
            stmt = f"SELECT * FROM {self.table} WHERE id = {pk};"
        else:
            stmt = f"SELECT * FROM {self.table} WHERE id = {pk} {condition};"

        result = Crud.__fetchone(stmt=stmt)
        return result

    def update(self, pk: int, set: str):
        stmt = f"""UPDATE {self.table} SET {set} WHERE id = {pk};"""
        Crud.__commit(stmt=stmt)

    def delete(self, pk: int, set: str):
        stmt = f"""DELETE {self.table}
                    WHERE id = {pk};"""
        Crud.__commit(stmt=stmt)

    def custom_query(self, query: str, execute: str):
        if execute == "many":
            result = Crud.__fetchall(stmt=query)
        elif execute == "one":
            result = Crud.__fetchone(stmt=query)
        elif execute == "hit":
            result = Crud.__commit(stmt=query)
        return result
