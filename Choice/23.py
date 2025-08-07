import requests
import json
import time
import os, sys
from time import sleep
from pystyle import Colors, Colorate

os.system("cls" if os.name == "nt" else "clear")

def banner():
    banner = Colorate.Diagonal(Colors.rainbow, """
████████╗██╗   ██╗██╗  ██╗████████╗ ██████╗  ██████╗ ██╗     
╚══██╔══╝██║   ██║██║  ██║╚══██╔══╝██╔═══██╗██╔═══██╗██║     
   ██║   ██║   ██║███████║   ██║   ██║   ██║██║   ██║██║     
   ██║   ╚██╗ ██╔╝██╔══██║   ██║   ██║   ██║██║   ██║██║     
   ██║    ╚████╔╝ ██║  ██║   ██║   ╚██████╔╝╚██████╔╝███████╗
   ╚═╝     ╚═══╝  ╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
""")
    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush()
        sleep(0.000001)

def info():
    info = Colorate.Diagonal(Colors.rainbow, """
\nAdmin Tool : Trần Văn Hoàng            Phiên Bản : 1.0
════════════════════════════════════════════════  
Youtuber : Trần Văn Hoàng
Zalo : 0974698128
════════════════════════════════════════════════  
""")
    for X in info:
        sys.stdout.write(X)
        sys.stdout.flush()
        sleep(0.000001)

def load_cookies_from_string(cookie_str):
    cookies = {}
    for item in cookie_str.split(';'):
        if '=' in item:
            key, value = item.strip().split('=', 1)
            cookies[key] = value
    return cookies

def unfollow_user(user_id, cookies, user_agent):
    csrf_token = cookies.get('tt_csrf_token')
    if not csrf_token:
        print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mKhông Tìm Thấy CSRF Token Trong Cookie")
        return

    headers = {
        'authority': 'www.tiktok.com',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://www.tiktok.com',
        'referer': f'https://www.tiktok.com/@{user_id}',
        'user-agent': user_agent,
        'x-secsdk-csrf-version': '1.2.22',
        'x-secsdk-csrf-request': '1',
        'x-tt-csrftoken': csrf_token
    }

    data = {
        "aid": "1988",
        "user_id": user_id,
        "type": 0
    }

    try:
        response = requests.post(
            'https://www.tiktok.com/api/commit/follow/user/',
            headers=headers,
            cookies=cookies,
            data=json.dumps(data)
        )
        if response.ok:
            print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐã Unfollow User {user_id} - Status : {response.status_code}")
        else:
            print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mLỗi Unfollow : {response.status_code} - {response.text}")
    except Exception as e:
        print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mLỗi Kết Nối : {e}")
        
if __name__ == "__main__":
    banner()
    info()    
    cookie_input = input("\n\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Cookie (Dạng Chuỗi Từ Trình Duyệt) : \033[1;36m")
    cookies = load_cookies_from_string(cookie_input)

    user_id = input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập user_id Muốn Unfollow : \033[1;36m").strip()
    delay = int(input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Delay Giữa Các Request (Giây) : \033[1;36m").strip())
    user_agent = input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập User-Agent (Hoặc Để Trống Để Dùng Mặc Định) : \033[1;36m").strip()

    if not user_agent:
        user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"

    unfollow_user(user_id, cookies, user_agent)
    print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mChờ {delay} Giây Trước Khi Thoát...")
    time.sleep(delay)