import psycopg2
import os


def connect():
    """Connection to database"""

    conn = psycopg2.connect(
        database='d1vcsvncmia2pu',
        user='wwsmvpyvegrmoa',
        password='aee73a8991e50b401fd088a52d2ffd267fc989ab89a1aa19a2e2c91bb67fad4e',
        host="ec2-23-23-80-20.compute-1.amazonaws.com",
        port='5432', sslmode='require')

    # conn = psycopg2.connect(
    #     database='postgres',
    #     user='postgres',
    #     password='spolspol',
    #     host='localhost',
    #     port='5432')
    return conn
