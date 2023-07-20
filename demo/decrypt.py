from util.EncryptData import EncryptData


def decrypt():
    path = r"demo/json_data/response.json_data"
    file = open(path, 'r', encoding='utf-8')

    file_result = open(r"demo/json_data/data.json_data", 'w', encoding='utf-8')

    # 密码
    password = 'MQ0WINT60DXP7U7R09A70V6Z1SEDIGYH'

    # ???????, file.read() ??????
    data = file.read()
    # ??**??????16???
    eg = EncryptData(password)
    res = eg.decrypt(str(data))

    # ???file_result??????, file_result.write() ??????
    file_result.write(res)


decrypt()
