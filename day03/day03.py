'''
    字符串和字节串
'''
s='hello world'
print(type(s))
s=b'hello world'# 普通字符串前面加b就变成了字节串
print(type(s))


s='你好'
print(s.encode()) # 将变量或者是非英文字符串转换为字节串

s='你好'.encode()
print(s.decode())# 串转换为字符串将字节

s=b'hello world'.decode()