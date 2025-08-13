# -*- coding: utf-8 -*-
import json
import time
import threading
import os
import sys
from concurrent.futures import ThreadPoolExecutor
from zlapi import ZaloAPI
from zlapi.models import *
from pystyle import Colors, Colorate
from time import sleep

DATA_FILE = "data_warzl.json"

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        f.write("{}")

def load_config():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_config(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

config = load_config()

with open(DATA_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

hiden_uid = data.get("uid")
hiden_prefix = data.get("prefix")

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

if "imei" in config and config["imei"].strip():
    imei = config["imei"]
    print(f"\n\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mImei Đã Lưu : \033[1;36m{imei}")
else:
    imei = input("\n\033[1;32m[\033[1;31m♤\033[1;32m] ➩ \033[1;32mNhập Imei : \033[1;36m").strip()
    config["imei"] = imei
    save_config(config)

if "cookies" in config and config["cookies"]:
    cookies_str = json.dumps(config["cookies"], ensure_ascii=False)
    print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mCookie Đã Lưu : \033[1;36m{cookies_str}")
else:
    cookies_str = input("\033[1;32m[\033[1;31m♤\033[1;32m] ➩ \033[1;32mNhập Cookie : \033[1;36m").strip()
    try:
        cookies = json.loads(cookies_str)
        config["cookies"] = cookies
        save_config(config)
    except json.JSONDecodeError:
        print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mCookie Không Đúng Định Dạng Json !")
        sys.exit()

if "prefix" in config and config["prefix"].strip():
    prefix = config["prefix"]
    print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mPrefix Đã Lưu : \033[1;36m{prefix}")
else:
    prefix = input("\033[1;32m[\033[1;31m♤\033[1;32m] ➩ \033[1;32mNhập Prefix : \033[1;36m").strip()
    config["prefix"] = prefix
    save_config(config)

if "uid" in config and config["uid"].strip():
    uid = config["uid"]
    print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mUid Đã Lưu : \033[1;36m{uid}")
else:
    uid = input("\033[1;32m[\033[1;31m♤\033[1;32m] ➩ \033[1;32mNhập Uid : \033[1;36m").strip()
    config["uid"] = uid
    save_config(config)

cookies = config["cookies"]
print (Colorate.Diagonal(Colors.blue_to_green, "══════════════════════════════════════════════════════════════"))

thread = ThreadPoolExecutor(max_workers=10000)

class Tool_WarZl(ZaloAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.auto_chatting = False
        self.start_time = time.time()
        self.copy_mode = False
        self.copy_target = set()

    def sendTxt(self, thread_id, thread_type, messages, delay=0.1):
        def auto_send():
            try:
                if isinstance(messages, str):
                    messages_list = [messages]
                elif isinstance(messages, list):
                    messages_list = [m for m in messages if isinstance(m, str) and m.strip()]
                else:
                    self.sendMessage(Message(text="➜ ❌ Sai Định Dạng Tin Nhắn Spam"), thread_id, thread_type)
                    return

                if not messages_list:
                    self.sendMessage(Message(text="➜ 🚫 Không Có Nội Dung Để Spam"), thread_id, thread_type)
                    return

                index = 0
                while self.auto_chatting:
                    self.sendMessage(Message(text=messages_list[index]), thread_id, thread_type)
                    index = (index + 1) % len(messages_list)
                    time.sleep(delay)

            except Exception as e:
                self.sendMessage(Message(text=f"➜ ⛔ Lỗi : {str(e)}"), thread_id, thread_type)
                self.auto_chatting = False

        threading.Thread(target=auto_send, daemon=True).start()

    def onMessage(self, mid, author_id, message, message_object, thread_id, thread_type):
        threading.Thread(target=self.onHandle, args=(mid, author_id, message, message_object, thread_id, thread_type)).start()
        print(Colorate.Diagonal(Colors.blue_to_green, "══════════════════════════════════════════════════════════════"))
        print(f"\033[1;32m[\033[1;31m♤\033[1;32m] ➩ \033[1;32mTin Nhắn : \033[1;36m{author_id} | \033[1;33m{message}")
        if self.copy_mode and author_id in self.copy_target:
            self.replyMessage(
                Message(text=message),
                message_object,
                thread_id=thread_id,
                thread_type=thread_type
            )

    def onHandle(self, mid, author_id, message, message_object, thread_id, thread_type):
        if hiden_uid and str(author_id) != str(hiden_uid):
            return

        if message == f"{prefix}help":
            ds_menu = f"""
🎉 Chào Mừng Bạn Đến Với Menu War :
  ➜ {prefix}uid : 🤲 Lấy Uid Của Người Dùng
  ➜ {prefix}time : ♨️ Xem Thời Gian Bot Hoạt Động
  ➜ {prefix}reset : ♻️ Khởi Động Lại Bot
  ➜ {prefix}war on/off : ✅ Bật / ⛔ Tắt Chế Độ War 🤡
  ➜ {prefix}reo on/off [@Tag] : ✅ Bật / ⛔ Tắt Chế Độ Chửi 🤬
  ➜ {prefix}nhay on/off : ✅ Bật / ⛔ Tắt Chế Độ Nhây 🤪
  ➜ {prefix}nhai on/off [@Tag] : 👨‍💻 Copy Tin Nhắn Người Được Tag 😜
  ➜ {prefix}treo on/off : ✅ Bật / ⛔ Tắt Chế Độ Treo Nội Dung Sẵn 💀
  ➜ {prefix}treogr on/off : ✅ Bật / ⛔ Tắt Treo + Tag All liên tục (Cẩn Thận Kick) 😤
  ➜ {prefix}allan [Nội Dung] : 🙃 Tag Tất Cả Thành Viên Ẩn 🎃
"""
            self.replyMessage(
                Message(text=ds_menu),
                message_object,
                thread_id=thread_id,
                thread_type=thread_type
            )
        # --- UID ---
        elif message.startswith(f"{prefix}uid"):
            if message_object.mentions:
                tagged_users = message_object.mentions[0]['uid']
            else:
                tagged_users = author_id
            self.replyMessage(Message(text=f"➜ Uid Của Bạn : {str(tagged_users)}"), message_object, thread_id, thread_type)
        # --- TIME ---
        elif message.startswith(f"{prefix}time"):
            uptime = time.time() - self.start_time
            days, remainder = divmod(uptime, 86400)
            hours, remainder = divmod(remainder, 3600)
            minutes, seconds = divmod(remainder, 60)
            uptime_str = f"{int(days)} Ngày, {int(hours)} Giờ, {int(minutes)} Phút, {int(seconds)} Giây"
            self.sendMessage(Message(text=f"➜ Time : {uptime_str}"), thread_id, thread_type)
        # --- RESET ---
        elif message.startswith(f"{prefix}reset"):
            self.sendMessage(Message(text="➜ Đang Khởi Động Lại, Vui Lòng Chờ..."), thread_id, thread_type)
            os.execv(sys.executable, [sys.executable] + sys.argv)
        elif message.startswith(f"{prefix}war on"):
            if message.strip() == f"{prefix}war off":
                self.auto_chatting = False
                self.sendMessage(Message(text="➜ Đã Dừng War Thành Công !"), thread_id, thread_type)
            else:
                if self.auto_chatting:
                    self.sendMessage(Message(text="➜ Nhập Sai Định Dạng Hoặc Lỗi"), thread_id, thread_type)
                else:
                    self.auto_chatting = True
                    spam_list = [
                        "me m rach ak",
                        "chao ban nho rain👋👋👋🗿😏😋😮😐😮😰😮😰😮😨😮",
                        "dit me nha may rain🖕🖕🖕😰👹😰😮😰😮😰😮😰😮😰😮",
                        "thang con cac nay rain👉☝️😘😞🤪😞😘😵😵😘👉😫👉☝️👋",
                        "dit me con nay bu dai tao gioi lam rain😰😨😅😰😅👿😰😅☝️😅👉😮👉🤯",
                        "cha sinh me de ra thang lon hay gi rain🤯🤯🤯😏😞😏😵😘👉🤯☝️🤯😰😄😨",
                        "dit rain😠😠😠😐😍😂😍😞😮😰😅😰😅🥪🍨🥪🥫🍤🍭🍤🥧🍤",
                        "con rain 😓😓😓😄😰😅☝️😄☝️😮👉☝️🤯🤯",
                        "me rain🤯🤯🤯😱🤔🤭😤😱😠😓😤😞🙄",
                        "nha rain😮😮😮😰😅🥰😅👿😅💌😅🥪🍮🥫🍨🥫🍤🥫🍤🥪🍤",
                        "may rain😫😫😫👺🤥👺👻👹👾👺👿🎃👿",
                        "luon rain😞😞😞👂💪👂👁️👣👍👃👊👃💪🤲💪🥪🍨🥪🍨🥪🍤🥪🍤🥪🍤",
                        "ha dit cha m rain😵😵😵✍️✍️🤝🤳💅🤳💅💇🚶🧖🧘🤾🤼",
                        "sao vay thang lon rain🥺🥺🥺🧟🦸🧙💂🧙🤴👩‍🚀💂👩‍🚀🤶👩‍🚀🤶👩‍🚀",
                        "bo me may bi tao dit cho chet roi rain😐😐😐👩‍🎨👶👩‍🎤🧒👧👵👩‍🦰👲👨👲👨👲👨👵",
                        "thang con di me nha may rain 🤩🤩🤩👩‍❤️‍👨👪👨‍👩‍👧‍👧👨‍👩‍👧👨‍👩‍👦‍👦👨‍👨‍👧‍👧👨‍👩‍👧‍👧👪👨‍👩‍👧‍👧👪👨‍👨‍👦",
                        "sao vay thang lon cali😭😭😭🗣️👣🗣️👥🤱👥🤱👤🤱🤱👥",
                        "sua cai deo gi vay em 👹👹👹🌿🥀🌸🥀🌸🍁🌿🍁🍃🍂🍃",
                        "bo dit ca lo nha may rain 😏😏😏🍁🌿🌱🍁🌱🍁🌿🍁🍂🌿🍂🌿🍂",
                        "dit rain 😘😘😘 🏞️🌡️🌋🌡️🌡️🌀🌊⚡🌈⚡🌫️⚡🌫️🏞️🌈🏜️🌈🏜️🌈🏜️",
                        "bo may nhet cac vao mom may rain🦴🦴🦴🌌🌒🌕🌓🌕🌒🌖🌑🌗🌑🌗💫🌍☀️⭐☀️⭐",
                        "me may bi tao dit cho ko con duong song rain🗿🗿🗿🦊🐼🐰🦓🐰🦓🦓🐲🐽🦝🐨🦝🐨",
                        "thang cha con di me ho hang nha may dit ba noi cha dai me nha may con di cac nha may lon ma may dit cha noi nha m dit co di chu bac nha m dit ca tong mon nha m dit ca lon nha m dit di nha may dit nat lon nha may rain 😂😂😂🦝🐼🐰🦓🐴🦓🐲🐗🦊🐗🦊🐼🦊🐼🐴🐨🐰🐨🐯🐨🐯🐨🦊🐨🦊🐨",
                        "dit con dai me nha may rain 😋😋😋🐫🐓🐪🦆🐤🦆🦅🐓🦅🐦🦅🐦🐥🦢🐤",
                        "con di ba nha m rain 🤣🤣🤣🦗🦂🐌🦋🐚🦋🦠🦋🐾🐾🐞🐞🐌🦂🦞🦂🦞",
                        "dit me 3 que sua cai deo gi tao deo hieu rain 😌😌😌🥥🍈🍇🥦🥑🥦🥥🥦🍅🌽🍆🌽🍆🌽🥑🌽",
                        "bo dit ca lo nha m rain 🖕🖕🖕🥘🍛🍝🌮🥪🍕🥫🍕🥡🍲🍤🍲🍣🍛🍣🍛",
                        "thang cha may bi tao chat cu rain 😍😍😍🍡🍦🎂🥧🍮🥧🎂🍦🍭🍨🧁🍨🎂🍨🍮🍦",
                        "lon ma nha may dit cu may rain 🤪🤪🤪🍽️🍵🥄🥢🥢🥄🥢🔪🍶🍽️🍹🍽️🍹🥤🍵🍾",
                        "me may khong the song thieu tinh trung tao rain 🍦🍹🍦🍹🍮🥪🥪🍵🍦🍹😅😄😅😄😂😃🤣😃🤣",
                        "cali cho sua gi the tao deo hieu gi rain 🤤🙃😏🙂😏🤪🤪🤤🤫😬😬🤫😱🤔🥺🤐🤐😋😋😜😋🙂😍🙂🥰🤤",
                        "dit me chung may luon kkkk rain 🥺🤫🥰🤐😜😬🍮🍹🥪🍽️🥫😅🍤😅🔪🍭🍶🥪🥫🍽️🍾😃🍹😃🥺🤫🤐🤫🍮😅",
                        "thang lon cac nha m rain 😜🥪🍾🥪😬🙂😂🙍🧖🚶🚶🤾🧗🤼🤾🤹⛹️🏃⛹️🏃💇🙎🙋🙎🙋🙍💇",
                    ]
                    self.sendTxt(thread_id, thread_type, spam_list, delay=0.1)

        elif message.startswith(f"{prefix}reo on"):
            if message.strip() == f"{prefix}reo off":
                self.auto_chatting = False
                self.sendMessage(Message(text="➜ Đã Dừng Réo Thành Công !"), thread_id, thread_type)
            else:
                if self.auto_chatting:
                    self.sendMessage(Message(text="➜ Sai Định Dạng Hoặc Lỗi !"), thread_id, thread_type)
                else:
                    if not message_object.mentions:
                        self.sendMessage(Message(text="➜ Tag Người Cần Réo !"), thread_id, thread_type)
                        return

                    tagged_uid = message_object.mentions[0]['uid']
                    self.auto_chatting = True
                    spam_list = [
                        "me m rach ak",
                        "chao ban nho rain👋👋👋🗿😏😋😮😐😮😰😮😰😮😨😮",
                        "dit me nha may rain🖕🖕🖕😰👹😰😮😰😮😰😮😰😮😰😮",
                        "thang con cac nay rain👉☝️😘😞🤪😞😘😵😵😘👉😫👉☝️👋",
                        "dit me con nay bu dai tao gioi lam rain😰😨😅😰😅👿😰😅☝️😅👉😮👉🤯",
                        "cha sinh me de ra thang lon hay gi rain🤯🤯🤯😏😞😏😵😘👉🤯☝️🤯😰😄😨",
                        "dit rain😠😠😠😐😍😂😍😞😮😰😅😰😅🥪🍨🥪🥫🍤🍭🍤🥧🍤",
                        "con rain 😓😓😓😄😰😅☝️😄☝️😮👉☝️🤯🤯",
                        "me rain🤯🤯🤯😱🤔🤭😤😱😠😓😤😞🙄",
                        "nha rain😮😮😮😰😅🥰😅👿😅💌😅🥪🍮🥫🍨🥫🍤🥫🍤🥪🍤",
                        "may rain😫😫😫👺🤥👺👻👹👾👺👿🎃👿",
                        "luon rain😞😞😞👂💪👂👁️👣👍👃👊👃💪🤲💪🥪🍨🥪🍨🥪🍤🥪🍤🥪🍤",
                        "ha dit cha m rain😵😵😵✍️✍️🤝🤳💅🤳💅💇🚶🧖🧘🤾🤼",
                        "sao vay thang lon rain🥺🥺🥺🧟🦸🧙💂🧙🤴👩‍🚀💂👩‍🚀🤶👩‍🚀🤶👩‍🚀",
                        "bo me may bi tao dit cho chet roi rain😐😐😐👩‍🎨👶👩‍🎤🧒👧👵👩‍🦰👲👨👲👨👲👨👵",
                        "thang con di me nha may rain 🤩🤩🤩👩‍❤️‍👨👪👨‍👩‍👧‍👧👨‍👩‍👧👨‍👩‍👦‍👦👨‍👨‍👧‍👧👨‍👩‍👧‍👧👪👨‍👩‍👧‍👧👪👨‍👨‍👦",
                        "sao vay thang lon cali😭😭😭🗣️👣🗣️👥🤱👥🤱👤🤱🤱👥",
                        "sua cai deo gi vay em 👹👹👹🌿🥀🌸🥀🌸🍁🌿🍁🍃🍂🍃",
                        "bo dit ca lo nha may rain 😏😏😏🍁🌿🌱🍁🌱🍁🌿🍁🍂🌿🍂🌿🍂",
                        "dit rain 😘😘😘 🏞️🌡️🌋🌡️🌡️🌀🌊⚡🌈⚡🌫️⚡🌫️🏞️🌈🏜️🌈🏜️🌈🏜️",
                        "bo may nhet cac vao mom may rain🦴🦴🦴🌌🌒🌕🌓🌕🌒🌖🌑🌗🌑🌗💫🌍☀️⭐☀️⭐",
                        "me may bi tao dit cho ko con duong song rain🗿🗿🗿🦊🐼🐰🦓🐰🦓🦓🐲🐽🦝🐨🦝🐨",
                        "thang cha con di me ho hang nha may dit ba noi cha dai me nha may con di cac nha may lon ma may dit cha noi nha m dit co di chu bac nha m dit ca tong mon nha m dit ca lon nha m dit di nha may dit nat lon nha may rain 😂😂😂🦝🐼🐰🦓🐴🦓🐲🐗🦊🐗🦊🐼🦊🐼🐴🐨🐰🐨🐯🐨🐯🐨🦊🐨🦊🐨",
                        "dit con dai me nha may rain 😋😋😋🐫🐓🐪🦆🐤🦆🦅🐓🦅🐦🦅🐦🐥🦢🐤",
                        "con di ba nha m rain 🤣🤣🤣🦗🦂🐌🦋🐚🦋🦠🦋🐾🐾🐞🐞🐌🦂🦞🦂🦞",
                        "dit me 3 que sua cai deo gi tao deo hieu rain 😌😌😌🥥🍈🍇🥦🥑🥦🥥🥦🍅🌽🍆🌽🍆🌽🥑🌽",
                        "bo dit ca lo nha m rain 🖕🖕🖕🥘🍛🍝🌮🥪🍕🥫🍕🥡🍲🍤🍲🍣🍛🍣🍛",
                        "thang cha may bi tao chat cu rain 😍😍😍🍡🍦🎂🥧🍮🥧🎂🍦🍭🍨🧁🍨🎂🍨🍮🍦",
                        "lon ma nha may dit cu may rain 🤪🤪🤪🍽️🍵🥄🥢🥢🥄🥢🔪🍶🍽️🍹🍽️🍹🥤🍵🍾",
                        "me may khong the song thieu tinh trung tao rain 🍦🍹🍦🍹🍮🥪🥪🍵🍦🍹😅😄😅😄😂😃🤣😃🤣",
                        "cali cho sua gi the tao deo hieu gi rain 🤤🙃😏🙂😏🤪🤪🤤🤫😬😬🤫😱🤔🥺🤐🤐😋😋😜😋🙂😍🙂🥰🤤",
                        "dit me chung may luon kkkk rain 🥺🤫🥰🤐😜😬🍮🍹🥪🍽️🥫😅🍤😅🔪🍭🍶🥪🥫🍽️🍾😃🍹😃🥺🤫🤐🤫🍮😅",
                        "thang lon cac nha m rain 😜🥪🍾🥪😬🙂😂🙍🧖🚶🚶🤾🧗🤼🤾🤹⛹️🏃⛹️🏃💇🙎🙋🙎🙋🙍💇",
                    ]

                    def send_tagged():
                        try:
                            index = 0
                            while self.auto_chatting:
                                base = spam_list[index]
                                text = base + " @member"
                                mention = Mention(tagged_uid, offset=len(base) + 1, length=8)
                                self.sendMessage(Message(text=text, mention=mention), thread_id, thread_type)
                                index = (index + 1) % len(spam_list)
                                time.sleep(0.1)
                        except Exception as e:
                            self.sendMessage(Message(text=f"➜ Lỗi : {str(e)}"), thread_id, thread_type)
                            self.auto_chatting = False

                    threading.Thread(target=send_tagged, daemon=True).start()

        elif message.startswith(f"{prefix}nhay on"):
            if message.strip() == f"{prefix}nhay off":
                self.auto_chatting = False
                self.sendMessage(Message(text="➜ Đã Dừng Nhây Thành Công !"), thread_id, thread_type)
            else:
                if self.auto_chatting:
                    self.sendMessage(Message(text="➜ Sai Định Dạng Hoặc Lỗi !"), thread_id, thread_type)
                else:
                    self.auto_chatting = True
                    spam_list = [
                        "me m rach ak",
                        "chao ban nho rain👋👋👋🗿😏😋😮😐😮😰😮😰😮😨😮",
                        "dit me nha may rain🖕🖕🖕😰👹😰😮😰😮😰😮😰😮😰😮",
                        "thang con cac nay rain👉☝️😘😞🤪😞😘😵😵😘👉😫👉☝️👋",
                        "dit me con nay bu dai tao gioi lam rain😰😨😅😰😅👿😰😅☝️😅👉😮👉🤯",
                        "cha sinh me de ra thang lon hay gi rain🤯🤯🤯😏😞😏😵😘👉🤯☝️🤯😰😄😨",
                        "dit rain😠😠😠😐😍😂😍😞😮😰😅😰😅🥪🍨🥪🥫🍤🍭🍤🥧🍤",
                        "con rain 😓😓😓😄😰😅☝️😄☝️😮👉☝️🤯🤯",
                        "me rain🤯🤯🤯😱🤔🤭😤😱😠😓😤😞🙄",
                        "nha rain😮😮😮😰😅🥰😅👿😅💌😅🥪🍮🥫🍨🥫🍤🥫🍤🥪🍤",
                        "may rain😫😫😫👺🤥👺👻👹👾👺👿🎃👿",
                        "luon rain😞😞😞👂💪👂👁️👣👍👃👊👃💪🤲💪🥪🍨🥪🍨🥪🍤🥪🍤🥪🍤",
                        "ha dit cha m rain😵😵😵✍️✍️🤝🤳💅🤳💅💇🚶🧖🧘🤾🤼",
                        "sao vay thang lon rain🥺🥺🥺🧟🦸🧙💂🧙🤴👩‍🚀💂👩‍🚀🤶👩‍🚀🤶👩‍🚀",
                        "bo me may bi tao dit cho chet roi rain😐😐😐👩‍🎨👶👩‍🎤🧒👧👵👩‍🦰👲👨👲👨👲👨👵",
                        "thang con di me nha may rain 🤩🤩🤩👩‍❤️‍👨👪👨‍👩‍👧‍👧👨‍👩‍👧👨‍👩‍👦‍👦👨‍👨‍👧‍👧👨‍👩‍👧‍👧👪👨‍👩‍👧‍👧👪👨‍👨‍👦",
                        "sao vay thang lon cali😭😭😭🗣️👣🗣️👥🤱👥🤱👤🤱🤱👥",
                        "sua cai deo gi vay em 👹👹👹🌿🥀🌸🥀🌸🍁🌿🍁🍃🍂🍃",
                        "bo dit ca lo nha may rain 😏😏😏🍁🌿🌱🍁🌱🍁🌿🍁🍂🌿🍂🌿🍂",
                        "dit rain 😘😘😘 🏞️🌡️🌋🌡️🌡️🌀🌊⚡🌈⚡🌫️⚡🌫️🏞️🌈🏜️🌈🏜️🌈🏜️",
                        "bo may nhet cac vao mom may rain🦴🦴🦴🌌🌒🌕🌓🌕🌒🌖🌑🌗🌑🌗💫🌍☀️⭐☀️⭐",
                        "me may bi tao dit cho ko con duong song rain🗿🗿🗿🦊🐼🐰🦓🐰🦓🦓🐲🐽🦝🐨🦝🐨",
                        "thang cha con di me ho hang nha may dit ba noi cha dai me nha may con di cac nha may lon ma may dit cha noi nha m dit co di chu bac nha m dit ca tong mon nha m dit ca lon nha m dit di nha may dit nat lon nha may rain 😂😂😂🦝🐼🐰🦓🐴🦓🐲🐗🦊🐗🦊🐼🦊🐼🐴🐨🐰🐨🐯🐨🐯🐨🦊🐨🦊🐨",
                        "dit con dai me nha may rain 😋😋😋🐫🐓🐪🦆🐤🦆🦅🐓🦅🐦🦅🐦🐥🦢🐤",
                        "con di ba nha m rain 🤣🤣🤣🦗🦂🐌🦋🐚🦋🦠🦋🐾🐾🐞🐞🐌🦂🦞🦂🦞",
                        "dit me 3 que sua cai deo gi tao deo hieu rain 😌😌😌🥥🍈🍇🥦🥑🥦🥥🥦🍅🌽🍆🌽🍆🌽🥑🌽",
                        "bo dit ca lo nha m rain 🖕🖕🖕🥘🍛🍝🌮🥪🍕🥫🍕🥡🍲🍤🍲🍣🍛🍣🍛",
                        "thang cha may bi tao chat cu rain 😍😍😍🍡🍦🎂🥧🍮🥧🎂🍦🍭🍨🧁🍨🎂🍨🍮🍦",
                        "lon ma nha may dit cu may rain 🤪🤪🤪🍽️🍵🥄🥢🥢🥄🥢🔪🍶🍽️🍹🍽️🍹🥤🍵🍾",
                        "me may khong the song thieu tinh trung tao rain 🍦🍹🍦🍹🍮🥪🥪🍵🍦🍹😅😄😅😄😂😃🤣😃🤣",
                        "cali cho sua gi the tao deo hieu gi rain 🤤🙃😏🙂😏🤪🤪🤤🤫😬😬🤫😱🤔🥺🤐🤐😋😋😜😋🙂😍🙂🥰🤤",
                        "dit me chung may luon kkkk rain 🥺🤫🥰🤐😜😬🍮🍹🥪🍽️🥫😅🍤😅🔪🍭🍶🥪🥫🍽️🍾😃🍹😃🥺🤫🤐🤫🍮😅",
                        "thang lon cac nha m rain 😜🥪🍾🥪😬🙂😂🙍🧖🚶🚶🤾🧗🤼🤾🤹⛹️🏃⛹️🏃💇🙎🙋🙎🙋🙍💇",
                    ]
                    self.sendTxt(thread_id, thread_type, spam_list, delay=0.1)
        elif message.startswith(f"{prefix}nhai"):
            arg = message[len(f"{prefix}nhai"):].strip().lower()
            if arg.startswith("off"):
                self.copy_mode = False
                self.copy_target = set()
                self.sendMessage(Message(text="➜ Đã Tắt Chế Độ Nhái"), thread_id, thread_type)
            elif arg.startswith("on"):
                self.copy_mode = True
                self.copy_target = set()
                if message_object.mentions:
                    for m in message_object.mentions:
                        self.copy_target.add(m['uid'])
                self.sendMessage(Message(text="➜ Đã Bật Chế Độ Nhái"), thread_id, thread_type)
            else:
                self.sendMessage(Message(text=f"➜ Sai cú pháp: nhai on/off [@Tag]"), thread_id, thread_type)
        elif message.startswith(f"{prefix}treo on"):
            if message.strip() == f"{prefix}treo off":
                self.auto_chatting = False
                self.sendMessage(Message(text="➜ Đã Dừng Treo Thành Công !"), thread_id, thread_type)
            else:
                if self.auto_chatting:
                    self.sendMessage(Message(text="➜ Sai Định Dạng Hoặc Lỗi !"), thread_id, thread_type)
                else:
                    self.auto_chatting = True
                    treo = """꧁༺ ★彡 亗 𝙏𝙧ầ𝙣 𝙑ă𝙣 𝙃𝙤à𝙣𝙜 𝘽á 𝙎à𝙣 𝙏𝙧𝙚𝙤 亗 ミ★ ༻꧂"""
                    self.sendTxt(thread_id, thread_type, treo, delay=0.1)

        elif message.startswith(f"{prefix}treogr on"):
            if message.strip() == f"{prefix}treogr off":
                self.auto_chatting = False
                self.sendMessage(Message(text="➜ Đã Dừng Treo Nhóm Thành Công !"), thread_id, thread_type)
            else:
                if self.auto_chatting:
                    self.sendMessage(Message(text="➜ Sai Định Dạng Hoặc Lỗi !"), thread_id, thread_type)
                else:
                    def send_treotagall():
                        try:
                            self.auto_chatting = True
                            group_info = self.fetchGroupInfo(thread_id).gridInfoMap[thread_id]
                            thanhvien = group_info.get('memVerList', [])
                            mention_objs = [
                                Mention(userId.split('_')[0], length=1, offset=0, auto_format=False)
                                for userId in thanhvien
                            ]
                            multi = MultiMention(mention_objs)
                            while self.auto_chatting:
                                self.sendMessage(Message(text="""꧁༺ ★彡 亗 𝙏𝙧ầ𝙣 𝙑ă𝙣 𝙃𝙤à𝙣𝙜 𝘽á 𝙎à𝙣 𝙏𝙧𝙚𝙤 亗 ミ★ ༻꧂""", mention=multi), thread_id, thread_type)
                                time.sleep(0.1)
                        except Exception as e:
                            self.sendMessage(Message(text=f"➜ Lỗi : {e}"), thread_id, thread_type)
                            self.auto_chatting = False
                    threading.Thread(target=send_treotagall, daemon=True).start()

        elif message.startswith(f"{prefix}tagall"):
            allowed_uids = [u.strip() for u in uid.split(',') if u.strip()]
            if author_id not in allowed_uids:
                self.replyMessage(Message(text="➜ Lệnh Này Chỉ Khả Thi Với Admin Của Bot !"), message_object, thread_id, thread_type)
                return

            parts = message.strip().split(' ', 1)
            if len(parts) < 2 or not parts[1].strip():
                self.replyMessage(Message(text="➜ 👨‍💻 Hãy Nhập Nội Dung !"), message_object, thread_id, thread_type)
                return
            try:
                cmd = parts[1].strip()
                group_info = self.fetchGroupInfo(thread_id).gridInfoMap[thread_id]
                thanhvien = group_info.get('memVerList', [])
                mention_objs = [
                    Mention(userId.split('_')[0], length=len(cmd), offset=0, auto_format=False)
                    for userId in thanhvien
                ]
                multi = MultiMention(mention_objs)
                self.sendMessage(Message(text=cmd, mention=multi), thread_id, thread_type)
            except Exception as e:
                print(f"\033[1;32m[\033[1;31m♤\033[1;32m] ➩ \033[1;32mLỗi : {e}")

bot = Tool_WarZl("<API_KEY>", "<SECRET_KEY>", imei=imei, session_cookies=cookies)
bot.listen()
