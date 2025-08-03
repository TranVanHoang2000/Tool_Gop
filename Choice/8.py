import requests

umbala = input("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Link Cần Lấy ID : \033[1;36m")

headers = {
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-arch': '""',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'sec-ch-ua-full-version': '"124.0.6327.4"',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'sec-ch-ua-platform-version': '"8.1.0"',
    'Referer': 'https://id.traodoisub.com/',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-bitness': '""',
    'sec-ch-ua-model': '"CPH1803"',
    'sec-ch-ua-platform': '"Android"',
}

data = {
    'link': umbala,
}

response = requests.post('https://id.traodoisub.com/api.php', headers=headers, data=data)

if response.status_code == 200:
    response_json = response.json()
    if 'id' in response_json:
        print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mID Của Bạn Là : \033[1;36m", response_json['id'])
    else:
        print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mKhông Tìm Thấy ID")
else:
    print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mThành Công", response.status_code)