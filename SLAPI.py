import redis
from redisbloom.client import Client

from demo.decrypt import decrypt
from demo.fall_into_database import falldata
from demo.request_api import get_data_through_api
from demo.update_last_id import get_last_id_in_local_file
from demo.update_last_id import update_last_id
from demo.update_latest_id import update_latest_id

# 创建 Redis 客户端
redis_client = redis.Redis(host='localhost', port=6379, db=0)

# 创建 RedisBloom 客户端
bloom_client = Client(redis_client)

# key
key = 'id_name'

# 创建布隆过滤器
bloom_client.bfCreate(key, errorRate=0.01, capacity=10000)

for i in range(500):
    # 获取数据时间段
    begin_time = "2023-01-01 00:00:00"
    end_time = "2027-07-11 23:59:59"

    # 调用方法获取最后一个ID
    last_id = get_last_id_in_local_file()
    print("最后一个ID：" + str(last_id))
    encrypted_data = update_last_id(begin_time, end_time, last_id)
    print(encrypted_data)
    # 抓数据
    get_data_through_api(encrypted_data)

    # 解密
    decrypt()

    # 落库
    falldata()

    # 更新last_id到本地文件中，用于下一次请求
    update_latest_id()
    print("循环次数:", i + 1)
