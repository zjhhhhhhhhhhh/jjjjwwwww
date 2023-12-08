import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)# 创建一个 UDP 套接字
ip = input("请输入接收方 IP 地址：")
port = int(input("请输入接收方端口号："))# 获取接收方的 IP 地址和端口号，
filename = input("请输入需要传输的文件名称的绝对路径：")#输入需要传输的文件名称
with open(filename, "rb") as f:# 发送方以二进制只读方式打开文件
    data = f.read(1024)#文件内容不为空
    while data:
        sock.sendto(data, (ip, port))# 读取文件内容并发送到接收方
        data = f.read(1024)#文件内容
sock.close()# 关闭套接字