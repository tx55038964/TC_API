import json

import pandas as pd
import pymysql

# 拼接文件路径
file_path = r"demo/json_data/data.json"
file_read = open(file_path, 'r', encoding='utf-8')
data = json.load(file_read)
df = pd.DataFrame(data["data"]["records"], columns=data["data"]["columnNames"])
df.fillna(0, inplace=True)
print("转换成功")
print(df.columns)

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
# 执行SQL语句将数据更新到表中
with connection.cursor() as cursor:
    # 构造SQL语句
    insert_query = f"REPLACE INTO {table_name} ({', '.join(df.columns)}) VALUES "
    row_values = []
    for row in df.itertuples(index=False):
        row_values.append(f"({', '.join(f'%s' for _ in range(len(df.columns)))})")
    insert_query += ", ".join(row_values) + ";"

    # 执行SQL语句
    cursor.execute(insert_query, [val for row in df.values for val in row])
    connection.commit()
    print(f"更新数据到MYSQL数据库中成功")
# 关闭数据库连接
connection.close()
