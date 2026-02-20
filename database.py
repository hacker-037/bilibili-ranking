import sqlite3

def create_db():
    conn = sqlite3.connect('bilibili_videos.db')
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
    conn.close()

def insert_video(title, owner, views, danmaku, pic_url, record_date):
    conn = sqlite3.connect('bilibili_videos.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO videos (title, owner, views, danmaku, pic_url, record_date)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (title, owner, views, danmaku, pic_url, record_date))
    conn.commit()
    conn.close()

def get_latest_video():
    conn = sqlite3.connect('bilibili_videos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM videos ORDER BY record_date DESC LIMIT 1')
    video = cursor.fetchone()
    conn.close()
    return video

def get_all_videos():
    conn = sqlite3.connect('bilibili_videos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM videos ORDER BY record_date DESC')
    videos = cursor.fetchall()
    conn.close()
    return videos