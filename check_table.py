# check_table.py
import sqlite3

def check_table_exists():
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        # 查询所有表的名字
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        # 判断是否存在 'videos' 表
        if ('videos',) in tables:
            print("videos 表存在")
            return True
        else:
            print("videos 表不存在")
            return False
    except sqlite3.Error as e:
        print(f"数据库连接失败或查询失败: {e}")
        return False
    finally:
        conn.close()

# 调用函数检查表是否存在
check_table_exists()