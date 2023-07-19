import pandas as pd
import pymysql
import redis
from redisbloom.client import Client

import json

# 连接到 Redis
redis_client = redis.Redis(host='localhost', port=6379, db=0)

# 创建 RedisBloom 客户端
bloom_client = Client(redis_client)

# key
key = 'id_name'

# 创建布隆过滤器
bloom_client.bfCreate(key, errorRate=0.01, capacity=10000)


def generate_identifier(row):
    # 假设"id"和"name"是DataFrame中的两列名称
    identifier = str(row.name) + str(row.id)
    return identifier


def falldata():
    # 拼接文件路径
    file_path = r"demo/json/data.json"
    print(file_path)
    file_read = open(file_path, 'r', encoding='utf-8')
    data = json.load(file_read)
    df = pd.DataFrame(data["data"]["records"], columns=data["data"]["columnNames"])
    df.fillna(0, inplace=True)
    print("转换成功")
    print(df.columns)
    print(df)

    # 连接MySQL数据库
    connection = pymysql.connect(host='150.158.93.174',
                                 user='root',
                                 password='Mc666888@@',
                                 db='MC_gyl',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("数据库连接成功")

    # 创建表
    table_name = 'crm_evaluation'

    create_table_query = f'CREATE TABLE IF NOT EXISTS `{table_name}` ('
    for column_name in df.columns:
        column_type = 'VARCHAR(255)'  # 默认将所有列设为VARCHAR(255)类型
        create_table_query += f'`{column_name}` {column_type}, '
    create_table_query = create_table_query[:-2] + ')'

    with connection.cursor() as cursor:
        cursor.execute(create_table_query)
        connection.commit()
    print("创建表成功")

    # 遍历 DataFrame 中的每一行数据
    for row in df.itertuples(index=False):
        # 生成唯一标识符
        identifier = generate_identifier(row)  # 根据需要自定义生成唯一标识符的逻辑

        # 检查标识符是否已存在于布隆过滤器中
        if bloom_client.bfExists(key, identifier):
            print(f"数据已存在于数据库中: {identifier}")
        else:
            # 执行插入操作
            with connection.cursor() as cursor:
                # 构造SQL语句
                insert_query = f"REPLACE INTO {table_name} ({', '.join(df.columns)}) VALUES ({', '.join(['%s'] * len(df.columns))})"
                cursor.execute(insert_query, row)
                connection.commit()

            # 将标识符添加到布隆过滤器中
            # redis_client.execute_command('BF.ADD', bloom_filter_name, identifier)
            bloom_client.bfAdd(key, identifier)

    print(f"更新数据到MYSQL数据库中成功")

    # 关闭数据库连接
    connection.close()


falldata()
