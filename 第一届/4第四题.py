import base64
import hashlib
import base64
import re

import ddddocr
from PIL import Image
from io import BytesIO
import pytesseract
import bs4
import requests
import ddddocr
sum_=0
def summ(data_2):
    global sum_
    for sublist in data_2:
        sorted_data = sorted(sublist, key=lambda x: x[0])

        result = ''.join(sublist[1] for sublist in sorted_data)
        sum_ += int(result)
def md5_hash(text):
    # 创建 MD5 对象
    md5 = hashlib.md5()

    # 更新对象的状态，以便添加文本
    md5.update(text.encode('utf-8'))

    # 获取加密结果
    hashed_text = md5.hexdigest()

    return hashed_text


headers = {
    "authority": "match.yuanrenxue.cn",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://match.yuanrenxue.cn/match/4",
    "accept-language": "zh-CN,zh;q=0.9"
}
cookies = {
    "sessionid": "wjaomjqth34llbjnuj5vt8t98d20iiym",
    "Hm_lvt_9bcbda9cbf86757998a2339a0437208e": "1703641633",
    "Hm_lvt_c99546cf032aaa5a679230de9a95c7db": "1703641633",
    "no-alert3": "true",
    "m": "8cc5454df1ce1802bd07fa3bc208db4a^|1703649597000",
    "Hm_lpvt_9bcbda9cbf86757998a2339a0437208e": "1703654262",
    "Hm_lpvt_c99546cf032aaa5a679230de9a95c7db": "1703654265"
}
url = "https://match.yuanrenxue.cn/api/match/4"
list_1 = []
for i in range(1, 6):

    params = {
        "page": i
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    # print(response.text)
    json_data = response.json()
    soup = bs4.BeautifulSoup(json_data['info'], 'html.parser')
    input_string = json_data['key'] + json_data['value']

    # 将字符串编码为 bytes 对象
    input_bytes = input_string.encode('utf-8')

    # 使用 base64 编码
    encoded_bytes = base64.b64encode(input_bytes)

    # 将 bytes 对象解码为字符串
    encoded_string = encoded_bytes.decode('utf-8').replace('=', '')

    # print(encoded_string)

    # 要加密的字符串
    input_text = encoded_string

    # 获取 MD5 加密后的结果
    hashed_result = md5_hash(input_text)
    print('.' + hashed_result)
    # 提取所有的 <td> 元素
    # print(soup)
    td_elements = soup.find_all('td')

    # 循环输出每个 <td> 元素的文本内容
    list_ = []
    for td in td_elements:
        # 提取当前 <td> 元素下的所有 <img> 元素
        img_elements = td.find_all('img')

        # 循环遍历每个 <img> 元素并输出其 class 属性值
        shuzi = []
        i = 0
        for img in img_elements:
            img_class = img.get('class')
            if hashed_result in img_class:
                continue
            else:
                i += 11.5
                # 假设 img_data 包含 Base64 编码的图片数据
                img_data = img.get('src')
                img_style = img.get('style')
                match = re.search(r'left:(-?\d+(\.\d+)?)px', img_style)
                print(match.group(1))
                left_value = float(match.group(1))

                # 从 Base64 解码图片数据
                image_bytes = base64.b64decode(img_data.split(',')[1])

                # 使用 PIL 打开图像
                ocr = ddddocr.DdddOcr(show_ad=False)
                image = Image.open(BytesIO(image_bytes))
                res = ocr.classification(image)
                shuzi.append([left_value + i,res])

        list_.append(shuzi)
    summ(list_)
print(sum_)