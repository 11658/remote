import requests


headers = {
    "authority": "match.yuanrenxue.cn",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://match.yuanrenxue.cn/match/13",
    "sec-ch-ua": "^\\^Not_A",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\\^Windows^^",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
}
cookies = {
    "Hm_lvt_c99546cf032aaa5a679230de9a95c7db": "1703662678",
    "tk": "-4362083381884593083",
    "sessionid": "ttwz30l97qxrnlspkn5myypmurqanh2",
    "qpfccr": "true",
    "no-alert3": "true",
    "Hm_lvt_9bcbda9cbf86757998a2339a0437208e": "1703662719",
    "Hm_lpvt_9bcbda9cbf86757998a2339a0437208e": "1703670850",
    "yuanrenxue_cookie": "1703670867^|wzsyyNUkSiWUUlrCKADcEBDXNBmlT9L2BjZhLRe34n3u2jKD5dBZHRKF4cS",
    "Hm_lpvt_c99546cf032aaa5a679230de9a95c7db": "1703670869"
}
url = "https://match.yuanrenxue.cn/match/13"
response = requests.get(url, headers=headers, cookies=cookies)
print("Headers:", response.cookies.get("sessionid"))
print(response.text)
hhh = response.cookies.get("sessionid")





for i in range(1, 10):
    import requests
    # print(i)
    url1 = "https://match.yuanrenxue.cn/api/match/13?page=5"

    querystring1 = {"page": "5"}

    headers1 = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "no-cache",
        "Cookie": f"Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1703662678; tk=-4362083381884593083; sessionid={hhh}; qpfccr=true; no-alert3=true; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1703662719; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1703670850; yuanrenxue_cookie=1703672014|hpNzUNxwLJfvlagFncRvRML5SPjs6l8MaFuEMldC; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1703672016",
        "Pragma": "no-cache",
        "Referer": "https://match.yuanrenxue.cn/match/13",
        "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
        "X-Requested-With": "XMLHttpRequest"
    }

    response = requests.request("GET", url1, headers=headers1)

    print(response.text)
