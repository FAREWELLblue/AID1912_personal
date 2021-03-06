'''
    seek.py
    文件偏移量展示
'''
f = open('file', 'w+')
f.write('春天来了')
f.flush()

print('当前文件偏移量位置：', f.tell())

f.seek(0, 0)  # 以开头为基准，向后移动0字节
# 第一个参数代表偏移量，正数向后，负数向前
# 第二个参数，0代表文件开头算起，1代表当前位置算起，2 表示文件末尾算起
# 必须以二进制打开才能是1或者2

data = f.read()
print(data)

f.close()
