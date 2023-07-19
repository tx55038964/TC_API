from util.EncryptData import EncryptData

def decrypt():
    path = r"demo/json/response.json"
    file = open(path, 'r', encoding='utf-8')

    file_result = open(r"demo/json/data.json", 'w', encoding='utf-8')

    # ??
    password = 'MQ0WINT60DXP7U7R09A70V6Z1SEDIGYH'

    # ???????, file.read() ??????
    data = file.read()
    # ??**??????16???
    eg = EncryptData(password)
    res = eg.decrypt(str(data))

    # ???file_result??????, file_result.write() ??????
    file_result.write(res)


decrypt()
