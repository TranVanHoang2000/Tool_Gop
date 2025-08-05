import requests
import random
import string
import hashlib
import os, sys
from time import sleep
from pystyle import Colors, Colorate
try:
    from faker import Faker
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad
    import requests
except ImportError:
    os.system('pip install Faker')
    os.system('pip install requests')
    os.system('pip install pycryptodome')
from faker import Faker
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import requests

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

def reverse_string(s):
    return s[::-1]

def xePwjMDG(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

def tLx6cpsx():
    url = 'https://api.mail.tm/domains'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['hydra:member']
        else:
            pass
            return None
    except Exception as e:
        print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;31mLỗi : {e}')
        return None

def f9kSLNSXl():
    fake = Faker()
    mail_domains = tLx6cpsx()
    if mail_domains:
        domain = random.choice(mail_domains)['domain']
        username = xePwjMDG(10)
        password = fake.password()
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=45)
        first_name = fake.first_name()
        last_name = fake.last_name()
        url = 'https://api.mail.tm/accounts'
        headers = {'Content-Type': 'application/json'}
        data = {'address': f'{username}@{domain}', 'password': password}
        try:
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 201:
                print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐã Tạo Email, Đang Tạo Acc Fb : {username}@{domain}')
                return (f'{username}@{domain}', password, first_name, last_name, birthday)
            else:
                pass
                return None, None, None, None, None
        except Exception as e:
            print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;31mLỗi : {e}')
            return None, None, None, None, None
    return None, None, None, None, None

def QuanHau(email, password, first_name, last_name, birthday):
    api_key = '882a8490361da98702bf97a021ddc14d'
    secret = '62f8ce9f74b12f84c123cc23437a4a32'
    gender = random.choice(['Nam', 'Nữ'])

    req = {
        'api_key': api_key,
        'attempt_login': True,
        'birthday': birthday.strftime('%Y-%m-%d'),
        'client_country_code': 'EN',
        'fb_api_caller_class': 'com.facebook.registration.protocol.RegisterAccountMethod',
        'fb_api_req_friendly_name': 'registerAccount',
        'firstname': first_name,
        'format': 'json',
        'gender': gender,
        'lastname': last_name,
        'email': email,
        'locale': 'en_US',
        'method': 'user.register',
        'password': password,
        'reg_instance': xePwjMDG(32),
        'return_multiple_errors': True
    }

    sorted_req = sorted(req.items(), key=lambda x: x[0])
    sig = ''.join(f'{k}={v}' for k, v in sorted_req)
    ensig = hashlib.md5((sig + secret).encode()).hexdigest()
    req['sig'] = ensig

    api_url = 'https://b-api.facebook.com/method/user.register'
    response = requests.post(api_url, data=req)

    if response.status_code == 200:
        reg = response.json()
        id = reg.get('new_user_id')
        token = reg.get('session_info', {}).get('access_token')

        print (Colorate.Diagonal(Colors.blue_to_green, "══════════════════════════════════════════════════════════════"))
        print(f"""\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mEmail : {email}
\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mMật Khẩu : {password}
\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mTên : {first_name} {last_name}
\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mSinh Nhật : {birthday}
\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mGiới Tính : {gender}""")
        print (Colorate.Diagonal(Colors.blue_to_green, "══════════════════════════════════════════════════════════════"))
    else:
        print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;31mLỗi Khi Đăng Ký : {response.text}')

def WcfriFTc(url, params, post=True):
    headers = {
        'User-Agent': '[FBAN/FB4A;FBAV/35.0.0.48.273;FBDM/{density=1.33125,width=800,height=1205};FBLC/en_US;FBCR/;FBPN/com.facebook.katana;FBDV/Nexus 7;FBSV/4.1.1;FBBK/0;]'
    }
    if post:
        response = requests.post(url, data=params, headers=headers)
    else:
        response = requests.get(url, params=params, headers=headers)
    return response.json()

def create_accounts(num_accounts):
    for i in range(num_accounts):
        email, password, first_name, last_name, birthday = f9kSLNSXl()
        if email and password and first_name and last_name and birthday:
            QuanHau(email, password, first_name, last_name, birthday)

num_accounts = int(input(f'\n\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số Lượng Acc Muốn Reg : \033[1;36m'))
create_accounts(num_accounts)