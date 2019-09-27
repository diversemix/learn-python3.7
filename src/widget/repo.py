from typing import List
from .dto import WidgetDto
from .with_sqlite3 import WithSqlite3


class WidgetRepo(object):
    sql_create_widget_table = """ CREATE TABLE IF NOT EXISTS widget (
                                        id text PRIMARY KEY,
                                        name text NOT NULL,
                                        weight_kg real NOT NULL
                                    ); """

    def __init__(self, config):
        self._conn = WithSqlite3(config["database_uri"])
        self._conn.create_table(self.sql_create_widget_table)

    def get_all_widgets(self) -> List[WidgetDto]:
        return self._conn.fetchall("SELECT * FROM widget")

    def add_widget(self, dto) -> int:
        sql = ''' INSERT INTO widget(id,name,weight_kg)
                  VALUES(?,?,?) '''
        return self._conn.insert(sql, dto.values())
