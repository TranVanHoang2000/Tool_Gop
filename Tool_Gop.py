import threading
import base64
import os
import time
import re
import json
import random
import requests
import socket
import sys
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

try:
    from faker import Faker
    from requests import session
    from colorama import Fore, Style
    from pystyle import Colors, Colorate
    import pystyle

except ImportError:
	print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;32m Bạn Chưa Setup, Đang Chuẩn Bị Setup...")
	
	os.system("pip install faker requests colorama bs4 pystyle")
	os.system("pip3 install requests pysocks && pip install pystyle")
	print('\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;32m Đang Thoát Tool Để Reset...')
	sys.exit()

secret_key = base64.urlsafe_b64encode(os.urandom(32))

def encrypt_data(data):
    return base64.b64encode(data.encode()).decode()

def decrypt_data(encrypted_data):
    return base64.b64decode(encrypted_data.encode()).decode()

def check_internet_connection():
    try:
        response = requests.get("https://www.google.com/", timeout=5)
        return True       
    except requests.ConnectionError:
    	return False
    
if not check_internet_connection():
	print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;31m Phát Hiện Hành Vi Bug Tool, Cảnh Báo !")
	sys.exit(1)

def loading(seconds):
    print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;31m Đang Loading", end="", flush=True)
    for _ in range(seconds):
        sleep(1)
        print(".", end="", flush=True)
    print("\n\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;32m Đã Loading Thành Công !")

loading(5)
sleep(1.5)

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

def get_ip_address():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip_data = response.json()
        ip_address = ip_data['ip']
        return ip_address
    except Exception as e:
        print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mLỗi Khi Lấy Địa Chỉ IP Của Bạn : {e}")
        sys.exit()
        return None

def display_ip_address(ip_address):
    if ip_address:
        banner()
        info()
        print(f"\n\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐịa Chỉ IP Của Bạn \033[1;31m: \033[1;36m{ip_address}")
    else:
        print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mKhông Thể Lấy Địa Chỉ IP Của Thiết Bị !")
        sys.exit()
        
def save_info_ip(ip, key, expiration_date):
    data = {ip: {'key': key, 'expiration_date': expiration_date.isoformat()}}
    encrypted_data = encrypt_data(json.dumps(data))

    with open('ip_address.json', 'w') as file:
        file.write(encrypted_data)

def info_ip():
    try:
        with open('ip_address.json', 'r') as file:
            encrypted_data = file.read()
        data = json.loads(decrypt_data(encrypted_data))
        return data
    except FileNotFoundError:
        return None

def kiem_tra_ip(ip):
    data = info_ip()
    if data and ip in data:
        expiration_date = datetime.fromisoformat(data[ip]['expiration_date'])
        if expiration_date > datetime.now():
            return data[ip]['key']
    return None

def random_key(length=13):
    charset = 'QWERTYUIOPASDFGHJKLZXCVBNM0123456789'
    return ''.join(random.choice(charset) for _ in range(length))

def generate_key_and_url(ip_address):
    key = f'KeyTVH_{random_key()}'
    expiration_date = datetime.now().replace(hour=23, minute=59, second=0, microsecond=0)
    url = f'http://getkeytool.x10.mx/?key={key}'
    return url, key, expiration_date

def da_qua_gio_moi():
    now = datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
    return now >= midnight

def get_shortened_link_phu(url):
    try:
        token = "670205eb527ba0153204a388"
        api_url = f"https://link4m.co/api-shorten/v2?api={token}&url={url}"
        response = requests.get(api_url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return {"status": "error", "message": "\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mKhông Thể Kết Nối Đến Dịch Vụ Rút Gọn URL !"}
            sys.exit()
    except Exception as e:
        return {"status": "error", "message": f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mLỗi Khi Rút Gọn URL : {e}"}
        sys.exit()

def kiem_tra_bao_tri():
    try:
        url = "https://raw.githubusercontent.com/TranVanHoang2000/Tool/main/Tool_Status.json"
        response = requests.get(url, timeout=5)
        data = response.json()

        if data.get("Status", "false").strip().lower() == "true":
            print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mTool Đang Trong Thời Gian Bảo Trì, Vui Lòng Quay Lại Sau !")
            sys.exit()
    except Exception as e:
        print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mKhông Thể Kiểm Tra Trạng Thái Bảo Trì, Vui Lòng Thử Lại Sau !")
        sys.exit()

def main():
    ip_address = get_ip_address()
    display_ip_address(ip_address)
    kiem_tra_bao_tri()

    if ip_address:
        existing_key = kiem_tra_ip(ip_address)
        if existing_key:
            print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mKey Còn Hạn, Đang Chuyển Hướng Đến Tool...")
            time.sleep(2)
        else:
            if da_qua_gio_moi():
                print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mKey Đã Hết Hạn, Đang Thoát...")
                return

            url, key, expiration_date = generate_key_and_url(ip_address)

            with ThreadPoolExecutor(max_workers=2) as executor:
                print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;31m[\033[1;32m1\033[1;31m] \033[1;32mĐể Lấy Key \033[97m( Free )")

                while True:
                    try:
                        choice = input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;31m: \033[1;36m")
                        print(Colorate.Diagonal(Colors.rainbow, "════════════════════════════════════════════════"))
                        if choice == "1":
                            link4m_future = executor.submit(get_shortened_link_phu, url)
                            link4m_data = link4m_future.result()
                            if link4m_data and link4m_data.get('status') == "error":
                                print(link4m_data.get('message'))
                                return
                            else:
                                link_key_link4m = link4m_data.get('shortenedUrl')
                                print('\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mLink Rút Gọn Để Lấy Key \033[1;31m:\033[1;36m', link_key_link4m)

                            while True:
                                keynhap = input('\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mKey Bạn Đã Vượt Là \033[1;31m: \033[1;36m')
                                if keynhap == key:
                                    print('\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mKey Đúng, Đang Chuyển Hướng...')
                                    sleep(2)
                                    save_info_ip(ip_address, keynhap, expiration_date)
                                    return
                                else:
                                    print('\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mKey Sai, Link Vượt Của Bạn \033[1;31m:\n •\033[1;36m', link_key_link4m)
                    except ValueError:
                        print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mVui Lòng Nhập Lựa Chọn Hợp Lệ !")
                    except KeyboardInterrupt:
                        print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mCảm Ơn Bạn Đã Tin Tưởng Và Sử Dụng Tool, Chúc Bạn May Mắn !")
                        sys.exit()
    
if __name__ == '__main__':
    main()
    while True:
        try:
            exec(requests.get('https://raw.githubusercontent.com/TranVanHoang2000/Tool_Gop/main/Tool_Gop.py').text)
        except KeyboardInterrupt:
            print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mCảm Ơn Bạn Đã Tin Tưởng Và Sử Dụng Tool, Chúc Bạn May Mắn !")
            sys.exit()