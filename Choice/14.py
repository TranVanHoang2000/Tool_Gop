import requests
from bs4 import BeautifulSoup
import time

def get_temp_email():
    url = "https://10minutemail.net/?lang=vi"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    
    session = requests.Session()
    response = session.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        
        email_input = soup.find("input", {"id": "fe_text"})
        email = email_input["value"] if email_input else "\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mKhông Lấy Đuợc Rmail"
        
        return email, session.cookies.get_dict()
    else:
        return "\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mLỗi Kết Nối", {}

def keep_email_alive(cookies):
    url = "https://10minutemail.net/mailbox.ajax.php?_="
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    session = requests.Session()
    session.cookies.update(cookies)
    
    while True:
        response = session.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            mails = soup.find_all("tr", style="font-weight: bold; cursor: pointer;")
            for mail in mails:
                sender = mail.find("a", class_="row-link").text.strip()
                content = mail.find_all("a", class_="row-link")[1].text.strip()
                print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNgười Gửi : {sender} | Nội Dung : {content}")
        else:
            print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mLỗi Kết Nối Tới Mailbox")
        time.sleep(10)  

if __name__ == "__main__":
    email, cookies = get_temp_email()
    print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mEmail Tạm Thời : {email}")
    keep_email_alive(cookies)