import pytest
from ..widget.with_sqlite3 import WithSqlite3


@pytest.fixture
def db(tmpdir):
    return WithSqlite3(tmpdir + "/tmp.sqlite3")

@pytest.fixture
def sql_table():
    return " CREATE TABLE IF NOT EXISTS person (name text NOT NULL); "


def test_sqlite3_fetchall(db):
    result = db.fetchall("SELECT 1")
    assert len(result) is 1


def test_sqlite3_create_table(db, sql_table):
    result = db.create_table(sql_table)
    assert result is True


def test_sqlite3_insert(db, sql_table):
    result = db.create_table(sql_table)
    result = db.insert("INSERT into person VALUES(?)", ["bob"])
    assert result == 1
