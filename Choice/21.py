import requests
import os, sys
from pystyle import Colors, Colorate
from time import sleep

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

def shorten_link():
    token = input("\n\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Token Link4m : \033[1;36m")
    link = input(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Link Cần Rút Gọn : \033[1;36m")
    api_url = f"https://link4m.co/api-shorten/v2?api={token}&url={link}"

    try:
        response = requests.get(api_url)
        data = response.json()

        if data.get('status') == "error":
            print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mLỗi : {data.get('message')}")
        else:
            shortened_link = data.get('shortenedUrl')
            print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mThành Công, Link Đã Rút Gọn Là : \033[1;36m{shortened_link}")
    except Exception as e:
        print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mLỗi Kết Nối Hoặc Định Dạng API : {e}")

if __name__ == "__main__":
    banner()
    info()
    shorten_link()