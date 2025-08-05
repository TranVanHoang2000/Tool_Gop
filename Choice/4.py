import os
import sys,re
import datetime
from datetime import datetime, timedelta
import json
import random
import platform
try:
  import requests
except ImportError:
  os.system('pip install requests')
  import requests
try:
  from colorama import Back, Fore, Fore, Style, init
except ImportError:
  os.system('pip install colorama')
  from colorama import Back, Fore, Fore, Style, init
try:
  from bs4 import BeautifulSoup
except ImportError:
  os.system('pip3 install beautifulsoup4')
  from bs4 import BeautifulSoup
try:
	from pystyle import Colors, Colorate
except ImportError:
	os.system('pip install pystyle')
	from pystyle import Colors, Colorate
try:
  import cloudscraper
except ImportError:
  os.system('pip install cloudscraper')
  import cloudscraper
import time
from time import sleep
import json,ast

os.system('cls' if os.name == 'nt' else 'clear')

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

def pr3(text):
  lines = text.split('\n')
  for line in lines:
      sys.stdout.write(line+'\n')
      sys.stdout.flush()
      sleep(0.1)
def pr(text):
  for i in range(len(text)+1):
      sys.stdout.write("\r" + text[:i])
      sys.stdout.flush()
      sleep(0.01)
  print()

def time():
  current_time = datetime.now()

  time = current_time.strftime("%M:%S")
  return time

def cint(number):
  while True:
    try:
      numbers = int(input(number))
      return numbers
    except ValueError:
      print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mVui Lòng Chỉ Nhập Số')

def changetoken(red,green,white):
  if os.path.exists("Cache_Golike_Auth.txt"):
    text=f'''\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mBạn Muốn Dùng Auth Cũ Hay Đổi Auth
\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m1\033[1;32m]\033[1;36m Đổi Auth
\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m2\033[1;32m]\033[1;36m Dùng Auth Cũ'''
    pr3(text)
    changetoken=cint(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số : \033]1;36m')
    print (Colorate.Diagonal(Colors.blue_to_green, "══════════════════════════════════════════════════════════════"))
    if changetoken==1:
      file_name = 'Cache_Golike_Auth.txt'
      if os.path.exists(file_name):
          os.remove(file_name)
    else:
      pass

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

def bes4(url):
  html_source = requests.get(url).text
  soup = BeautifulSoup(html_source, 'html.parser')
  og_description = soup.find('meta', {'property': 'og:description'})
  if og_description:
      text =og_description['content']
      return text
  else:
      print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mKhông Tìm Thấy Thẻ Meta Với Thuộc Tính property='og:description'")

