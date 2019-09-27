import sqlite3
from sqlite3 import Error
from .dto import WidgetDto

class WidgetRepo(object):
    sql_create_widget_table = """ CREATE TABLE IF NOT EXISTS widget (
                                        id text PRIMARY KEY,
                                        name text NOT NULL,
                                        weight_kg real NOT NULL
                                    ); """

    def __init__(self, config):
        self._conn = WidgetRepo.create_connection(config["database_uri"])
        WidgetRepo.create_table(self._conn, self.sql_create_widget_table)

    @staticmethod
    def create_connection(db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

        return conn

    @staticmethod
    def create_table(conn, create_table_sql):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print("!!! Could not create table!")
            print(e)


    def get_all(self):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = self._conn.cursor()
        cur.execute("SELECT * FROM widget")

        rows = cur.fetchall()

        for row in rows:
            print(row)
        return rows

    def add_widget(self, dto):
        sql = ''' INSERT INTO widget(id,name,weight_kg)
                  VALUES(?,?,?) '''
        cur = self._conn.cursor()
        cur.execute(sql, dto.values())
        self._conn.commit()
        print(cur.lastrowid)
        return cur.lastrowid
