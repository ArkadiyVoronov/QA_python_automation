# from numpy.random import default_rng
import time

# from asyncio import sleep
import datetime
import random
import numpy as np
import boto3
# import tensorflow as tf
# import aiopg

import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()


def create_table():
    """Создаёт бд"""
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")


create_table()


def dynamic_data_entry():
    from time import sleep

    unix = int(time.time())
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0, 100)

    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
              (unix, date, keyword, value))

    conn.commit()
    sleep(1)


def read_from_db():
    """Чтение из бд."""

    c.execute('SELECT * FROM stuffToPlot')
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)

    c.execute('SELECT * FROM stuffToPlot WHERE value = 3')
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)

    c.execute('SELECT * FROM stuffToPlot WHERE unix > 1452554972')
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)

    c.execute('SELECT value, datestamp FROM stuffToPlot WHERE unix > 1452554972')
    data = c.fetchall()
    print(data)
    for row in data:
        print(row[0])


from numpy.random import default_rng

rg = default_rng(12345)

for i in range(int(rg.random() * 100)):
    dynamic_data_entry()
dir(boto3)


def graph_data():
    """Рисует данные из таблицы."""
    c.execute('SELECT datestamp, value FROM stuffToPlot')
    data = c.fetchall()

    dates = []
    values = []

    for row in data:
        dates.append(parser.parse(row[0]))
        values.append(row[1])

    plt.plot_date(dates, values, '-')
    plt.show()


def graph_data_new():
    # Connect to database
    now = datetime.now()
    sqlite_file = '/home/pi/scripts/database/climate.db'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    style.use('fivethirtyeight')

    c.execute('SELECT temperature, humidity, feelslike, timenow FROM external')
    data = c.fetchall()

    temperature = []
    humidity = []
    feelslike = []
    timenow = []

    for row in data:
        timenow.append(parser.parse(row[0]))
        values.append(row[1])

    plt.plot_date(temperature, humidity, feelslike, '-')
    plt.savefig('/home/pi/scripts/database/foo.png')
    c.close()
    conn.close()


import matplotlib.pyplot as plt
# import matplotlib.dates as mdates
from dateutil import parser
from matplotlib import style

style.use('fivethirtyeight')

read_from_db()
graph_data()
c.close
conn.close()