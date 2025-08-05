#!/usr/bin/env python3

try:
    import requests, time, os, re, json, sys
    from rich import print as println  
    from pystyle import Colors, Colorate
    import platform
    import random
    from fake_useragent import UserAgent
    from time import sleep

except ModuleNotFoundError:
    print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31m Bạn Chưa Setup, Đang Setup...")
    os.system('pip install requests rich pystyle fake_useragent')
    print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32m Đã Setup Thành Công, Đang Thoát Để Reset...")
    sys.exit(1)

BASE_URL = "https://socioblend.com"
SUCCESS, FAILED, DELAY = [], [], {"TIME": 0}

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

class SubmitTikTokViews:
    def __init__(self, video_url: str) -> None:
        self.video_url = video_url
        self.session = requests.Session()

    def RetrieveCookies(self) -> str:
        self.session.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
            "Host": "socioblend.com",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": f"{UserAgent().random}"
        }
        response = self.session.get(f"{BASE_URL}/Free-TikTok-Views", verify=True, allow_redirects=True)
        cookies_string = "; ".join([f"{key}={value}" for key, value in self.session.cookies.get_dict().items()])
        return cookies_string

    def SubmitForm(self, cookies: str) -> None:
        global SUCCESS, FAILED, DELAY
        data = {
            "video_url": self.video_url
        }

        self.session.headers.update({
            "Content-Length": str(len(json.dumps(data))),
            "Content-Type": "application/x-www-form-urlencoded",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Cookie": cookies,
            "Accept": "*/*",
            "Sec-Fetch-Dest": "empty",
            "Origin": BASE_URL,
            "Referer": f"{BASE_URL}/free-tiktok-views",
        })

        response = self.session.post(f"{BASE_URL}/submit-tiktok.php", data=data, verify=True, allow_redirects=False)

        if '"status":"success"' in response.text:
            print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32m{response.status_code} - {response.reason}")
            print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mStatus : Đã Gửi View Thành Công !")
            print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mLink : {self.video_url}")
            print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mViews : +1000")

        elif '"retry_after"' in response.text:
            retry_after = re.search(r'"retry_after":(\d+)', response.text)
            if retry_after:
                DELAY["TIME"] = int(retry_after.group(1))
        elif 'The URL you entered is not a valid TikTok video link.' in response.text:
            print(f"\033[1;32m[\033[1;31m♤\033[1;32m] ➩ \033[1;31mURL Không Hợp Lệ, Hãy Kiểm Tra Lại !")
            sys.exit(1)
        else:
            print(f"\033[1;32m[\033[1;31m♤\033[1;32m] ➩ \033[1;31mLỗi Khi Gửi View | {response.status_code} - {response.reason}")
            FAILED.append(self.video_url)
            time.sleep(5)

def Main():
    os.system("cls" if os.name == "nt" else "clear")
    banner()
    info()

    print("\n\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mDán Liên Kết Video TikTok Hợp Lệ (Ví Dụ : https://www.tiktok.com/@...)")
    video_url = input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Link TikTok Cần Buff : \033[1;36m").strip()

    if video_url.startswith("https://www.tiktok.com/@") or video_url.startswith("https://tiktok.com/@"):
        print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐang Xử Lý, Vui Lòng Chờ...")
        time.sleep(2)

        while True:
            try:
                if DELAY["TIME"] != 0:
                    for timer in range(DELAY["TIME"], 0, -1):
                        print(f"\r\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;36mChờ {timer} Giây... | \033[1;32mThành Công : {len(SUCCESS)} | \033[1;31mThất Bại : {len(FAILED)}", end="")
                        time.sleep(1)
                    DELAY["TIME"] = 0

                submitter = SubmitTikTokViews(video_url)
                cookies = submitter.RetrieveCookies()
                submitter.SubmitForm(cookies)

            except requests.exceptions.RequestException:
                print("\n\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32m Kết Nối Mạng Không Ổn Định, Hãy Thử Lại !")
                time.sleep(10)

            except KeyboardInterrupt:
                print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mCảm Ơn Bạn Đã Tin Tưởng Và Sử Dụng Tool, Chúc Bạn May Mắn !")
                break

            except Exception as e:
                print(f"\n\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mLỗi Không Xác Định : {e}")
                time.sleep(5)
    else:
        print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mLink TikTok Không Hợp Lệ, Hãy Dùng Link Đầy Đủ Từ Trình Duyệt !")
        sys.exit(1)

Main()