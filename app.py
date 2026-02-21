from flask import Flask, render_template
import json
import os

app = Flask(__name__)

# 读取 JSON 数据的辅助函数
def get_data():
    file_path = "data.json"
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

@app.route('/')
def index():
    videos = get_data()
    # 取最后一条记录（最新的）展示在首页
    latest_video = videos[-1] if videos else None
    return render_template('index.html', video=latest_video)

@app.route('/history')
def history():
    videos = get_data()
    # 倒序排列，最新的排在最前面
    return render_template('history.html', videos=reversed(videos))

# Vercel 不需要 app.run，直接暴露 app 对象即可

# ... 你之前的爬虫和路由代码 ...
if __name__ == '__main__':
    # 这里的 debug=True 非常重要，它会告诉你哪里报错了
    app.run(debug=True, port=5000)