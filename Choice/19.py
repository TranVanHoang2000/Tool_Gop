# -*- coding: utf-8 -*-
import os
import aiohttp
import random
import sys
import time
from pystyle import Colors, Colorate
from time import sleep

MAX_CONCURRENT_REQUESTS = 3

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

def print_instructions():
	print (Colorate.Diagonal(Colors.rainbow, "\n╔═════════════════════╗"))
	print (Colorate.Diagonal(Colors.rainbow, "║  Tool Spam Discord  ║"))
	print (Colorate.Diagonal(Colors.rainbow, "╚═════════════════════╝"))
	
	instructions = f"""\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m1\033[1;32m]\033[1;36m Treo Discord
\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m2\033[1;32m]\033[1;36m Nhây (Tag Hoặc Để Trống)
\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m3\033[1;32m]\033[1;36m Nhây Fake Typing 
\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m0\033[1;32m]\033[1;36m Thoát"""


	print(instructions)

def validate_token(token):
    url = "https://discord.com/api/v10/users/@me"
    headers = {"Authorization": token}
    with aiohttp.ClientSession() as session:
        with session.get(url, headers=headers) as response:
            if response.status == 200:
                return True
            else:
                print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mToken Không Hợp Lệ : {token}")
                return False

def load_tokens_from_file(token_file):
    if not os.path.exists(token_file):
        print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mFile {token_file} Không Tồn Tại !")
        return []
    
    with open(token_file, 'r', encoding='utf-8') as file:
        tokens = file.read().splitlines()
        
    if not tokens:
        print(f"File {token_file} chứa token trống.")
    return tokens

def handle_response(response, channel_id, message, token):
    if len(message.splitlines()) > 10:
        message_lines = message.splitlines()
        message = "\n".join(message_lines[:5] + message_lines[-5:])
    
    token_preview = token[:5] + "..." + token[-5:] if len(token) > 10 else token
    message_words = message.split()
    message_preview = " ".join(message_words[:5]) + "..." + " ".join(message_words[-5:]) if len(message_words) > 10 else message
    
    try:
        if response.status == 200:
            print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mToken {token_preview} Đã Gửi Thành Công Tin Nhắn : '{message_preview}' Đến Kênh {channel_id}")
            return 0
        elif response.status == 429:
            retry_after = response.json()
            retry_after_time = retry_after.get("retry_after", 1)
            print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mTạm Dừng {retry_after_time} Giây !")
            return retry_after_time
        elif response.status == 401:
            print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mLỗi Xác Thực : Kiểm Tra Lại Token Cho Kênh {channel_id}")
            return 0
        elif response.status in [500, 502]:
            print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mLỗi Máy Chủ, Thử Lại Sau !")
            return 5
        elif response.status == 408:
            print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mYêu Cầu Timeout, Thử Lại !")
            return 5
        else:
            print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mLỗi {response.status} : {response.text()}")
            return 5
    except Exception as e:
        print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mLỗi Xử Lý Phản Hồi : {e}")
        return 5

def get_valid_input(prompt, valid_func, error_message="Input Không Hợp lệ, Vui Lòng Thử Lại"):
    while True:
        user_input = input(prompt)
        if valid_func(user_input):
            return user_input
        else:
            print(error_message)

def is_valid_delay(input_str):
    try:
        delay = float(input_str)
        if delay <= 0:
            raise ValueError
        return True
    except ValueError:
        return False

def is_valid_number(input_str):
    try:
        float(input_str)
        return True
    except ValueError:
        return False

def is_valid_channel_id(input_str):
    return input_str.isdigit()

def check_file_exists(file_path):
    if not os.path.exists(file_path):
        print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mTệp Tin {file_path} Không Tồn Tại !")
        return False
    return True

def process_tokens(token_files):
    for token_file in token_files:
        if not check_file_exists(token_file):
            continue
        tokens = load_tokens_from_file(token_file)
        if not tokens:
            continue

def handle_token_error(token, error):
    token_preview = token[:5] + "..." + token[-5:] if len(token) > 10 else token
    print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mToken {token_preview} Gặp Lỗi : {str(error)}, Bỏ Qua Token Này Và Tiếp Tục !")

def spam_message(token, channel_id, message, delay, color, semaphore):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    url = f"https://discord.com/api/v10/channels/{channel_id}/messages"
    
    if len(message) > 2000:
        print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mTin Nhắn Dài Hơn 2000 Ký Tự, Sẽ Bị Cắt Bớt !")
        message = message[:2000]
        print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mTin Nhắn Đã Bị Cắt Bớt Xuống 2000 Ký Tự")
    
    with aiohttp.ClientSession() as session:
        while True:
            try:
                with semaphore:
                    with session.post(url, json={"content": message}, headers=headers) as response:
                        retry_after = handle_response(response, channel_id, message, token)
                        
                        if retry_after:
                            print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mChờ {retry_after} Giây Trước Khi Thử Lại !")
                            sleep(retry_after)
                        else:
                            sleep(delay + random.uniform(0.5, 1.5))
            except Exception as e:
                print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mLỗi : {str(e)}")
                sleep(1)
                continue

