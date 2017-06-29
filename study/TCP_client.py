# 导入socket库:
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('192.168.8.79', 9999))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
for data in [b'fool', b'boy', b'world']:
    # 发送数据:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()