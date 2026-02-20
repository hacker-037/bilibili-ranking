import sqlite3

DB_NAME = 'bilibili_videos.db'

def get_db_connection():
    """ 获取数据库连接，使用 with 语句确保连接正确关闭 """
    conn = sqlite3.connect(DB_NAME)
    return conn

def create_db():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS videos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                owner TEXT,
                views INTEGER,
                danmaku INTEGER,
                pic_url TEXT,
                record_date TEXT
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"数据库错误: {e}")
    finally:
        conn.close()  # 确保连接关闭

def insert_video(title, owner, views, danmaku, pic_url, record_date):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO videos (title, owner, views, danmaku, pic_url, record_date)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (title, owner, views, danmaku, pic_url, record_date))
        conn.commit()
    except sqlite3.Error as e:
        print(f"数据库插入错误: {e}")
    finally:
        conn.close()  # 确保连接关闭

def get_latest_video():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM videos ORDER BY record_date DESC LIMIT 1')
        video = cursor.fetchone()
        return video
    except sqlite3.Error as e:
        print(f"查询错误: {e}")
        return None
    finally:
        conn.close()

def get_all_videos():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM videos ORDER BY record_date DESC')
        videos = cursor.fetchall()
        return videos
    except sqlite3.Error as e:
        print(f"查询错误: {e}")
        return []
    finally:
        conn.close()