def spam_message_nhay(token, channel_id, messages, delay, color, mention_user=False, user_ids=[], semaphore=None):
    if len(token) > 10:
        token_preview = token[:5] + "..." + token[-5:]
    else:
        token_preview = token

    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    url = f"https://discord.com/api/v10/channels/{channel_id}/messages"
    
    if user_ids:
        mention_string = " ".join([f"<@{user_id}>" for user_id in user_ids])
    
    with aiohttp.ClientSession() as session:
        while True:
            for message in messages:
                try:
                    with semaphore:
                        if mention_user:
                            message_to_send = f"{mention_string} {message}" if mention_user else message
                        with session.post(url, json={"content": message}, headers=headers) as response:
                            retry_after = handle_response(response, channel_id, message, token)
                            if retry_after:
                                sleep(retry_after)
                            sleep(delay + random.uniform(0.5, 1.5))
                except Exception as e:
                    handle_token_error(token, e)
                    break

def fake_typing_and_send_message(token, channel_id, messages, delay, color, mention_user, user_ids, semaphore):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    url = f"https://discord.com/api/v10/channels/{channel_id}/messages"
    
    mention_string = " ".join([f"<@{user_id}>" for user_id in user_ids]) if mention_user else ""
    
    with aiohttp.ClientSession() as session:
        while True:
            for message in messages:
                typing_url = f"https://discord.com/api/v10/channels/{channel_id}/typing"
                try:
                    with session.post(typing_url, headers=headers):
                        print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐang Soạn Tin Nhắn...")
                    for char in message:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        sleep(0.05)

                    with semaphore:
                        message_to_send = f"{mention_string} {message}" if mention_user else message
                        while True:
                            with session.post(url, json={"content": message_to_send}, headers=headers) as response:
                                retry_after = handle_response(response, channel_id, message, token)
                                if retry_after:
                                    print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐang Chờ {retry_after} Giây Trước Khi Thử Lại...")
                                    sleep(retry_after)
                                else:
                                    break
                    sleep(delay)
                except Exception as e:
                    handle_token_error(token, e)
                    break

def simulate_typing_and_send_message(token, channel_id, messages, delay, color, mention_user, user_ids, semaphore, name_to_call=None):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    url = f"https://discord.com/api/v10/channels/{channel_id}/messages"
    
    mention_string = " ".join([f"<@{user_id}>" for user_id in user_ids]) if mention_user else ""
    
def main():
    banner()
    info()
    print_instructions()

    choice = get_valid_input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số  : \033[1;36m", lambda x: x in ["1", "2", "3", "4"])
    
    token = input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Token : \033[1;36m")
    tokens = [token]

    if not tokens:
        return

    channel_id = get_valid_input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Channel ID : \033[1;36m", is_valid_channel_id)
    delay = float(get_valid_input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Delay Giữa Các Tin Nhắn : \033[1;36m", is_valid_delay))

    color = random.choice(CHANNEL_COLORS)
    semaphore = Semaphore(MAX_CONCURRENT_REQUESTS)

    if choice == "1":
        message = input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Nội Dung Tin Nhắn : \033[1;36m")
        gather(*[
            spam_message(token, channel_id, message, delay, color, semaphore)
            for token in tokens
        ])

    elif choice == "2":
        messages_file = input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập File Chứa Các Dòng Tin Nhắn (Ví Dụ : messages.txt) : \033[1;36m")
        if not os.path.exists(messages_file):
            print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mFile {messages_file} Không Tồn Tại")
            return
        with open(messages_file, 'r', encoding='utf-8') as f:
            messages = f.read().splitlines()

        mention_user = get_valid_input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mBạn Có Muốn Tag User Không ? (y/n) : \033[1;36m ", lambda x: x.lower() in ['y', 'n']) == "y"
        user_ids = input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập user_id Để Tag (Cách Nhau Bằng Dấu Phẩy) : \033[1;36m").split(",") if mention_user else []

        gather(*[
            spam_message_nhay(token, channel_id, messages, delay, color, mention_user, user_ids, semaphore)
            for token in tokens
        ])

    elif choice == "3":
        messages_file = input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập File Chứa Các Dòng Tin Nhắn : \033[1;36m")
        if not os.path.exists(messages_file):
            print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mFile {messages_file} Không Tồn Tại")
            return
        with open(messages_file, 'r', encoding='utf-8') as f:
            messages = f.read().splitlines()

        mention_user = get_valid_input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mBạn Có Muốn Tag User Không ? (y/n) : \033[1;36m", lambda x: x.lower() in ['y', 'n']) == "y"
        user_ids = input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập user_id Để Tag (Cách Nhau Bằng Dấu Phẩy) : \033[1;36m").split(",") if mention_user else []

        gather(*[
            fake_typing_and_send_message(token, channel_id, messages, delay, color, mention_user, user_ids, semaphore)
            for token in tokens
        ])

    elif choice == "0":
        print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mCảm Ơn Bạn Đã Tin Tưởng Và Sử Dụng Tool, Chúc Bạn May Mắn !")
        sys.exit()

if __name__ == "__main__":
    main()