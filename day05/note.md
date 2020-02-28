# UDP套接字
##服务端：
socket--bind--recvfrom--sendto--close
socket=socket(AF_INET,SOCK_DGRAM)
socket.bind()
data,addr=sockfd.recvfrom(buffersize)
> 功能：接收UDP消息
> 参数：每次最多接收多少字节
> 返回值：data 接收到的内容
>        addr 消息发送方地址

n=sockfd.sendto(data,addr)
> 功能：发送UDP消息
> 参数：data 发送的内容 bytes格式
>      addr  目标地址：（ip，端口）
> 返回值：发送的字节数

sockfd.close
##客户端：
socket--sendto--recvfrom--close
## 特征：
1. 不会产生粘包问题
2. 接收量少于发送量时会丢失信息
#TCP与UDP
1. 流式套接字是以字节流方式传输，数据报套接字以数据报形式传输
2. TCP套接字会有粘包，udp套接字有信息边界不会粘包
3. TCP套接字保证信息完整性，udp套接字不能
4. tcp套接字依赖listen accept建立连接才能收发消息，udp则不需要
5. tcp套接字使用send，recv收发消息。udp套接字使用sendto，recvfrom收发消息

#struct 模块
- 原理 将一组简单数据进行打包，转换为bytes格式发送。或者将一组bytes格式数据，进行解析。
- 接口使用
  * Struct(fmt)
    + 功能：生成结构化对象
    + 参数：fmt 定制的数据结构
    > i表示整数 f表示浮点数 s表示字节串，字节串前跟长度例：4s
    > 字节串前的长度如果大于实际长度，解包后多出的为空字节
        >如果小于实际长度，打包时会丢失多余字节
  * st.pack(v1,v2,v3...)
    + 功能：将一组数据按照指定格式打包转换为bytes
    + 参数：要打包的数据
    + 返回值：bytes字节串
  * st.unpack(bytes_data)
    + 将bytes字节串按照指定的格式解析
    + 参数：要解析的字节串
    + 返回值：解析后的内容
  * 也可以直接用struct调用
    > data=struct.pack('i4sif',1,b'li',168,92.5)
    > data=struct.unpack('i4sif',data)

# HTTP协议
## HTTP协议（超文本传输协议）
- 用途：网页获取，数据的传输
- 特点：
    + 应用层协议，传输层使用TCP传输
    + 简单，灵活，很多语言都有HTTP专用接口
    + 无状态，协议不记录传输内容
    + http1.1 支持永久连接，丰富了请求类型
- 网页请求过程
1. 客户端（浏览器）通过TCP传输，发送http请求给服务端
2. 服务端接收到http请求后解析
3. 服务端处理请求内容，组织响应内容
4. 服务端将响应内容以http响应格式发送给浏览器
5. 浏览器接收到响应内容，解析展示