import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)# 创建一个 UDP 套接字
ip = "0.0.0.0"
port = int(input("请输入接收方端口号："))
sock.bind((ip, port))# 绑定接收方的ip和端口号
filename = input("请输入接收到的文件保存的绝对路径：")# 接收文件数据并保存到指定路径下
with open(filename, "wb") as f:
    while True:
        data, addr = sock.recvfrom(1024)
        if not data:
            break
        f.write(data)
sock.close()# 关闭套接字