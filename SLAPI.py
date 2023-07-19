from redisbloom.client import Client as RedisBloomClient

from demo.decrypt import decrypt
from demo.falldata import falldata
from demo.miyao import TCSLKEY
from demo.miyao import lastid
from demo.newlastid import newlastid
from demo.zhua import getAPI

# 创建redis_client
redis_client = RedisBloomClient(host='localhost', port=6379, db=0)
for i in range(500):
    # 获取数据时间段
    beginTime = "2023-01-01 00:00:00"
    endTime = "2027-07-11 23:59:59"

    # 调用 TCSLKEY 函数，取最后一个lastid 参数，拼JSON加密串
    lastid_value = lastid()
    print("最后一个ID：" + str(lastid_value))
    encrypted_data = TCSLKEY(beginTime, endTime, lastid_value)
    print(encrypted_data)
    # 抓数据
    getAPI(encrypted_data)

    # 解密
    decrypt()

    # 落库
    falldata()

    # 更新lastid到参数中，用于下一次请求
    newlastid()
    print("循环次数:", i + 1)
