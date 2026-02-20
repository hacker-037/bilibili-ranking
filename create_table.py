import sqlite3

def create_video_table():
    # 确保使用相同的数据库文件
    conn = sqlite3.connect('bilibili_videos.db')  # 连接数据库
    cursor = conn.cursor()

    # 创建 videos 表的 SQL 语句
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        url TEXT,
        uploader TEXT,
        views INTEGER,
        date TEXT
    );
    ''')

    conn.commit()  # 提交更改
    conn.close()   # 关闭连接

create_video_table()

# 检查表是否存在
def check_table_exists():
    conn = sqlite3.connect('bilibili_videos.db')  # 确保数据库名一致
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    if ('videos',) in tables:
        print("videos 表存在")
    else:
        print("videos 表不存在")
    conn.close()

check_table_exists()