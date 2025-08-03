import subprocess
import sys

required_modules = [
    "selenium",
    "colorama",
    "requests",
    "prettytable",
    "webdriver-manager",
    "undetected-chromedriver"
]

for module in required_modules:
    try:
        __import__(module.replace("-", "_"))
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", module])

import undetected_chromedriver as uc
from selenium.common.exceptions import NoAlertPresentException, UnexpectedAlertPresentException
from selenium import webdriver
from colorama import Fore
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import os
from pystyle import Colors, Colorate
from time import sleep
import time

try:
	import requests,colorama,prettytable
except:
	os.system("pip install selenium.webdriver")
	os.system("pip install requests")
	os.system("pip install colorama")

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
    
class Main:
    def __init__(self):
        self.driver = None
        self.options = Options()
        self.options.add_argument("--disable-notifications")

        prefs = {"profile.default_content_setting_values.notifications": 2}
        self.options.add_experimental_option("prefs", prefs)

        # Khởi tạo Chrome driver
        self.driver = uc.Chrome(options=self.options)

        # Cập nhật XPath mới theo class/ID mới nhất
        self.xpaths = [
            "//button[contains(@class, 't-followers-button')]",       # Followers
            "//button[contains(@class, 't-likes-button')]",           # Hearts
            "//button[contains(@class, 't-commentslike-button')]",    # Comments Hearts
            "//button[contains(@class, 't-views-button')]",           # Views
            "//button[contains(@class, 't-shares-button')]",          # Shares
            "//button[contains(@class, 't-favorites-button')]",       # Favorites
            "//button[contains(@class, 't-live-button')]"             # Livestream
        ]

        self.enter_video_url = [
            "//input[@placeholder='Enter TikTok video URL']",   # Followers
            "//input[@placeholder='Enter TikTok video URL']",   # Hearts
            "//input[@placeholder='Enter TikTok video URL']",   # Comments Hearts
            "//input[@placeholder='Enter TikTok video URL']",   # Views
            "//input[@placeholder='Enter TikTok video URL']",   # Shares
            "//input[@placeholder='Enter TikTok video URL']",   # Favorites
            "//input[@placeholder='Enter TikTok video URL']"    # Livestream
        ]

        self.search_button = [
            "//button[contains(text(),'Search')]",  # Followers
            "//button[contains(text(),'Search')]",  # Hearts
            "//button[contains(text(),'Search')]",  # Comments Hearts
            "//button[contains(text(),'Search')]",  # Views
            "//button[contains(text(),'Search')]",  # Shares
            "//button[contains(text(),'Search')]",  # Favorites
            "//button[contains(text(),'Search')]"   # Livestream
        ]

        self.send_button = [
            "//button[contains(text(),'Send')]",  # Followers
            "//button[contains(text(),'Send')]",  # Hearts
            "//button[contains(text(),'Send')]",  # Comments Hearts
            "//button[contains(text(),'Send')]",  # Views
            "//button[contains(text(),'Send')]",  # Shares
            "//button[contains(text(),'Send')]",  # Favorites
            "//button[contains(text(),'Send')]"   # Livestream
        ]

        self.timer_text = [
            "//span[contains(text(),'Next Submit')]",  # Followers
            "//span[contains(text(),'Next Submit')]",  # Hearts
            "//span[contains(text(),'Next Submit')]",  # Comments Hearts
            "//span[contains(text(),'Next Submit')]",  # Views
            "//span[contains(text(),'Next Submit')]",  # Shares
            "//span[contains(text(),'Next Submit')]",  # Favorites
            "//span[contains(text(),'Next Submit')]"   # Livestream
        ]

        self.xpathnames = [
            "Followers",
            "Hearts",
            "Comment Hearts",
            "Views",
            "Shares",
            "Favorites",
            "Livestream"
        ]

        self.telegram = "https://t.me/tienich"
        self.option = 0

    def clear_console(self):
        os.system("cls" if os.name == "nt" else "clear")

    def wait_for_page_to_load(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mPage Is Ready !")
        except TimeoutException:
            print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31m001 Error - Cant Connect To Web Service")
            quit()

    def wait_for_captcha_solve(self):
        print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mVui Lòng Giải Captcha Thủ Công Trong Trình Duyệt.")
        input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhấn Enter Sau Khi Captcha Đã Được Giải Và Giao Diện Chính Đã Hiện Ra...")

    def check_if_button_is_enabled(self, button): 
        if button.is_enabled():
            return True
        else:
            return False



    def check_button_status(self, xpath):
        try:
            element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, xpath)))
            if element.is_enabled():
                return f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mOnline"
            else:
                return f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mOffline"
        except TimeoutException:
            return f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mNot Found"

    def display_button_list(self):
        text = "\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mDecide Which Bot You Want [1 To 8]\n"
        for i in range(7):
            text = text + "[" + str(i+1) + "] " + self.xpathnames[i] + " " + self.check_button_status(self.xpaths[i]) + "\n" 
            i+=i
        text = text + f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32m 8 - Telegram [Online]"
        print(text)

    def click_button(self, number_option):
        try:
            xpath = self.xpaths[number_option - 1]
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
            if element.is_enabled():
                element.click()
            else:
                print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31m004 Error - Offline OR Number not found")
                quit()
        except TimeoutException:
            print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31m005 Error - Offline OR Number not found OR Network error")
            quit()



    def user_input_option(self):
        self.option = int(input())
        if self.option == 8:
            self.driver.get(self.telegram)
        else:
            self.click_button(self.option)

    def check_if_website_loaded(self, path, message, error_message, delay):
        try:
            myElem = WebDriverWait(self.driver, delay).until(
                EC.presence_of_element_located((By.CLASS_NAME, path))
            )
            print(message)
        except TimeoutException:
            print(error_message)
            quit()
        except UnexpectedAlertPresentException:
            try:
                alert = self.driver.switch_to.alert
                alert.dismiss()
                print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐã phát hiện và đóng alert.")
            except NoAlertPresentException:
                print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mKhông có alert nào xuất hiện.")


    def get_insert_tiktok_link(self):
        print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mSend the Tiktok Link")
        tiktok_link = input()
        myElem = None
        try:
            myElem = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, self.enter_video_url[self.option-1])))
            print("\n\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mLoading input Field")
        except TimeoutException:
            print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31m006 Error - Cant Find Input Field")
            quit()
        myElem = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, self.enter_video_url[self.option-1])))
        myElem.send_keys(str(tiktok_link))

        time.sleep(2)



    def send(self):
        text_box = None
        search_button = None
        send_button = None
        
        #Search Button init
        try:
            search_button = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.search_button[self.option-1])))
            print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mLoading Search Field") 
            time.sleep(1)
            search_button.click()
        except TimeoutException:
            print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31m009 Error - Search not Found OR disabled")
            quit()

        time.sleep(3)


        #Send Button init
        try:
            send_button = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.send_button[self.option-1])))
            time.sleep(1)
            send_button.click()
            print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mLoading Button Field")
            print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mLoaded Everything successfully!")
            print(f"\n\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mBot Is Running Now")
            self.successfully_message()
            self.generate_and_send(text_box, search_button, send_button)
        except TimeoutException:
            print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mLoading Text Field")
            

        time.sleep(1)

        #Trying to get textbox
        try:
            text_box = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.timer_text[self.option-1])))
            print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mLoaded Everything successfully!")
            print(f"\n{Fore.WHITE}[BOT IS RUNNING NOW]{Fore.RESET}")
            self.generate_and_send(text_box, search_button, send_button)
        except TimeoutException:
            print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31m008 Error - Send Key not Found")
            quit()

       


    def generate_and_send(self, text_box, search_button, send_button):
        delay = 900
        
        #Send Message
        try:
            while True:
                text_box = WebDriverWait(self.driver, delay).until(EC.text_to_be_present_in_element((By.XPATH, self.timer_text[self.option-1]), "Next Submit: READY....!"))
                time.sleep(3)
                search_button.click()
                send_button = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.send_button[self.option-1])))
                time.sleep(5)
                send_button.click()
                self.successfully_message()
                text_box = None
        except TimeoutException:
            print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31m007 Error - Cant send "+(self.xpathnames[self.option+1])+" because of Connection Error or Closed Service")
            quit()




    def successfully_message(self):
        print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mSend "+(self.xpathnames[self.option-1])+" Successfully!")

    def main(self):
        self.clear_console()
        banner()
        info()

        self.driver.get("https://zefoy.com/")

        print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mBot Loading, please wait!")
        self.wait_for_page_to_load()
        time.sleep(2)
        self.wait_for_captcha_solve()
        
        self.display_button_list()
        self.user_input_option()

        time.sleep(1)
        self.check_if_website_loaded('row', "\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mStarted successfully!", "\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32m006 Error - Site cant Connect AND Load", 5)

        self.get_insert_tiktok_link()
        self.send()

        # Weitere Schritte und Methoden hier einfügen

        self.driver.quit()


if __name__ == "__main__":
    main = Main()
    main.main()