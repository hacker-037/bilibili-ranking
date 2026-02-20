# check_table.py
import sqlite3

def check_table_exists():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    if ('videos',) in tables:
        print("videos 表存在")
    else:
        print("videos 表不存在")
    
    conn.close()

check_table_exists()