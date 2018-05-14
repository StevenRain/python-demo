import socket

HOST = '0.0.0.0'
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()

while 1:
    data = conn.recv(1024)
    readBuffer = []
    if not data:
        break
    else:
        for index in range(0, len(data)):
            readBuffer.append(data[index] >> 2)
    print("revc %s" % data)
    resultData = b''.join(readBuffer).decode('utf-8')
    print(resultData)
    conn.sendall(data)  # 发送接收到的数据
    # conn.sendall(readBuffer)
conn.close()
