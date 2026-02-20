from flask import Flask, render_template
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import requests
import database

app = Flask(__name__)

# 每天12点整获取数据并记录
def record_video():
    url = "https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=all"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    top_video = data["data"]["list"][0]
    
    title = top_video["title"]
    owner = top_video["owner"]["name"]
    views = top_video["stat"]["view"]
    danmaku = top_video["stat"]["danmaku"]
    pic_url = top_video["pic"]
    record_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # 将数据插入数据库
    database.insert_video(title, owner, views, danmaku, pic_url, record_date)

@app.route('/')
def index():
    # 获取最新的记录
    video = database.get_latest_video()
    return render_template('index.html', video=video)

if __name__ == '__main__':
    # 初始化数据库
    database.create_db()

    # 手动触发一次数据记录
    record_video()

    # 设置定时任务，立即开始，每24小时执行一次
    scheduler = BackgroundScheduler()
    scheduler.add_job(record_video, 'interval', hours=24, start_date='2026-02-21 12:00:00', timezone='Asia/Shanghai')
    scheduler.start()

    # 启动Flask应用
    app.run(debug=True, port=5000)
else:
    # 当被 Vercel 等服务器调用时，跳过那些会报错的写操作
    # 这样 Vercel 启动时就不会因为无法创建数据库而崩溃
    pass
