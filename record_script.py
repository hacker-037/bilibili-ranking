import requests
import json
import os
from datetime import datetime

def record_video():
    url = "https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=all"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        top_video = data["data"]["list"][0]
        
        new_record = {
            "title": top_video["title"],
            "owner": top_video["owner"]["name"],
            "views": top_video["stat"]["view"],
            "danmaku": top_video["stat"]["danmaku"],
            "pic": top_video["pic"],
            "time": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        # 读取并追加数据
        file_path = "data.json"
        history = []
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                history = json.load(f)
        
        history.append(new_record)

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(history, f, ensure_ascii=False, indent=4)
        
        print(f"记录成功: {new_record['title']}")
        
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    record_video()