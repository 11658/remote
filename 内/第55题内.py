from base64 import b64decode
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad

# 定义密钥（假设密钥是16字节，对于AES-128）
KEY = b'aiding6666666666'

# 假设str是已经Base64编码过的密文，先解码
encoded_ciphertext = b"2A4w0jqbUivhDV042Ka+VbfXmH65wRwPgKTNHCnEW2hkVTAx4LzvekaBzGEikZHegf/SkmYIElLIwA4+XHzPtZvUhytE+X+F5z8txWCUrGElE3bYgT8P10ImYGVNtjiwlJDs3yvXsAkYP8o8RlX8+sc08m/s51+5/RLtBR4MrNtDRtBU0SAGafMIYXXHazvr7B4oUP5SQ8AhZe8gmN0V8SJV0Bk9oGTSNT9a5zOhFJg/2ym+5xjCWMqchNjSwJ+Z1GMz0K1vnE0viFBK0SnqyrQxDZ1vk9wo1t0nnB0OMd6Sh1VuT402fnOj3sjC++nyX2geck9FbakfoKX+qVxbqA=="  # 确保这是一个bytes对象
try:
    str_bytes = b64decode(encoded_ciphertext)
except Exception as e:
    print(f"Base64解码失败: {e}")
else:
    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        decrypted_bytes = cipher.decrypt(str_bytes)
    except ValueError as e:
        print(f"AES解密失败: {e}")
    else:
        # 去除PKCS7填充
        try:
            plaintext = unpad(decrypted_bytes, AES.block_size)
        except ValueError as e:
            print(f"PKCS7解填充失败: {e}")
        else:
            print(plaintext.decode('utf-8'))