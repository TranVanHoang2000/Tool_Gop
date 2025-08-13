import os, base64, sys, time
from pprint import pformat
from pystyle import Colors, Colorate
from time import sleep

alphabet = [
    "\U0001f600",
    "\U0001f603",
    "\U0001f604",
    "\U0001f601",
    "\U0001f605",
    "\U0001f923",
    "\U0001f602",
    "\U0001f609",
    "\U0001f60A",
    "\U0001f61b",
]

MAX_STR_LEN = 70
OFFSET = 10

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
        
def slowprint(n):
    for word in n + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.000001)

def sprint(n):
    for word in n + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.00002)

def choice():
    os.system("cls" if os.name == "nt" else "clear")
    banner()
    info()

    print('\n\033[1;32m[♤] ➩ \033[1;32mNhập Số [1] Trở Về Menu')
    print('\033[1;32m[♤] ➩ \033[1;32mNhập Số [2] Thoát')
    
    ret = input("\033[1;32m[♤] ➩ \033[1;32mNhập Số : \033[1;36m")

    if ret == "1":
        main()
    elif ret == "2":
        exit()
    else:
        exit()

def mover(out_file):
    move= input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mBạn Có Muốn Move File Không ? (y/n) : \033[1;36m")
    if move=="y":
        mpath=input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Đường Dẫn Chứa Cần Chứa (Ví Dụ : /sdcard/download/...) : \033[1;36m")
        if os.path.exists(mpath):
            os.system("mv -f '"+out_file+"' '"+mpath+"'")
            sprint(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mMoved To {mpath}\n")
            exit()
        else:
            sprint("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mĐường Dẫn Không Hợp Lệ !\n")
            exit()
    else:
        print("\n")
        exit()
    exit()

def obfuscate(VARIABLE_NAME, file_content):
    b64_content = base64.b64encode(file_content.encode()).decode()
    index = 0
    code = f'{VARIABLE_NAME} = ""\n'
    for _ in range(int(len(b64_content) / OFFSET) + 1):
        _str = ''
        for char in b64_content[index:index + OFFSET]:
            byte = str(hex(ord(char)))[2:]
            if len(byte) < 2:
                byte = '0' + byte
            _str += '\\x' + str(byte)
        code += f'{VARIABLE_NAME} += "{_str}"\n'
        index += OFFSET
    code += f'exec(__import__("\\x62\\x61\\x73\\x65\\x36\\x34").b64decode({VARIABLE_NAME}.encode("Encode_TVH")).decode("TranVanHoang"))'
    return code

def chunk_string(in_s, n):
    return "\n".join(
        "{}\\".format(in_s[i : i + n]) for i in range(0, len(in_s), n)
    ).rstrip("\\")

def encode_string(in_s, alphabet):
    d1 = dict(enumerate(alphabet))
    d2 = {v: k for k, v in d1.items()}
    return (
        'exec("".join(map(chr,[int("".join(str({}[i]) for i in x.split())) for x in\n'
        '"{}"\n.split("  ")])))\n'.format(
            pformat(d2),
            chunk_string(
                "  ".join(" ".join(d1[int(i)] for i in str(ord(c))) for c in in_s),
                MAX_STR_LEN,
            ),
        )
    )

def encryptsh():
    in_file = input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập File Cần Encode : \033[1;36m")
    if not os.path.exists(in_file):
        sprint('\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mFile Không Tồn Tại !')
        sleep(2)
        encryptsh()
    os.system("bash-obfuscate " + in_file + " -o .temp")
    if not os.path.exists(".temp"):
        try:
            sprint("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐang Cài Đặt Bash-Obfuscate....\n")
            os.system("apt install nodejs -y && npm install -g bash-obfuscate")
            os.system("bash-obfuscate " + in_file + " -o .temp")
        except:
            sprint("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mCài Đặt Bash-Obfuscate Không Thành Công, Hãy Copy Đoạn Này Và Cài Đặt Lại :\n••> apt install nodejs -y && npm install -g bash-obfuscate")
            exit(1)
    out_file= input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Tên File Đã Encode : \033[1;36m")
    with open(".temp",'r') as temp_f, open(out_file,'w') as out_f:
        filedata = temp_f.read()
        out_f.write("# Copyright : Trần Văn Hoàng\n# Tác Giả : TVH Tool\n# Youtuber : Trần Văn Hoàng\n# Do Not Retup\n\n"+filedata)
    os.remove(".temp")
    sprint(" \033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐã Lưu Ở " + out_file)
    mover(out_file)

def decryptsh():
    in_file = input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập File Cần Encode : \033[1;36m")
    if not os.path.exists(in_file):
        print('\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mFile Không Tồn Tại !')
        sleep(2)
        decryptsh()
    with open(in_file,'r') as in_f, open(".temp1",'w') as temp_f:
        filedata = in_f.read()
        if not (filedata.find("eval") != -1):
            sprint("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mCannot Be Decrypted !")
            exit()
        newdata = filedata.replace("eval","echo")
        temp_f.write(newdata)
    out_file = input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Tên File Đã Mã Hóa : \033[1;36m")
    os.system("bash .temp1 > .temp2")
    os.remove(".temp1")
    with open(".temp2",'r') as temp_f2, open(out_file,'w') as out_f:
        filedata = temp_f2.read()
        out_f.write("# Copyright : Trần Văn Hoàng\n# Tác Giả : TVH Tool\n# Youtuber : Trần Văn Hoàng\n# Do Not Retup\n\n"+filedata)
    os.remove(".temp2")
    sprint(" \033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐã Lưu Ở " + out_file)
    mover(out_file)

def encryptvar():
    var= 'HAMII/:P/:)/;*/;*'
    if (var==""):
        sprint("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mNo Variable")
        os.system("sleep 3")
        encryptvar()
    if (var.find(" ")!= -1):
        sprint("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mOnly One Word !")
        os.system("sleep 3")
        encryptvar()

    VARIABLE_NAME = var * 100
    in_file = input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập File Cần Encode : \033[1;36m")

    if not os.path.isfile(in_file):
        print('\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mFile Không Tồn Tại')
        sleep(2)
        encryptvar()
    out_file = input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Tên File Đã Encode : \033[1;36m")
    with open(in_file, 'r', encoding='utf-8', errors='ignore') as in_f,open(out_file, 'w') as out_f:
       file_content = in_f.read()
       obfuscated_content = obfuscate(VARIABLE_NAME, file_content)
       out_f.write("# Copyright : Trần Văn Hoàng\n# Tác Giả : TVH Tool\n# Youtuber : Trần Văn Hoàng\n# Do Not Retup\n\n"+obfuscated_content)
    sprint(" \033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐã Lưu Ở " + out_file)
    mover(out_file)

def encryptem():
    in_file = input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Tên File Cần Encode : \033[1;36m")
    if not os.path.isfile(in_file):
        sprint("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mFile Không Tồn Tại !")
        time.sleep(2)
        encryptem()
    out_file = input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Tên File Đã Encode : \033[1;36m")
    with open(in_file, encoding="utf-8") as in_f, open(out_file, "w", encoding="utf-8") as out_f:
        out_f.write("# Copyright : Trần Văn Hoàng\n# Tác Giả : TVH Tool\n# Youtuber : Trần Văn Hoàng\n# Do Not Retup\n\n")
        out_f.write(encode_string(in_f.read(), alphabet))
    sprint(" \033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐã Lưu Ở " + out_file)
    mover(out_file)

def main():
    os.system("cls" if os.name == "nt" else "clear")
    banner()
    info()
    
    print('\n\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m1\033[1;32m]\033[1;36m Encode Bash/Shell')
    print('\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m2\033[1;32m]\033[1;36m Decode Bash/Shell')
    print('\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m3\033[1;32m]\033[1;36m Encode Python Into Variable')
    print('\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m4\033[1;32m]\033[1;36m Encode Python Into Emoji')
    print('\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m0\033[1;32m]\033[1;36m Thoát')
    
    while True:
        choose = input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số : \033[1;36m")
        if choose == "1" or choose == "01":
            encryptsh()
        elif choose == "2" or choose == "02":
            decryptsh()
        elif choose == "3" or choose == "03":
            encryptvar()
        elif choose == "4" or choose == "04":
            encryptem()
        elif choose == "0":
            exit()
        else:
            sprint('\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mĐầu Vào Không Hợp Lệ !')
            sleep(2)
            continue

try:
    main()
except KeyboardInterrupt:
    print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mCảm Ơn Bạn Đã Tin Tưởng Và Sử Dụng Tool, Chúc Bạn May Mắn !")
    exit()
except Exception as e:
    sprint(str(e))