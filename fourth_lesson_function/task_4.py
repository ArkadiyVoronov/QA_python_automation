import sqlite3

conn = sqlite3.connect('task.db')

def create_table():
    """Функция которая создает таблицу."""
    c = conn.cursor()
    sql = """CREATE TABLE if not exists "Expenses"\
    ( "id" BIGSERIAL UNIQUE PRIMARY KEY NOT NULL,\
    "date" date NOT NULL,"name" varchar(25) NOT NULL,\
    "money" double NOT NULL);"""
    c.execute(sql)

def read_table(date_inc: str):
    """Функция которая создает таблицу."""
    c = conn.cursor()

    sql = """SELECT * FROM Expenses WHERE date = {date_inc;"""
    c.execute(sql)
    c.fetchall()

date_inc = '2022-01-01'

def insert_one(): """Функция которая создает таблицу."""
    c = conn.cursor()
    sql = """INSERT INTO Expenses (id, date, name, money)\
    VALUES (1, "2022-01-01", "phone", 10000);"""
    c.execute(sql)
    conn.commit()

create_table()
# insert_one()
read_table(date_inc)
conn.close()