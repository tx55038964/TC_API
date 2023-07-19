import os

import requests


def getAPI(data):
    url = "http://o2oapi.wuuxiang.com/external/evaluateinfo/GetEvaluateInfo.htm"
    apidata = data
    payload = 'systype=85694MCBFZB52856&data={}'.format(apidata)
    print("完整的请求URL：" + url)
    print("请求参数：" + payload)
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    # 获取当前脚本所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 定义要保存的文件路径
    file_path = os.path.join(current_dir, 'json', 'response.json')

    # 将响应数据存储到文件中
    with open(file_path, 'w') as file:
        file.write(response.text)


# 调用 getAPI() 函数并传入参数值
data_value = "Pbfsx4sbThNzUOsfOjbzURtJE6zDg5oaQ23xzGkcbvn9YnYB9ddWuBWBmVxCtQeI8nnHPtIjREkByQn7jQut33AteWnNVZWAkS0azh7AK-w="
getAPI(data_value)
