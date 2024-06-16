import requests
import json
import time

def app(live_id):
    url = f"https://www.mirrativ.com/api/live/online_users?live_id={live_id}&page=1"
    headers = {
        'User-Agent': 'MR_APP/10.45.3/Android/PIXEL 8/12',
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        users = data.get('users', [])
        user_info = [{'name': user.get('name', '').encode().decode('utf-8', 'ignore'), 'user_id': user.get('user_id', '')} for user in users]
        
        # Get current time in hours, minutes, and seconds
        current_time = time.localtime()
        hour = current_time.tm_hour
        minute = current_time.tm_min
        second = current_time.tm_sec

        print(f"[!]{hour}時{minute}分{second}秒: {len(user_info)}人のユーザーがオンラインです。")
        for user in user_info:
            print(f"ユーザー名: {user['name']}, ユーザーID: {user['user_id']}")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

live_id = input("LiveId: ")

for i in range(100):
    app(live_id)
    time.sleep(60)