def checkauth(red, blue, green, yellow, cyan, magenta, orange, xanhnhat, xduong, pink):
    scraper = cloudscraper.create_scraper()

    while True:
        if not os.path.exists("Cache_Golike_Auth.txt"):
            auth = str(input(f'\n\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Auth : \033[1;36m'))
        else:
            with open('Cache_Golike_Auth.txt') as f:
                auth = f.read().strip()

        headers = {
            'Authorization': auth,
            't': 'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
            'User-Agent': "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
        }

        try:
            response = scraper.get('https://gateway.golike.net/api/tiktok-account', headers=headers)
        except Exception as e:
            print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mKhông Thể Kết Nối Tới API : {e}")
            continue

        if response.status_code == 200:
            if response.text.strip():
                try:
                    check = response.json()
                except json.JSONDecodeError:
                    print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mPhản Hồi Không Hợp Lệ (Không Phải JSON) : ")
                    print(response.text)
                    continue
            else:
                print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mPhản Hồi Rỗng, Có Thể Auth Không Đúng !")
                continue
        else:
            print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mAuth Sai Hoặc Bị Từ Chối (status code: {response.status_code})")
            continue

        if check.get('status') == 200:
            name = check['data'][0]['username']
            hea = {
                'Authorization': auth,
                't': 'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
                'User-Agent': headers['User-Agent']
            }

            try:
                report_response = scraper.get('https://gateway.golike.net/api/statistics/report', headers=hea)
                data = report_response.json()
            except Exception:
                print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mLỗi Khi Lấy Thống Kê !")
                continue

            total_pending_coin = sum(
                value['pending_coin'] for key, value in data.items()
                if isinstance(value, dict) and 'pending_coin' in value
            )
            xht = data.get('current_coin', 0)

            pr(f'\n\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mTên Tài Khoản : {name}')
            pr(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32m Số Dư Hiện Tại :{green}{xht}đ')
            pr(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mChờ Duyệt :{total_pending_coin}đ')

            nicknames = [item['nickname'] for item in check['data'] if 'nickname' in item]
            print (Colorate.Diagonal(Colors.blue_to_green, "══════════════════════════════════════════════════════════════"))
            pr(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mSelect Acc Chạy Nhiệm Vụ')
            for i, nickname in enumerate(nicknames, start=1):
                globals()[f'{i}'] = nickname
                pr(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32m{i} : {nickname}')

            with open("Cache_Golike_Auth.txt", "w") as f:
                f.write(auth)

            return auth, check
        else:
            pr(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mAuth Không Hợp Lệ, Hãy Thử Lại !')

def get_id_from_nickname_number(ranmau,check,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink):
  while True :    
    user_input=input(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32m{random.choice(ranmau)} | {random.choice(ranmau)} | {random.choice(ranmau)} - Chọn Acc TikTok Muốn Chạy Job : \033]1;36m')
    try:
      n = int(user_input)
      if 'data' in check and len(check['data']) >= n:
          idtiktok = check['data'][n-1]['id']
          if idtiktok :
              text=f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mID Của NickName Số {n} Là : \033]1;36m{idtiktok}"
              pr(text)
              print (Colorate.Diagonal(Colors.blue_to_green, "══════════════════════════════════════════════════════════════"))
              return idtiktok 
          else:
              text=f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mKhông Tìm Thấy NickName Tương Ứng !"
              pr(text)
      else:
          continue 
    except ValueError:
          pr(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mVui Lòng Chỉ Nhập Số !")
          continue 

def getjob(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink):
    startmaxjob=1
    job_success=0
    hea={
'Authorization':	auth,
't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
}
    while True:
      while True:
        try:
              a=requests.get(f'https://gateway.golike.net/api/advertising/publishers/tiktok/jobs?account_id={idtiktok}&data=null',headers=hea).json()
              break
        except:
            print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mCó Lỗi Gì Đó, Đang Nhận Lại Nhiệm Vụ...")
            sleep(2)
            pass
      try:
        link=a['data']['link']
        id=a['data']['id']
        object_id=a['lock']['object_id']
        os.system(f'termux-open-url {link}')
        for k in range(delay,-1,-1):
            mau=random.choice(ranmau)
            print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mThành Công : {job_success}/{startmaxjob} | {random.choice(ranmau)}Loading{random.choice(ranmau)} - Nhiệm Vụ Mới Sau {random.choice(ranmau)} | {random.choice(ranmau)}[{k}s]',end='\r')
            sleep(1)
        print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐang Kiểm Tra Hành Động...',end='\r')
        headers = {
            'authorization': auth,
        't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
        'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
                      }
      
        json_data = {
            'ads_id': id,
            'account_id': idtiktok ,
            'async': True,
            'data': None,
                      }
        while True:
            try:
                g =requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',headers=headers,json=json_data).json()
                break
            except:
                print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mĐã Xảy Ra Lỗi Gì đó, Đang Thử Lại...',end="\r")
                sleep(2)
                pass
        if g['status']==200:
            job_success+=1
            print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32m Thành Công : {job_success}/{startmaxjob} | {time()} | {random.choice(ranmau)} Thành Công | Follow |+{g["data"]["prices"]}')
            startmaxjob+=1
            jobloi=0
            if startmaxjob == maxjob+1:
                print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐã Đạt Max Job !')
                return

        else:
            print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐang Kiểm Tra Lại Hành Động...',end="\r")
            sleep(2)
            while True:
                try:
                    g = requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',headers=headers,json=json_data).json()
                    break
                except:
                    print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐang Nhận Lại Phần Thưởng...',end="\r")
                    sleep(2)
            if g['status']==200:
                job_success+=1
                print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mThành Công : {job_success}/{startmaxjob} | {time()} | {random.choice(ranmau)}Thành Công | Follow | +{g["data"]["prices"]}')
                startmaxjob+=1
                jobloi=0
                if startmaxjob == maxjob+1:
                    print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐã Đạt Max Job !')
                    return
            else:
                print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐang Bỏ Qua Nhiệm Vụ...',end='\r')
                headers = {
                    'authorization': auth,
                    't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
                    'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
                            }
                
                json_data = {
                    'description': 'Báo cáo hoàn thành thất bại',
                    'users_advertising_id': id,
                    'type': 'ads',
                    'provider': 'tiktok',
                    'fb_id': idtiktok ,
                    'error_type': 3,
                              }
                
                requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data)
            
              
                headers = {
                    'authorization': auth,
                    't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
                    'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
                          }
                
                json_data = {
                    'ads_id': id,
                    'object_id': object_id,
                    'account_id': idtiktok ,
                    'type': 'follow',
                              }
                skipjob=requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',headers=headers,json=json_data)
                startmaxjob+=1
                jobloi+=1
                if startmaxjob == maxjob+1:
                    print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐã Đạt Max Job !')
                    return
                elif jobloi==15:
                    select=input(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mLỗi Nhiều, Bạn Có Muốn Đổi Nick ? (y/n) :')
                    if select.lower() == 'n':
                        pass
                    else:
                        nicknames = [item['nickname'] for item in check['data'] if 'nickname' in item]
                        for i, nickname in enumerate(nicknames, start=1):
                            globals()[f'{i}'] = nickname
                        print (Colorate.Diagonal(Colors.blue_to_green, "══════════════════════════════════════════════════════════════"))
                        text=f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mSelect Acc Chạy Nhiệm Vụ '
                        pr(text)
                        for i, nickname in enumerate(nicknames, start=1):
                            text=f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32m{i} : {globals()[f"{i}"]}'
                            pr(text)
                        idtiktok = get_id_from_nickname_number(ranmau,check,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
                        jobloi=0

      except:
          print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐang Nhận Lại Nhiệm Vụ...',end='\r')
          sleep(2)

def getjob_follow(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink):
    startmaxjob=1
    job_success=0
    jobloi=0
    hea={
'Authorization':	auth,
't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
}
    while True:
      while True:
        try:
              a=requests.get(f'https://gateway.golike.net/api/advertising/publishers/tiktok/jobs?account_id={idtiktok}&data=null',headers=hea).json()
              break
        except:
            print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mCó Lỗi Gì Đó, Đang Nhận Lại Nhiệm Vụ...")
            sleep(2)
            pass
      try:
        link=a['data']['link']
        id=a['data']['id']
        object_id=a['lock']['object_id']
        if 'video' in link:
            print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐang Lọc Job Like           ",end='\r')
            headers = {
                'authorization': auth,
                't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
                'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
                        }
            
            json_data = {
                'description': 'Tôi không muốn làm Job này',
                'users_advertising_id': id,
                'type': 'ads',
                'provider': 'tiktok',
                'fb_id': idtiktok,
                'error_type': 0,
                        }

            response = requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data)

            
            json_data = {
                'ads_id': id,
                'object_id': object_id,
                'account_id': idtiktok,
                'type': 'like',
                        }
            response = requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',headers=headers,json=json_data)
        else:  
            os.system(f'termux-open-url {link}')
            for k in range(delay,-1,-1):
                mau=random.choice(ranmau)
                print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mThành Công : {job_success}/{startmaxjob} | {random.choice(ranmau)}Loading{random.choice(ranmau)} - Nhiệm Vụ Mới Sau{random.choice(ranmau)} | {random.choice(ranmau)}[{k}s]',end='\r')
                sleep(1)
            print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐang Kiểm Tra Hành Động...',end='\r')
            headers = {
                'authorization': auth,
            't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
            'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
                         }
          
            json_data = {
                'ads_id': id,
                'account_id': idtiktok ,
                'async': True,
                'data': None,
                         }
            while True:
                try:
                    g =requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',headers=headers,json=json_data).json()
                    break
                except:
                    print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mCó Lỗi Gì Đó, Đang Thử Lại...',end="\r")
                    sleep(2)
                    pass
            if g['status']==200:
                job_success+=1
                print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mThành Công : {job_success}/{startmaxjob} | {time()} | {random.choice(ranmau)}Thành Công | Follow | +{g["data"]["prices"]}')
                startmaxjob+=1
                jobloi=0
                if startmaxjob == maxjob+1:
                    print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐã Đạt Max Job !')
                    return

            else:
                print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐang Kiểm Tra Lại Hành Động...',end="\r")
                sleep(2)
                while True:
                    try:
                        g = requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',headers=headers,json=json_data).json()
                        break
                    except:
                        print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐang Nhận Lại Phần Thưởng...',end="\r")
                        sleep(2)
                if g['status']==200:
                    job_success+=1
                    print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mThành Công : {job_success}/{startmaxjob} | {time()} | {random.choice(ranmau)}Thành Công | Follow | +{g["data"]["prices"]}')
                    startmaxjob+=1
                    jobloi=0
                    if startmaxjob == maxjob+1:
                        print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐã Đạt Max Job !')
                        return
                else:
                    print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mĐang Bỏ Qua Nhiệm Vụ...',end='\r')
                    headers = {
                        'authorization': auth,
                        't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
                        'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
                                }
                    
                    json_data = {
                        'description': 'Báo cáo hoàn thành thất bại',
                        'users_advertising_id': id,
                        'type': 'ads',
                        'provider': 'tiktok',
                        'fb_id': idtiktok ,
                        'error_type': 3,
                                 }
                    
                    requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data)
                
                  
                    headers = {
                        'authorization': auth,
                        't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
                        'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
                             }
                    
                    json_data = {
                        'ads_id': id,
                        'object_id': object_id,
                        'account_id': idtiktok ,
                        'type': 'follow',
                                 }
                    skipjob=requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',headers=headers,json=json_data)
                    startmaxjob+=1
                    jobloi+=1
                    if startmaxjob == maxjob+1:
                        print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐã Đạt Max Job !')
                        return
                    elif jobloi==15:
                        select=input(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mLỗi Nhiều, Bạn Có Muốn Đổi Nick ? (y/n) :')
                        if select.lower() == 'n':
                            pass
                        else:
                            nicknames = [item['nickname'] for item in check['data'] if 'nickname' in item]
                            for i, nickname in enumerate(nicknames, start=1):
                                globals()[f'{i}'] = nickname
                            print (Colorate.Diagonal(Colors.blue_to_green, "══════════════════════════════════════════════════════════════"))
                            text=f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mSelect Acc Chạy Nhiệm Vụ '
                            pr(text)
                            for i, nickname in enumerate(nicknames, start=1):
                                text=f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32m{i} : {globals()[f"{i}"]}'
                                pr(text)
                            idtiktok = get_id_from_nickname_number(ranmau,check,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
                            jobloi=0

      except:
          print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐang Nhận Lại Nhiệm ụ...',end='\r')
          sleep(2)

def creat_key():
  current_time = datetime.now()
  time = current_time.strftime("%F")
  characters_to_choose_from = 'qưertyuiopasdghjklzxcvbnmQWERTYUIOPASDGHJKLZXCVBNM123456789'
  characters = 'qưertyuiopasdghjklzxcvbnmQWERTYUIOPASDGHJKLZXCVBNM123456789'
  randoma = ''.join(random.choice(characters_to_choose_from) for _ in range(10))
  end_link = ''.join(random.choice(characters) for _ in range(10))
  dulieu=f'Key-{time}-{randoma}'
  notelink= f'https://laylinkngon.000webhostapp.com/?text={dulieu}'
  data = {
    'url': notelink,
    'custom': '',
    'expiry': '',
    'password': '',
    'description': '',
    'multiple': '0',
        }

  response = requests.post('https://bom.so/shorten', data=data).json()
  note=response['short']
  shortlink=requests.get(f"https://3link.co/api?api=e21aeb8a5f25d560d53a6881ae7b74703470f98d&url={note}").json()
  shortlink=shortlink['shortenedUrl']
  return shortlink,dulieu

blue='\033[38;5;12m'
cyan='\033[38;5;14m'
white='\033[1;39m'
magenta='\033[38;5;5m'
orange='\033[38;5;202m'
xanhnhat = "\033[1;36m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
xduong = "\033[1;34m"
pink = "\033[1;35m"
trang = "\033[1;39m"
whiteb="\033[1;39m"
redb="\033[1;31m"
end='\033[0m'

ranmau=(red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)

while True:
  banner()
  info()
  current_time = datetime.now()
  time_key = current_time.strftime("%F")
  changetoken(red,green,white) 
  auth,check =checkauth(red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
  if not os.path.exists("Setting_Golike.txt"):
      idtiktok =get_id_from_nickname_number(ranmau,check,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
      print(f'''\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32m Bạn Có Muốn Lọc Job Like Không :
\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m4\033[1;32m]\033[1;36m Có
\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m4\033[1;32m]\033[1;36m Không''')
      select_job=cint(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số : \033]1;36m')
      delay =cint(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Delay : \033]1;36m')
      maxjob= cint(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Max Job : \033]1;36m')
      setting={
        "loaijob":select_job,
        "delay":delay,
        "maxjob":maxjob
      }

      file = open("Setting_Golike.txt", "a")
      file.write(json.dumps(setting))
      file.close()
      print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32m Khởi Chạy Nhiệm Vụ') 
      print (Colorate.Diagonal(Colors.blue_to_green, "══════════════════════════════════════════════════════════════"))
      sleep(1)
      if select_job==1:
        getjob_follow(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
      else:
        getjob(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)   
          
                
  else: 
        idtiktok = get_id_from_nickname_number(ranmau,check,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
        select_setting=input(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mBạn Có Muốn Sử Dụng Setting Cũ Không ? (y/n) : \033]1;36m' )
        if select_setting.lower() == 'n':
            os.remove('Setting_Golike.txt')
            idtiktok =get_id_from_nickname_number(ranmau,check,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
            print(f'''\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32m Bạn Có Muốn Lọc Job Like Không :
\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m4\033[1;32m]\033[1;36m Có
\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m4\033[1;32m]\033[1;36m Không''')
            select_job=cint(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số : \033]1;36m')
            delay =cint(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Delay : \033]1;36m')
            maxjob= cint(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Max Job : \033]1;36m')
            setting={
              "loaijob":select_job,
              "delay":delay,
              "maxjob":maxjob
            }
            file = open("Setting_Golike.txt", "a")
            file.write(json.dumps(setting))
            file.close()

            print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mKhởi Chạy Nhiệm Vụ') 
            print (Colorate.Diagonal(Colors.blue_to_green, "══════════════════════════════════════════════════════════════"))
            sleep(1)
            if select_job==1:
              getjob_follow(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
            else:
              getjob(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)   
                
                      
        else:
          try:
              with open("Setting_Golike.txt", "r") as file:
                data_txt=file.read()
                data_json = json.loads(data_txt)
                select_job = int(data_json.get('loaijob'))
                delay = int(data_json.get('delay'))
                maxjob= int(data_json.get('maxjob'))
                print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mKhởi Chạy Nhiệm Vụ') 
                print (Colorate.Diagonal(Colors.blue_to_green, "══════════════════════════════════════════════════════════════"))
                sleep(1)
                if select_job==1:
                  getjob_follow(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
                else:
                  getjob(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
          except json.JSONDecodeError:
              print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mDữ Liệu Không Hợp Lệ, Vui Lòng Kiểm Tra Lại Định Dạng JSON Trong Tệp !")