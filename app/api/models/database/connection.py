import psycopg2
import os


def connect():
    """Connection to database"""

    conn = psycopg2.connect(
        database='postgres',
        user='postgres',
        password='spolspol',
        host='localhost',
        port='5432')
    return conn
