import sqlite3
import os

# 创建视频表
def create_video_table(db_name='bilibili_videos.db'):
    # 确保使用相对路径，避免路径问题
    db_path = os.path.join(os.getcwd(), db_name)
    
    conn = sqlite3.connect(db_path)  # 连接数据库
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

    print(f"视频表已经创建（如果没有的话）。数据库文件：{db_path}")


# 检查表是否存在
def check_table_exists(db_name='bilibili_videos.db'):
    db_path = os.path.join(os.getcwd(), db_name)
    
    conn = sqlite3.connect(db_path)  # 确保数据库名一致
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    if ('videos',) in tables:
        print("videos 表存在")
    else:
        print("videos 表不存在")
    
    conn.close()


if __name__ == "__main__":
    create_video_table()  # 创建表
    check_table_exists()  # 检查表是否存在