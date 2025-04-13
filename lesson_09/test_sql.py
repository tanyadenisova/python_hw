import pytest
from sqlalchemy import create_engine, inspect
from sqlalchemy.sql import text


db_connection_string = "postgresql://postgres:1234567890@localhost:5432/postgres"
db = create_engine(db_connection_string)

def test_db_connection():
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names[0] == 'users'

def test_create_employee():
    connection = db.connect()
    transaсtion = connection.begin()
    sql = text('INSERT INTO users (user_id, user_email, subject_id) VALUES(:user_id, :user_email, :subject_id)')
    connection.execute(sql, {'user_id': 66060, 'user_email': 'pypypy@mail.ru', 'subject_id': 3})
    transaсtion.commit()
    check_sql = text('SELECT * FROM users WHERE user_id = :user_id')
    result = connection.execute(check_sql, {'user_id': 66060}).fetchone()
    assert result is not None
    connection.close()

def test_update_employee():
    connection = db.connect()
    transaсtion = connection.begin()
    sql = text('UPDATE users SET user_email = :user_email WHERE user_id = :user_id')
    connection.execute(sql, {'user_email': 'lalala@mail.ru', 'user_id': 66060})
    transaсtion.commit()
    check_sql = text('SELECT * FROM users WHERE user_email = :user_email')
    result = connection.execute(check_sql, {'user_email': 'lalala@mail.ru'}).fetchone()
    assert result is not None
    connection.close()

def test_delete_employee():
    connection = db.connect()
    transaсtion = connection.begin()
    sql = text('DELETE FROM users WHERE user_id = :user_id')
    connection.execute(sql, {'user_id': 66060})
    transaсtion.commit()
    check_sql = text('SELECT * FROM users WHERE user_id = :user_id')
    result = connection.execute(check_sql, {'user_id': 66060}).fetchone()
    assert result is None
    connection.close()
