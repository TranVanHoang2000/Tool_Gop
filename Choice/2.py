from weakref import proxy
import requests
from time import sleep
from pystyle import *
import os, sys
from datetime import date, datetime
import random

tmp1 = open('ua.txt','a+')
tmp1.close()
file1=open('ua.txt')
read_ua=file1.readlines()
list_acc = []
from datetime import date
today = date.today()
import requests, random
rds=random.randint(1,999)
ngay=today.day

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
    
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
silent_mode = True

def load_token():
    try:
        with open("Config_TĐS.txt", "r") as f:
            token = f.readline().strip()
            if token:
                return token
    except:
        return None
    return None

def save_token(token):
    with open("Config_TĐS.txt", "w") as f:
        f.write(token.strip())

os.system('cls' if os.name == 'nt' else 'clear')
banner()
info()

def safe_get_json(url):
    try:
        res = requests.get(url)
        if res.status_code == 200 and res.text.strip():
            return res.json()
        else:
            if not silent_mode:
                print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mLỗi Khi Lấy Dữ Liệu Từ : {url}")
                print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mStatus Code : {res.status_code}, Nội Dung : {res.text[:100]}")
            return {}
    except requests.exceptions.JSONDecodeError:
        if not silent_mode:
            print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mJSONDecodeError : Dữ Liệu Không Hợp Lệ Từ {url}")
    except Exception as e:
        if not silent_mode:
            print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mLỗi Khi Kết Nối Tới {url}, Lỗi : {e}")
    return {}

