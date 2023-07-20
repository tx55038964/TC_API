import json


def update_latest_id():
    # 定义json路径
    path_data = r"demo/json_data/data.json_data"
    file_read = open(path_data, 'r', encoding='utf-8')

    path_request = r"demo/json_data/request.json_data"
    file_request = open(path_request, 'r', encoding='utf-8')

    # 需要加密的内容, file.read() 读取文件内容
    json_data = json.load(file_read)

    # 获取json_data的lastid
    lastid = json_data["lastid"]

    # 把lastid写入到json_write.lastid中
    json_request = json_data.load(file_request)
    json_request["lastid"] = lastid

    json_str = json_data.dumps(json_request)
    # 写入文件内容
    file_write = open(r"demo/json_data/request.json_data", 'w', encoding='utf-8')
    file_write.write(json_str)
    # 提示
    print("更新lastid成功")
