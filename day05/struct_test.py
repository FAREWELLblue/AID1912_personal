'''
    数据打包示例
'''
import struct

# 数据： 1 b"Lily“ 168 92.5

# 确定格式对象
st = struct.Struct('i4sif')

# 打包
data=st.pack(1, b"Li", 168, 92.5)
print(data)

# 解包
data=st.unpack(data)
print(data[1].strip(b'\x00'))# 去除字节串两侧的\x00