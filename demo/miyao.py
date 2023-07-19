import os

import json
from util.EncryptData import EncryptData


def TCSLKEY(beginTime, endTime, lastid):
    # 获取当前脚本所在目录的绝对路径
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # 构建相对于当前目录的文件路径
    path = os.path.join(current_directory, "json/request.json")
    file = open(path, 'r', encoding='utf-8')

    password = 'MQ0WINT60DXP7U7R09A70V6Z1SEDIGYH'  # 秘钥
    data = json.load(file)  # 需要加密的内容

    # 更新数据中的 beginTime、endTime 和 lastid
    data['beginTime'] = beginTime
    data['endTime'] = endTime
    data['lastid'] = data['lastid']  # 将 data.json 中的 lastid 值赋给 lastid 参数

    eg = EncryptData(password)  # 这里**的长度必须是16的倍数
    res = eg.encrypt(json.dumps(data))
    return res


def lastid():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_directory, "json/request.json")
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        lastid_value = data['lastid']
    return lastid_value
