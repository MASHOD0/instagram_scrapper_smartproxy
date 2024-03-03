import mysql.connector
from .cred import user, password # import credentials
DATABASE = 'telaverge'
USER = user
PASSWORD = password
HOST = 'localhost'

def connect():
    try:
        conn = mysql.connector.connect(
            host=HOST,
            user=USER,
            passwd=PASSWORD,
            database=DATABASE
        )
        print('Opened DB succesfully')
        return conn
    except Exception as e:
        print(e)
        
def cursor(conn):
    try:
        cur = conn.cursor()
        print('cursor generated')
        return cur
    except Exception as e:
        print(e)
        
def commit(conn):
    try:
        conn.commit()
        print('query commited')
    except Exception as e:
        print(e)
        
def execute(conn, query):
    try:
        cur = cursor(conn)
        cur.execute(query)
        print("Query Executed.")
        commit(conn)
    except Exception as e:
        print(e)

def fetch(conn, query):
    try:

        cur = cursor(conn)
        cur.execute(query)
        rows = cur.fetchall()
        print('query fetched')
        return rows
        
    except Exception as e:
        print(e)

def close(conn):
    try:
        conn.close()
        print('connection closed')
    except Exception as e:
        print(e)
        

