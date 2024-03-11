import requests

kk = 0
for i in range(1, 101):

    headers = {
        "authority": "www.python-spider.com",
        "content-length": "0",
        "pragma": "no-cache",
        "cache-control": "no-cache",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
        "accept": "*/*",
        "origin": "https://www.python-spider.com",
        "sec-fetch-site": "same-origin",

        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://www.python-spider.com/challenge/7",
        "accept-language": "zh-CN,zh;q=0.9"
    }
    cookies = {
        "Hm_lvt_337e99a01a907a08d00bed4a1a52e35d": "1706862741,1708307504",
        "sessionid": "c2yeb0yp2dcg6n3jevxzyfe8mhxwb7bl",
        "no-alert": "true",
        "Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d": "1708314184"
    }
    url = "https://www.python-spider.com/cityjson"
    response = requests.post(url, headers=headers, cookies=cookies)

    print(response.text)
    print(response)

    headers = {
        "authority": "www.python-spider.com",
        "pragma": "no-cache",
        "cache-control": "no-cache",
        "accept": "application/json, text/javascript, */*; q=0.01",
        "x-requested-with": "XMLHttpRequest",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://www.python-spider.com",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://www.python-spider.com/challenge/7",
        "accept-language": "zh-CN,zh;q=0.9"
    }
    cookies = {
        "Hm_lvt_337e99a01a907a08d00bed4a1a52e35d": "1706862741,1708307504",
        "sessionid": "c2yeb0yp2dcg6n3jevxzyfe8mhxwb7bl",
        "no-alert": "true",
        "Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d": "1708314184"
    }
    url = "https://www.python-spider.com/api/challenge7"
    data = {
        "page": i
    }
    response = requests.post(url, headers=headers, cookies=cookies, data=data)

    print(response.text)
    for i in response.json()['data']:
        print(i['value'])
        kk += int(i['value'])
print(kk)
