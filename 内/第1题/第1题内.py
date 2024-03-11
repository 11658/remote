import base64
import hashlib
import time
import requests
timestamp = str(int(time.time()))
print(timestamp)

base_timestamp = base64.b64encode(("9622" + timestamp).encode()).decode()

print(base_timestamp)
# hex_md5
md5_hash = hashlib.md5(base_timestamp.encode()).hexdigest()
print(md5_hash)
kk = 0
for j in range(1, 101):
    headers = {
        "authority": "www.python-spider.com",
        "accept": "application/json, text/javascript, */*; q=0.01",
        "timestamp": timestamp,
        "x-requested-with": "XMLHttpRequest",
        "safe": md5_hash,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://www.python-spider.com",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://www.python-spider.com/challenge/1",
        "accept-language": "zh-CN,zh;q=0.9",
        "cookie": "no-alert=true; Hm_lvt_337e99a01a907a08d00bed4a1a52e35d=1706862741; sessionid=j187woyb42uwkfym2rimsyyooneloa0m; Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d=1708242770"}

    data = {
        "page": j,
    }
    url = "https://www.python-spider.com/api/challenge1"
    reques = requests.post(url, headers=headers, data=data)
    print(reques.json())
    #循环data

    for i in reques.json()['data']:
        print(i['value'])
        kk += int(i['value'])
print(kk)