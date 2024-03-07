import base64
import json

import requests


headers = {
    "authority": "match.yuanrenxue.cn",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://match.yuanrenxue.cn/match/12",
    "sec-ch-ua": "^\\^Not_A",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\\^Windows^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    "x-requested-with": "XMLHttpRequest"
}
cookies = {
    "Hm_lvt_c99546cf032aaa5a679230de9a95c7db": "1703662678",
    "tk": "-4362083381884593083",
    "sessionid": "ttwz30l97qxrnlspkn5myypmuorqanh1",
    "qpfccr": "true",
    "no-alert3": "true",
    "Hm_lvt_9bcbda9cbf86757998a2339a0437208e": "1703662719",
    "Hm_lpvt_9bcbda9cbf86757998a2339a0437208e": "1703670425",
    "Hm_lpvt_c99546cf032aaa5a679230de9a95c7db": "1703670457"
}
url = "https://match.yuanrenxue.cn/api/match/12"
dun_=0
for i in range(1, 6):
    input_string = 'yuanrenxue'+f'{i}'

    # 将字符串编码为 bytes 对象
    input_bytes = input_string.encode('utf-8')

    # 使用 base64 编码
    encoded_bytes = base64.b64encode(input_bytes)

    # 将 bytes 对象解码为字符串
    encoded_string = encoded_bytes.decode('utf-8')
    params = {
        "page": i,
        "m": encoded_string
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    print(response.text)
    data = json.loads(response.text)
    sum_of_values = sum(item["value"] for item in data["data"])

    print("和:", sum_of_values)
    dun_ += sum_of_values
print("平均值:", dun_ )