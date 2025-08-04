import requests
from concurrent.futures import ThreadPoolExecutor
from pystyle import Colors, Colorate
import os
import sys
import time
from time import sleep
import pystyle
import random
import time

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
\n➢ Admin : Trần Văn Hoàng            ➢ Phiên Bản : 1.0
════════════════════════════════════════════════  
➢ Youtuber : https://www.youtube.com/@TranVanHoang2000
➢ Nhóm Zalo Có Bot : https://zalo.me/g/lzousq414
════════════════════════════════════════════════  
""")
    for X in info:
        sys.stdout.write(X)
        sys.stdout.flush()
        sleep(0.000001)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

sleep(3)
clear()
banner()
info()
sleep(3)
proxy_list = input("\n\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mVui Lòng Nhập File Chứa Proxy : \033[1;36m")
with open(proxy_list, 'r') as file:
    proxy_list = file.read().split("\n")
    proxy_count = len(proxy_list)
luu = input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mVui Lòng Nhập Tệp Để Lưu Proxy Live : \033[1;36m")
print(f" \033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mFound : {proxy_count} Proxy In Your Proxy File")
sleep(2)
print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mPlease Wait For A Sec")
sleep(3)
print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mStart Running The Tool Please Don't Press Anything")
print (Colorate.Diagonal(Colors.blue_to_green, "══════════════════════════════════════════════════════════════"))
sleep(3)
list = []
for p in proxy_list:
    prx = p.strip("\n")
    list.append(prx)


def check_proxy(proxy):
    proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
    }
    
    try:
        response = requests.get('http://httpbin.org/ip', proxies=proxies, timeout=20)
        if response.status_code == 200 or response.status_code == 202 or response.status_code == 504 or response.status_code == 503 or response.status_code == 502 or response.status_code == 500:
            detect_location(proxy)
            open(luu,'a').write(proxy+'\n')
            return True
    except requests.exceptions.RequestException:
        pass

    print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32m{proxy} • Unknown/Unknown • BAD")
    return False


def detect_location(proxy):
    ip_address = proxy.split(':')[0]
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data["status"] == "success":
            print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32m{proxy} • {data['country']}/{data['city']} • Live")
            open(luu,'a').write(proxy+'\n')
        else:
            print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mFailed To Detect Location For Proxy.")


def process_proxy(proxy):
    if check_proxy(proxy):
        pass


num_workers = 200

with ThreadPoolExecutor(max_workers=num_workers) as executor:
    executor.map(process_proxy, proxy_list)

print(
    f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mScanning Proxies Successfully, Currently On The Proxy List {luu} Is Having %s Proxies-Live"
    % (len(open(f"{luu}").readlines()))
)
print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mThanks For Using My Tool !")
logout = input("Press Enter To Exit !")
exit()