import os
import sys
import time
import requests
from collections import deque
from random import shuffle, choice
from time import sleep
from pystyle import Colors, Colorate

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

class EscapeMasterTool:
    def __init__(self):
        self.lich_su_phong = deque(maxlen=10)
        self.tong_loi = 0
        self.tool_running = True
        self.vong_choi = None
        self.chuoi_thang = 0
        self.count_thang = 0
        self.count_thua = 0
        self.number_cuoc = 0
        self.colors = []
        self.current_time = int(time.time() * 1000)
        self.nhap_cau_hinh()
        self.so_du_ban_dau = 0
        self.headers = {
            "user-id": self.user_id,
            "user-login": self.user_login,
            "user-secret-key": self.user_secret_key
        }
        self.url = f"https://user.3games.io/user/regist?is_cwallet=1&is_mission_setting=true&version=&time={self.current_time}"
        self.api_10_van = f"https://api.escapemaster.net/escape_game/recent_10_issues?asset=BUILD"
        self.api_cuoc = "https://api.escapemaster.net/escape_game/bet"
        
    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def nhap_cau_hinh(self):
        self.user_id = input("\n\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Id : \033[1;36m")
        self.user_login = input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập User_Login (Mặc Định : login_v2) : \033[1;36m") or "login_v2"
        self.user_secret_key = input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Secret Key : \033[1;36m")
        self.amount = int(input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số Tiền Cược Ban Đầu (Bé Nhất Là 1) : \033[1;36m"))
        self.cuoc_ban_dau = self.amount
        print (Colorate.Diagonal(Colors.blue_to_green, "══════════════════════════════════════════════════════════════"))
        sl = input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mBật Stop Loss ? (y/n) : \033[1;36m").lower()
        self.stop_loss_enabled = sl == 'y'
        if self.stop_loss_enabled:
            self.stop_loss_amount = int(input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số Build Cần Dừng Khi Bị Lỗ : \033[1;36m"))
            self.take_profit_amount = int(input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số Build Cần Dừng Khi Đã Lời : \033[1;36m"))
        print (Colorate.Diagonal(Colors.blue_to_green, "══════════════════════════════════════════════════════════════"))
        custom = input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mTùy Chỉnh Hệ Số Gấp ? (y/n) : \033[1;36m").lower()
        if custom == 'y':
            self.multiplier_1 = float(input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mHệ Số Lần 1 (Ví Dụ : 15) : \033[1;36m"))
            self.multiplier_2 = float(input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mHệ Số Lần 2 (Ví Dụ : 20) : \033[1;36m"))
            self.multiplier_3 = float(input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mHệ Số Lần 3 (Ví Dụ : 15) : \033[1;36m"))
        else:
            self.multiplier_1 = 15
            self.multiplier_2 = 20
            self.multiplier_3 = 15

    def login(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            if response.status_code == 200:
                data = response.json()
                if data.get("code") == 200:
                    username = data["data"]["username"]
                    self.so_du_ban_dau = round(data["data"]["cwallet"]["ctoken_contribute"])
                    print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mTên : \033[1;36m{username}")
                    print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mSố Dư : \033[1;36m{self.so_du_ban_dau} Build")
                else:
                    print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mĐăng Nhập Không Thành Công Do Id Hoặc Secret Sai !")
                    self.tool_running = False
            else:
                print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mLỗi Mạng")
        except:
            print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mLỗi Không Xác Định")

    def tong_loi_lo(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            if response.status_code == 200:
                data = response.json()
                if data.get("code") == 200:
                    ctoken = round(data["data"]["cwallet"]["ctoken_contribute"])
                    loi_lo = ctoken - self.so_du_ban_dau
                    print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mTổng Lời/Lỗ Hiện Tại : {loi_lo} Build")
                    if self.stop_loss_enabled:    
                        if loi_lo <= -self.stop_loss_amount:    
                            print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐạt Stop Loss : {loi_lo} Build, Dừng Tool !")    
                            self.tool_running = False    
                        elif loi_lo >= self.take_profit_amount:    
                            print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐạt Fake Profit : {loi_lo} , Dừng Tool !")    
                            self.tool_running = False    
        except:    
            print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mLỗi Không Xác Định")

    def lich_su(self):
        try:
            response = requests.get(self.api_10_van, headers=self.headers)
            if response.status_code == 200:
                data = response.json()
                if data.get("code") == 0:
                    issues = data.get("data", [])[:3]
                    vong_truoc = issues[0]["issue_id"]
                    room_id = issues[0]["killed_room_id"]
                    vong_hien_tai = vong_truoc + 1
                    room_mapping = {
                        1: "Nhà Kho", 2: "Phòng Họp", 3: "Phòng Giám Đốc",
                        4: "Phòng Trò Chuyện", 5: "Phòng Giám Sát", 6: "Văn Phòng",
                        7: "Phòng Tài Vụ", 8: "Phòng Nhân Sự"
                    }
                    ten_phong = room_mapping.get(room_id, "Không Xác Định")
                    issue_details = []
                    for issue in issues:
                        id = issue["issue_id"]
                        room = issue["killed_room_id"]
                        ten = room_mapping.get(room, "Không Xác Định")
                        issue_details.append(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mIssue Id : {id}, Room : {ten}")
                    if vong_truoc != self.vong_choi:
                        print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mVòng Hiện Tại : {vong_hien_tai}")
                        print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mKết Quả Vòng Trước : {vong_truoc} | {ten_phong}")
                        self.vong_choi = vong_truoc
                        self.kiem_tra_dieu_kien(issue_details)
        except Exception as e:
            print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mLỗi : {e}")

    def tinh_ty_le_phong(self):
        if not self.lich_su_phong:
            return {}
        weights, wins, total = {}, {}, {}
        for i, (room, dinh) in enumerate(reversed(self.lich_su_phong)):
            weight = 1 - (i / len(self.lich_su_phong))
            total[room] = total.get(room, 0) + weight
            if dinh:
                wins[room] = wins.get(room, 0) + weight
        return {room: round(wins.get(room, 0) / total[room] * 100, 1) for room in total}
        
    def dat_cuoc(self, room_id):
        body = {
            "asset_type": "BUILD",
            "bet_amount": self.amount,
            "room_id": room_id,
            "user_id": self.user_id
        }
        try:
            res = requests.post(self.api_cuoc, headers=self.headers, json=body)
            if res.status_code == 200:
                print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mCược Thành Công {self.amount} Build")
            else:
                print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mLỗi Cược : ", res.status_code)
        except Exception as e:
            print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mLỗi Cược : {e}")

    def kiem_tra_dieu_kien(self, issue_details):
        room_mapping = {
            "Nhà Kho": 1, "Phòng Họp": 2, "Phòng Giám Đốc": 3,
            "Phòng Trò Chuyện": 4, "Phòng Giám Sát": 5,
            "Văn Phòng": 6, "Phòng Tài Vụ": 7, "Phòng Nhân Sự": 8
        }
        try:
            room_0 = issue_details[0].split(",")[1].split(":")[1].strip()
            room_1 = issue_details[1].split(",")[1].split(":")[1].strip()
            room_2 = issue_details[2].split(",")[1].split(":")[1].strip()
        except:
            print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mLỗi Đọc Dữ Liệu Phòng")
            return
        dinh = (room_0 == room_2)
        self.lich_su_phong.append((room_0, dinh))
        if len(self.lich_su_phong) > 20:
            self.lich_su_phong.pop(0)
        tile = self.tinh_ty_le_phong()
        for k, v in tile.items():
            print(f"{k}: {v}%")
        phong_da_dinh = [phong for phong, trung in self.lich_su_phong[-5:] if trung]
        phong_an_toan = sorted(tile.items(), key=lambda x: x[1])
        room_name = room_id = None
        shuffle(phong_an_toan)
        for ten_phong, _ in phong_an_toan:
            if ten_phong in room_mapping and ten_phong != room_0 and ten_phong not in phong_da_dinh:
                room_name = ten_phong
                room_id = room_mapping[ten_phong]
                break
        if not room_id:
            for ten_phong, _ in phong_an_toan:
                if ten_phong in room_mapping and ten_phong != room_0:
                    room_name = ten_phong
                    room_id = room_mapping[ten_phong]
                    break
        if not room_id:
            room_name = room_1
            room_id = room_mapping.get(room_name)
        print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mChọn Phòng : \033[1;36m{room_name}")
        if self.number_cuoc == 0:
            self.dat_cuoc(room_id)
            self.number_cuoc = 1
            return
        thang = room_0 != room_2
        if thang:
            print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mThắng !")
            self.count_thang += 1
            self.chuoi_thang += 1
            self.tong_loi += self.amount
            self.amount = self.cuoc_ban_dau
            self.tong_loi_lo()
            self.dat_cuoc(room_id)
            self.number_cuoc = 1
        else:
            print("Thua !")
            self.count_thua += 1
            self.chuoi_thang = 0
            self.tong_loi -= self.amount
            self.tong_loi_lo()
            if not self.tool_running:
                return
            if self.number_cuoc == 1:
                self.amount = int(self.amount * self.multiplier_1)
                self.number_cuoc = 2
            elif self.number_cuoc == 2:
                self.amount = int(self.amount * self.multiplier_2)
                self.number_cuoc = 3
            elif self.number_cuoc == 3:
                self.amount = int(self.amount * self.multiplier_3)
                self.number_cuoc = 4
            else:
                print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mGấp Cược Tối Đa, Reset")
                self.amount = self.cuoc_ban_dau
                self.number_cuoc = 1
            self.dat_cuoc(room_id)

    def run(self):
        self.clear_screen()
        print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mSố Tiền Cược Ban Đầu : \033[1;36m{self.cuoc_ban_dau}")
        if self.stop_loss_enabled:
            print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mStop Loss : -{self.stop_loss_amount} | Take Profit : +{self.take_profit_amount}")
        else:
            print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mStop Loss/Take Profit = Tắt")
        print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mHệ Số Gấp : x{self.multiplier_1}, x{self.multiplier_2}, x{self.multiplier_3}")
        self.login()
        try:
            while self.tool_running:
                self.lich_su()
                if not self.tool_running:
                    print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mTool đã dừng do Stop Loss / Take Profit.")
                    break
                time.sleep(15)
        except KeyboardInterrupt:
            print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mCảm Ơn Bạn Đã Tin Tưởng Và Sử Dụng Tool, Chúc Bạn May Mắn !")

if __name__ == "__main__":
    tool = EscapeMasterTool()
    tool.run()