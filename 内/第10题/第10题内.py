import requests
kk = 0
for i in range(1, 101):
    session = requests.session()
    headers = {
        "Host": "www.python-spider.com",
        "Content-Length": "5",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Referer": "https://www.python-spider.com/challenge/10",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }
    cookies = {
        "Hm_lvt_337e99a01a907a08d00bed4a1a52e35d": "1706862741,1708307504",
        "sessionid": "c2yeb0yp2dcg6n3jevxzyfe8mhxwb7bl",
        "no-alert": "true",
        "Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d": "1708329544"
    }
    url = "https://www.python-spider.com/api/challenge10"
    data = {
        "page": i
    }
    session.headers.clear()
    session.headers.update(headers)
    response = session.post(url, cookies=cookies, data=data)

    print(response.text)
    print(response)
    for i in response.json()['data']:
        kk += int(i['value'])
print(kk)