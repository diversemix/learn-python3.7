import sqlite3
from typing import List
from sqlite3 import Error


class WithSqlite3(object):

    def __init__(self, filename: str):
        self._conn = WithSqlite3.create_connection(filename)

    @staticmethod
    def create_connection(db_file: str):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

        return conn

    def create_table(self, create_table_sql: str):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        result = None
        try:
            c = self._conn.cursor()
            result = c.execute(create_table_sql)
        except Error as e:
            print("!!! Could not create table!")
            print(e)
            return False
        return True

    def fetchall(self, sql: str) -> List:
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = self._conn.cursor()
        cur.execute(sql)

        return cur.fetchall()

    def insert(self, sql: str, values: List[str]) -> int:
        cur = self._conn.cursor()
        cur.execute(sql, values)
        self._conn.commit()
        return cur.lastrowid
