import json

from util.EncryptData import EncryptData

# 定义json路径
path = r"../../TC_API/json/request.json"
file = open(path, 'r', encoding='utf-8')

password = 'MQ0WINT60DXP7U7R09A70V6Z1SEDIGYH'  # 秘钥
data = json.load(file)  # 需要加密的内容
eg = EncryptData(password)  # 这里**的长度必须是16的倍数
res = eg.encrypt(str(data))
print("密文：" + res)
print("明文：" + eg.decrypt(res))
