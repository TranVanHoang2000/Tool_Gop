import telebot
from telebot.types import Message
import threading
import time
import re
import requests
import os, sys
import shlex
import random
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

banner()
info()
TOKEN = input("\n\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Token : \033[1;36m")
ADMIN_ID = int(input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mID Admin : \033[1;36m"))

bot = telebot.TeleBot(TOKEN)
allowed_users = set([ADMIN_ID])
waiting_for_file = {}
treo_threads = {}
treo_start_times = {}
nhay_threads = {}
nhay_start_times = {}
chui_threads = {}
chui_start_times = {}

@bot.message_handler(content_types=['document'])
def handle_document(message: Message):
    user_id = message.from_user.id
    if user_id not in allowed_users:
        return

    if user_id in waiting_for_file:
        path = waiting_for_file[user_id]
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(path, 'wb') as f:
            f.write(downloaded_file)
        bot.reply_to(message, f"➜ Đã Lưu File Thành Công Vào : {path}", parse_mode="Markdown")
        del waiting_for_file[user_id]

@bot.message_handler(commands=['them'])
def add_user(message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    match = re.search(r'/them (\d+)', message.text)
    if match:
        uid = int(match.group(1))
        allowed_users.add(uid)
        bot.reply_to(message, f"➜ Đã Thêm Người Dùng {uid}", parse_mode="Markdown")

@bot.message_handler(commands=['xoa'])
def remove_user(message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    match = re.search(r'/xoa (\d+)', message.text)
    if match:
        uid = int(match.group(1))
        allowed_users.discard(uid)
        bot.reply_to(message, f"➜ Đã Xóa Người Dùng {uid}", parse_mode="Markdown")

def treo_func(chat_id, cmd):
    os.system(cmd)

def chui_func(user_id):
    while user_id in chui_threads:
        print(f"User {user_id} đang chửi...")
        time.sleep(3)

@bot.message_handler(commands=['chui-on'])
def handle_chui(message: Message):
    user_id = message.from_user.id
    if user_id not in allowed_users:
        return
    if user_id in chui_threads:
        bot.reply_to(message, "➜ Bạn Đang Chửi Rồi !")
        return

    thread = threading.Thread(target=chui_func, args=(user_id,))
    thread.start()
    chui_threads[user_id] = thread
    chui_start_times[user_id] = time.time()
    bot.reply_to(message, "➜ Đã Bật Chửi !")

@bot.message_handler(commands=['chui-off'])
def stop_chui(message: Message):
    user_id = message.from_user.id
    if user_id in chui_threads:
        del chui_threads[user_id]
        del chui_start_times[user_id]
        bot.reply_to(message, "➜ Đã Tắt Chửi !")
    else:
        bot.reply_to(message, "➜ Bạn Chưa Bật Chửi Để Tắt !")

@bot.message_handler(commands=['help'])
def help_cmd(message: Message):
    help_text = """
🚥 Danh Sách Lệnh :
  ➜ /Chui-On : Bật Chửi
  ➜ /Chui-Off : Tắt chửi
  ➜ /Them [user_id] : Thêm người dùng
  ➜ /Xoa [user_id] : Xóa Người Dùng"""
    bot.reply_to(message, help_text, parse_mode="Markdown")

print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mBot Đang Chạy...")
bot.infinity_polling()