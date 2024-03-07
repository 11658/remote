import requests

import urllib3

urllib3.disable_warnings()

session = requests.Session()
url = 'https://www.python-spider.com/challenge/7'

headers = {
    'Content-Length': '6',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Origin': 'https://www.python-spider.com',
    'Referer': 'https://www.python-spider.com/challenge/10',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}
cookies = {
    'sessionid': 'bxi2hyvitjzkwf08n8repsyqwuma32o4'
}
proxies = {
    'http': 'http://127.0.0.1:8888',
    'https': 'http://127.0.0.1:8888'
}
session.headers.clear()
session.headers.update(headers)
kk = 0
for i in range(1, 101):
    data = {
        'page': i
    }
    response = session.post('https://www.python-spider.com/api/challenge6', headers=headers, cookies=cookies,
                            verify=False, proxies=proxies, data=data)
    print(response.text)
    for i in response.json()['data']:
        kk += int(i['value'])
print(kk)