while True:
    tokenn = load_token()
    if tokenn:
        print(f'\n\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m1\033[1;32m]\033[1;36m Giữ Lại Tài Khoản TĐS Đã Lưu')
        print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m2\033[1;32m]\033[1;36m Nhập Access_Token TDS Mới')
        opt = input(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số  : \033[1;36m')
        if opt == '2':
            tokenn = input(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Token TĐS Mới : \033[1;36m')
            save_token(tokenn)
    else:
        tokenn = input(f'\n\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32m Nhập Token TĐS : \033[1;36m')
        save_token(tokenn)

    login = safe_get_json(f'https://traodoisub.com/api/?fields=profile&access_token={tokenn}')
    if 'success' in login:
        name = login['data']['user']
        xu = login['data']['xu']
        print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐăng Nhập Thành Công !')
        break
    else:
        print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mToken TĐS Sai, Hãy Nhập Lại !')
        sleep(1)

print(f'\n\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m1\033[1;32m]\033[1;36m Nhập Cookie Thủ Công')
print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m2\033[1;32m]\033[1;36m Nhập Cookie Đọc File.txt  ')
a=input(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số : \033]1;36m')

if(a=='1'):
    i=1
    cookieig=input(f'\n\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Cookie Thứ {i} : \033]1;36m')
    list_acc.append(cookieig)
    while len(cookieig)>1:
        i=i+1
        cookieig=input(f'\n\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Cookie Thứ {i} : \033]1;36m')
        list_acc.append(cookieig)
        break
if(a=='2'):
    file = input(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Tên File Cần Đọc Cookie (Mỗi Cookie 1 Dòng) : \033]1;36m')
    file =  open(f'{file}')
    read_ck = file.readlines()
    for ck in read_ck:
        cookieig = ck.split('\n')[0]
        list_acc.append(cookieig)
clear_terminal()
checkfl=input(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mCó Làm Nhiệm Vụ Follow Không (Nhập On/Off) : \033]1;36m')
if(checkfl=='on'):
    sofl=input(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số Follow/ 1 Acc : \033]1;36m')
    sofl=int(sofl)
    delayfl=input(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Delay Follow : \033]1;36m')
checklike=input(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mCó Làm Nhiệm Vụ Like Không (Nhập On/Off) : \033]1;36m')
if(checklike=='on'):
    solike=input(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số Like/1 Acc : \033]1;36m')
    solike=int(solike)
    delaylike=input(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Delay Like : \033]1;36m')
chuyenacc=input(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Thời Gian Chuyển Acc : \033]1;36m')
chuyenacc=int(chuyenacc)
clear_terminal()
ghj=input(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mCó Sử Dụng Proxy Không (Nhập On/Off) : \033]1;36m')
list_proxie=[]
if ghj=='on':
    print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mFile Proxy Sẽ Có Định Dạng [Tên Proxy].txt')
    print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mHOST:PORT Hoặc USER:PASS@HOST:PORT')
    tenproxy= input(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Tên File Chứa Proxy (Mỗi Proxy Cho 1 Đồng Sẽ Tự Random 1 Proxy/ 1 Acc) : \033]1;36m')
    tmp3=open(f'{tenproxy}', 'a+')
    tmp3.close()
    file2 =  open(f'{tenproxy}')
    read_proxy = file2.readlines()
    for pro in read_proxy:
        proxii = pro.split('\n')[0]
        list_proxie.append(proxii)
clear_terminal()
print (Colorate.Diagonal(Colors.blue_to_green, "══════════════════════════════════════════════════════════════"))
print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mUsername : {name}') 
print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mAccountnumber : {len(list_acc)}')
print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mCoin : {xu}')
print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mVersion : {Red}1.0')
print (Colorate.Diagonal(Colors.blue_to_green, "══════════════════════════════════════════════════════════════"))
sleep(0.5)

def apifl1(cookies,idfl,uafake,proxie):
    proxies= {
        'http': f'http://{proxie}',
        'https': f'http://{proxie}',
    }
    token=cookies.split('csrftoken=')[1].split(';')[0]
    headers = {
        'authority': 'i.instagram.com',
        'accept': '*/*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': cookies,
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': uafake,
        'x-asbd-id': '198387',
        'x-csrftoken': token,
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR1UYU8O8XCMl4jZdv4YxiRUxEIymCA_4stpgFmc092K1Kb2',
        'x-instagram-ajax': '1006309104',
    }
    while True:
        try:
            responsefl = requests.post(f'https://i.instagram.com/api/v1/web/friendships/{idfl}/follow/', headers=headers, proxies=proxies, timeout=10).json()
            check = responsefl['status']
            if(check == 'ok'):
                print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mThành Công !')
                fl1=1
            else :
                print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mKhông Thành Công !')
                fl1=0
            return fl1
            break
        except:
            print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐã Xảy Ra Lỗi Gì Đó, Vui Lòng Chờ 5 Giây...', end='\r')
            sleep(5)
            print('                                              ', end='\r')

def apifl2(cookies,idfl,uafake):
    token=cookies.split('csrftoken=')[1].split(';')[0]
    headers = {
        'authority': 'i.instagram.com',
        'accept': '*/*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': cookies,
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': uafake,
        'x-asbd-id': '198387',
        'x-csrftoken': token,
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR1UYU8O8XCMl4jZdv4YxiRUxEIymCA_4stpgFmc092K1Kb2',
        'x-instagram-ajax': '1006309104',
    }
    while True:
        try:
            responsefl = requests.post(f'https://i.instagram.com/api/v1/web/friendships/{idfl}/follow/', headers=headers, timeout=10).json()
            check = responsefl['status']
            if(check == 'ok'):
                print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mThành Công !')
                fl1=1
            else :
                print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mKhông Thành Công !')
                fl1=0
            return fl1
            break
        except:
            print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐã Xảy Ra Lỗi Gì Đó, Vui Lòng Chờ 5 Giây...', end='\r')
            sleep(5)
            print('                                              ', end='\r')
def apilike1(cookies,idlike,uafake,link,proxie):
    proxies= {
        'http': f'http://{proxie}',
        'https': f'http://{proxie}',
    }
    if(idlike=='false'):
        pass
    else:
        token=cookies.split('csrftoken=')[1].split(';')[0]
        headers = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': cookies,
            'origin': 'https://www.instagram.com',
            'referer': link,
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': uafake,
            'x-asbd-id': '198387',
            'x-csrftoken': token,
        }
        e=0
        while True:
            try:
                responselike = requests.post(f'https://www.instagram.com/web/likes/{idlike}/like/',headers=headers,proxies=proxies)
                r1=responselike.text
                if(r1=='Sorry, this photo has been deleted'):
                    print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mPhoto Has Been Delete !')
                    pass
                else:
                    check=r1.split('status":"')[1].split('"')[0]
                    if(check== 'ok'):
                        print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mThành Công !')
                    else :
                        print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mKhông Thành Công !')
                break
            except:
                print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐã Xảy Ra Lỗi Gì Đó, Vui Lòng Chờ 5 Giây...', end='\r')
                sleep(5)
                print('                                              ', end='\r')
                e=e+1
                if(e==3):
                    break
def apilike2(cookies,idlike,uafake,link):
    if(idlike=='false'):
        pass
    else:
        token=cookies.split('csrftoken=')[1].split(';')[0]
        headers = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': cookies,
            'origin': 'https://www.instagram.com',
            'referer': link,
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': uafake,
            'x-asbd-id': '198387',
            'x-csrftoken': token,
        }
        e=0
        while True:
            try:
                responselike = requests.post(f'https://www.instagram.com/web/likes/{idlike}/like/',headers=headers)
                r1=responselike.text
                if(r1=='Sorry, this photo has been deleted'):
                    print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mPhoto Has Been Delete !')
                    pass
                else:
                    check=r1.split('status":"')[1].split('"')[0]
                    if(check== 'ok'):
                        print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mThành Công !')
                    else :
                        print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mKhông Thành Công !')
                break
            except:
                print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐã Xảy Ra Lỗi Gì Đó, Vui Lòng Chờ 5 Giây...', end='\r')
                sleep(5)
                print('                                              ', end='\r')
                e=e+1
                if(e==3):
                    break

print('\n')
def job():
    x=0
    accthu=0
    followthu=0
    global checkfl
    global checklike
    global checkdie
    while True:
        if a == '1':
            aaa = len(list_acc) - 1
        elif a == '2':
            aaa = len(list_acc)
        else:
            aaa = len(list_acc)

        for i in range(aaa):
            print (Colorate.Diagonal(Colors.blue_to_green, "══════════════════════════════════════════════════════════════"))
            x1=0
            x2=0
            try:
                ran_proxi=random.randint(0, len(list_proxie)-1)
                proxie=list_proxie[ran_proxi]
            except:
                pass
            Cookie=list_acc[i]
            uaa = random.randint(0, 299)
            try:
                uafake=read_ua[uaa].split('\n')[0]
            except:
                uafake='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
            ds_user_id=Cookie.split('ds_user_id=')[1].split(';')[0]
            headersig = {
                'authority': 'www.instagram.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
                'cache-control': 'max-age=0',
                'cookie': Cookie,
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': uafake,
                'viewport-width': '1366',
            }
            while True:
                try:
                    accthu=accthu+1
                    response = requests.get('https://www.instagram.com/',headers=headersig).text
                    checkdie=response.split('class="')[1].split(' ')[0]
                    if(checkdie=='no-js'):
                        print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;31m ➩ \033[1;32mAccount Number {accthu} Die')
                        break
                    else:
                        userig = response.split(f'username')[1]
                        user = userig.split('"')[2].split("\\")[0]
                        break
                except:
                    print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐã Xảy Ra Lỗi Gì Đó, Vui Lòng Chờ 5 Giây...', end='\r')
                    sleep(5)
                    print('                                              ', end='\r')
            if(checkdie=='no-js'):
                continue
            else:
                check=0
                while True:
                    try:
                        cauhinh = safe_get_json(f'https://traodoisub.com/api/?fields=instagram_run&id={ds_user_id}&access_token={tokenn}')
                        if 'success' in cauhinh:
                            print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mAccount Number {accthu} | Cấu Hình ID : {user} Thành Công' )
                            break
                        else:
                            check=check+1
                            print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mAccount Number {accthu} | Cấu Hình ID : {user} Thất Bại' )
                            sleep(10)
                            if(check==3):
                                break
                    except:
                        print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐã Xảy Ra Lỗi Gì Đó, Vui Lòng Chờ 5 Giây...', end='\r')
                        sleep(5)
                        print('                                              ', end='\r')
            if(check==3):
                pass
            else:
                if(checkfl=='on'):
                    kkk=0
                    demfl=0
                    while True:
                        checkk=0
                        while True:
                            try:
                                job = safe_get_json(f'https://traodoisub.com/api/?fields=instagram_follow&access_token={tokenn}')
                                job=job['data']
                                checkid=job[0]['id']
                                break
                            except:
                                checkk=checkk+1
                                if(checkk==3):
                                    break
                                sleep(1)
                        if(checkk==3):
                            break
                        if(len(job)>=1):
                            print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mTìm Thấy {len(job)} Nhiệm Vụ Follow')
                            for job in job:
                                x=x+1
                                demfl=demfl+1
                                kkk=kkk+1
                                id=job['id']
                                idfl=id.split('_')[0]
                                hnay=datetime.now()
                                gio=hnay.hour
                                phut=hnay.minute
                                giay=hnay.second
                                print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mThời Gian : {gio}:{phut}:{giay} | Follow | {idfl} ', end='')
                                if ghj == 'on':
                                    jjj = apifl1(Cookie, idfl, uafake, proxie)
                                else:
                                    jjj = apifl2(Cookie, idfl, uafake)

                                if jjj == 0:
                                    break

                                max_retry = 3
                                for attempt in range(max_retry):
                                    duyet = safe_get_json(f'https://traodoisub.com/api/coin/?type=INS_FOLLOW_CACHE&id={id}&access_token={tokenn}')
                                    
                                    if duyet.get('data') and isinstance(duyet['data'], dict):
                                        break
                                    elif duyet.get("cache"):
                                        if not silent_mode:
                                            print(f"{Yellow}➤ [Lưu ý] Server đang cache kết quả... thử lại sau vài giây (Lần {attempt+1}/{max_retry})")
                                        sleep(3)
                                        
                                    else:
                                        break

                                if duyet.get('data') and isinstance(duyet['data'], dict):
                                    nhan = duyet['data'].get('msg', 'Không xác định')
                                    tong = duyet['data'].get('pending', 0)
                                    print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhận : {nhan} | Đang Đợi Duyệt : {tong}")
                                else:
                                    if not silent_mode:
                                        print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mKhông Thể Nhận Dữ Liệu Từ Server Khi Duyệt Nhiệm Vụ !")
                                        print(f"{Red}➤ Phản hồi: {duyet}")
                                    nhan = 'Không xác định'
                                    tong = 0


                                for i in range(int(delayfl),-1,-1):
                                    print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32m{str(i)} | Sleep ', end='\r')
                                    sleep(0.2)
                                    print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32m{str(i)} | Sleep ', end='\r')
                                    sleep(0.2)
                                    print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32m{str(i)} | Sleep ', end='\r')
                                    sleep(0.2)
                                    print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32m{str(i)} | Sleep ', end='\r')
                                    sleep(0.2)
                                    print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32m{str(i)} | Sleep ', end='\r')
                                    sleep(0.2)
                                if(kkk==sofl):
                                    break
                            if(jjj==0 or kkk==sofl):
                                try:
                                    sodu=demfl*800
                                    print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐã Xong Job Follow | Nhận Được {sodu} Xu | Đang Đợi Duyệt : {tong}')
                                except:
                                    pass
                                break
                        else:
                            print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mKhông Có Nhiệm Vụ Follow !',end='\r')
                            sleep(1)
                            print('                                              ', end='\r')
                            if(demfl >=1 ):
                                try:
                                    sodu=demfl*800
                                    print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐã Xong Job Follow | Nhận Được {sodu} Xu | Đang Đợi Duyệt : {tong}')
                                except:
                                    pass
                            x1=1
                            if(checklike!='on'):
                                x1=0
                                sleep(2)
                            break
                if(checklike=='on'):
                    demlike=0
                    ooo=0
                    while True:
                        checkk=0
                        while True:
                            try:
                                joblike = safe_get_json(f'https://traodoisub.com/api/?fields=instagram_like&access_token={tokenn}')
                                joblike=joblike['data']
                                idlike=joblike[0]['id']
                                break
                            except:
                                checkk=checkk+1
                                if(checkk==3):
                                    break
                                sleep(1)
                        if(checkk==3):
                            break
                        if(len(joblike)>=1):
                            print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mTìm Thấy {len(joblike)} Nhiệm Vụ Like         ')
                            for joblike in joblike:
                                x=x+1
                                ooo=ooo+1
                                demlike=demlike+1
                                idlike=joblike['id']
                                link=joblike['link']
                                idjob=idlike.split('_')[0]
                                hnay=datetime.now()
                                gio=hnay.hour
                                phut=hnay.minute
                                giay=hnay.second
                                print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mThời Gian : {gio}:{phut}:{giay} | Follow | {idjob} ', end='')
                                if ghj=='on':
                                    lll=apilike1(Cookie,idjob,uafake,link,proxie)
                                else :
                                    lll=apilike2(Cookie,idjob,uafake,link)
                                if(lll==0):
                                    break
                                if duyet.get('data') and isinstance(duyet['data'], dict):
                                    nhan = duyet['data'].get('msg', 'Không xác định')
                                    tong = duyet['data'].get('pending', 0)
                                    
                                    nhanxu = safe_get_json(f'https://traodoisub.com/api/coin/?type=INS_LIKE&id={idlike}&access_token={tokenn}')
                                    if not silent_mode:
                                        print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐã Nhận Xu : {nhanxu}")

                                while 'error' in duyet and not silent_mode:
                                    duyet = safe_get_json(f'https://traodoisub.com/api/coin/?type=INS_LIKE_CACHE&id={idlike}&access_token={tokenn}')
                                    if('success' in duyet):
                                        break
                                
                                for i in range(int(delaylike),-1,-1):
                                    print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32m{str(i)} | Sleep ', end='\r')
                                    sleep(0.2)
                                    print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32m{str(i)} | Sleep ', end='\r')
                                    sleep(0.2)
                                    print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32m{str(i)} | Sleep ', end='\r')
                                    sleep(0.2)
                                    print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32m{str(i)} | Sleep ', end='\r')
                                    sleep(0.2)
                                    print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32m{str(i)} | Sleep ', end='\r')
                                    sleep(0.2)
                                if(ooo==solike):
                                    break
                            if(lll==0 or ooo==solike):
                                try:
                                    sodu=demlike*500
                                    print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐã Xong Job Like | Nhận Được {sodu} Xu | Đang Đợi Duyệt {tong}')
                                except:
                                    pass
                                break
                            x2=1
                        else:
                            print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mKhông Có Nhiệm Vụ Like !  ',end = '\r')
                            sleep(1)
                            print('                                                       ', end='\r') 
                            if(demlike>=1):
                                try:
                                    sodu=demlike*500
                                    print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐã Xong Job Like | Nhận Được {sodu} Xu | Đang Đợi Duyệt {tong}')
                                except:
                                    pass
                            x2=0
                            continue
            if(x1==1 or x2==1): 
                print('\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mChuyển Acc Sau',chuyenacc, 'giay:')
                for i in range(chuyenacc, -1, -1):
                    print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mPlease Wait After {i} •   ', end='\r')
                    sleep(0.25)
                    print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mPlease Wait After {i} ••    ', end='\r')
                    sleep(0.25)
                    print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mPlease Wait After {i} •••    ', end='\r')
                    sleep(0.25)
                    print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mPlease Wait After {i} ••••    ', end='\r')
                    sleep(0.25)
                    print('                                                  ', end='\r')
job()