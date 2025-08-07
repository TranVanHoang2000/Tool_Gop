import os
import sys
import subprocess
from pystyle import Colors, Colorate
from rich.console import Console
from rich.panel import Panel
from rich.console import Console
from rich.text import Text
from time import strftime, sleep, time
import requests
import json
from datetime import datetime, timedelta
import base64

def check_internet_connection():
    try:
        response = requests.get("https://www.google.com/", timeout=5)
        return True       
    except requests.ConnectionError:
    	return False
    
if not check_internet_connection():
	print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;32m Phát Hiện Hành Vi Bug Tool, Cảnh Báo !")
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

banner()
info()

print (Colorate.Diagonal(Colors.rainbow, "\n╔═════════════════════╗"))
print (Colorate.Diagonal(Colors.rainbow, "║  Tool Trao Đổi Sub  ║"))
print (Colorate.Diagonal(Colors.rainbow, "╚═════════════════════╝"))
print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m1\033[1;32m]\033[1;36m Tool TĐS TikTok')
print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m2\033[1;32m]\033[1;36m Tool TĐS Instagram')
print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m3\033[1;32m]\033[1;36m Tool TĐS Facebook')
print (Colorate.Diagonal(Colors.rainbow, "╔═════════════════════════╗"))
print (Colorate.Diagonal(Colors.rainbow, "║  Tool Golike            ║"))
print (Colorate.Diagonal(Colors.rainbow, "╚═════════════════════════╝"))
print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m4\033[1;32m]\033[1;36m Tool Golike TikTok')
print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m5\033[1;32m]\033[1;36m Tool Golike Instagram')
print (Colorate.Diagonal(Colors.blue_to_green, "══════════════════════════════════════════════════════════════"))
print (Colorate.Diagonal(Colors.rainbow, "╔════════════════╗"))
print (Colorate.Diagonal(Colors.rainbow, "║  Tool Profile  ║"))
print (Colorate.Diagonal(Colors.rainbow, "╚════════════════╝"))
print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m6\033[1;32m]\033[1;36m Tool Share Ảo Cookies')
print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m7\033[1;32m]\033[1;36m Tool Lấy Token FB')
print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m8\033[1;32m]\033[1;36m Tool Get Id Bài Viết, Id Tài Khoản Facebook')
print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m9\033[1;32m]\033[1;36m Tool Lấy Cookies FB Từ Tài Khoản, Mật Khẩu')
print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m10\033[1;32m]\033[1;36m Tool War Messenger')
print (Colorate.Diagonal(Colors.blue_to_green, "══════════════════════════════════════════════════════════════"))
print (Colorate.Diagonal(Colors.rainbow, "╔════════════════╗"))
print (Colorate.Diagonal(Colors.rainbow, "║  Tool Tiện Ích ║"))
print (Colorate.Diagonal(Colors.rainbow, "╚════════════════╝"))
print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m11\033[1;32m]\033[1;36m Tool Doss Attack Web')
print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m12\033[1;32m]\033[1;36m Tool Lấy Proxy Các Loại')
print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m13\033[1;32m]\033[1;36m Tool Lọc Proxy Live')
print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m14\033[1;32m]\033[1;36m Tool Scan Mail Ảo Lấy Mã')
print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m15\033[1;32m]\033[1;36m Tool Spam Sms')
print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m16\033[1;32m]\033[1;36m Tool Buff View Tiktok (Bản PC)')
print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m17\033[1;32m]\033[1;36m Tool Buff View Tiktok (Bản Adr, Ip)')
print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m18\033[1;32m]\033[1;36m Tool Reg Acc Facebook')
print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m19\033[1;32m]\033[1;36m Tool Spam Discord')
print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m20\033[1;32m]\033[1;36m Tool Spam Telegram')
print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m21\033[1;32m]\033[1;36m Tool Rút Gọn Link4m Từ Token')
print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m22\033[1;32m]\033[1;36m Tool Nuôi Acc Facebook')
print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m23\033[1;32m]\033[1;36m Tool Unfollow TikTok')
print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m24\033[1;32m]\033[1;36m Tool Xword - Vua Thoát Hiểm')
print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m0\033[1;32m]\033[1;36m Thoát Ra')
print (Colorate.Diagonal(Colors.blue_to_green, "══════════════════════════════════════════════════════════════"))

chon = str(input("\033[1;32m[\033[1;31m♤\033[1;32m] \033[1;33m➩ \033[1;32mNhập Số \033[1;31m: \033[1;36m"))

if chon == '1' :
    exec(requests.get('https://raw.githubusercontent.com/TranVanHoang2000/Tool_Gop/main/Choice/1.py').text)
if chon == '2':
    exec(requests.get('https://raw.githubusercontent.com/TranVanHoang2000/Tool_Gop/main/Choice/2.py').text)
if chon == '3' :
    exec(requests.get('https://raw.githubusercontent.com/TranVanHoang2000/Tool_Gop/main/Choice/3.py').text) 
if chon == '4' :
    exec(requests.get('https://raw.githubusercontent.com/TranVanHoang2000/Tool_Gop/main/Choice/4.py').text) 
if chon == '5' : 
   exec(requests.get('https://raw.githubusercontent.com/TranVanHoang2000/Tool_Gop/main/Choice/5.py').text) 
if chon == '6' :
    exec(requests.get('https://raw.githubusercontent.com/TranVanHoang2000/Tool_Gop/main/Choice/6.py').text)
if chon == '7' :
   exec(requests.get('https://raw.githubusercontent.com/TranVanHoang2000/Tool_Gop/main/Choice/7.py').text)
if chon == '8' :
   exec(requests.get('https://raw.githubusercontent.com/TranVanHoang2000/Tool_Gop/main/Choice/8.py').text)
if chon == '9' :
    exec(requests.get('https://raw.githubusercontent.com/TranVanHoang2000/Tool_Gop/main/Choice/9.py').text)
if chon == '10' :
    exec(requests.get('https://raw.githubusercontent.com/TranVanHoang2000/Tool_Gop/main/Choice/10.py').text)
if chon == '11' :
    exec(requests.get('https://raw.githubusercontent.com/TranVanHoang2000/Tool_Gop/main/Choice/11.py').text)
if chon == '12' :
    exec(requests.get('https://raw.githubusercontent.com/TranVanHoang2000/Tool_Gop/main/Choice/12.py').text)
if chon == '13' :
    exec(requests.get('https://raw.githubusercontent.com/TranVanHoang2000/Tool_Gop/main/Choice/13.py').text)
if chon == '14' :
    exec(requests.get('https://raw.githubusercontent.com/TranVanHoang2000/Tool_Gop/main/Choice/14.py').text)
if chon == '15' :
    exec(requests.get('https://raw.githubusercontent.com/TranVanHoang2000/Tool_Gop/main/Choice/15.py').text)
if chon == '16' :
    exec(requests.get('https://raw.githubusercontent.com/TranVanHoang2000/Tool_Gop/main/Choice/16.py').text)
if chon == '17' :
    exec(requests.get('https://raw.githubusercontent.com/TranVanHoang2000/Tool_Gop/main/Choice/17.py').text)
if chon == '18' :
    exec(requests.get('https://raw.githubusercontent.com/TranVanHoang2000/Tool_Gop/main/Choice/18.py').text)
if chon == '19' :
    exec(requests.get('https://raw.githubusercontent.com/TranVanHoang2000/Tool_Gop/main/Choice/19.py').text)
if chon == '20' :
    exec(requests.get('https://raw.githubusercontent.com/TranVanHoang2000/Tool_Gop/main/Choice/20.py').text)
if chon == '21' :
    exec(requests.get('https://raw.githubusercontent.com/TranVanHoang2000/Tool_Gop/main/Choice/21.py').text)
if chon == '22' :
    exec(requests.get('https://raw.githubusercontent.com/TranVanHoang2000/Tool_Gop/main/Choice/22.py').text)
if chon == '23' :
    exec(requests.get('https://raw.githubusercontent.com/TranVanHoang2000/Tool_Gop/main/Choice/23.py').text)
if chon == '24' :
    exec(requests.get('https://raw.githubusercontent.com/TranVanHoang2000/Tool_Gop/main/Choice/24.py').text)
if chon == '0' :
    exec(requests.get('https://raw.githubusercontent.com/TranVanHoang2000/Tool_Gop/main/Choice/0.py').text)
else:
	print("\033[1;32m[\033[1;31m♤\033[1;32m] \033[1;33m➩ \033[1;32mLựa Chọn Sai, Vui Lòng Thử Lại Sau !")	

	sys.exit()
