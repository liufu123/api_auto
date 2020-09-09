import hashlib
def md5_value(value):
    """md5加密"""
    md5 = hashlib.md5(value.encode())
    result = md5.hexdigest()
    return result


print(md5_value("liufu"))