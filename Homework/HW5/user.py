from socket import *
import time
BUF_SIZE = 1024

while True:
    user = input()
    
    # 디바이스 1
    device1 = socket(AF_INET, SOCK_STREAM)
    device1.connect(('localhost', 7777))

    # 디바이스 2
    device2 = socket(AF_INET, SOCK_STREAM)
    device2.connect(('localhost', 8888))

    if user == '1':
        device1.send(b'Request')
        msg = device1.recv(BUF_SIZE)
        data = msg.decode()

        now = time.strftime('%c', time.localtime(time.time()))
        req = now + f': Device1: '+ data + '\n'

        f = open('data.txt', 'a')
        f.write(req)
        f.close()

    elif user == '2':
        device2.send(b'Request')
        msg = device2.recv(BUF_SIZE)
        data = msg.decode()

        now = time.strftime('%c', time.localtime(time.time()))
        req = now + f': Device2: '+ data + '\n'

        f = open('data.txt', 'a')
        f.write(req)
        f.close()

    elif user == 'quit':
        device1.send(b'quit')
        device2.send(b'quit')
        break

    device1.close()
    device2.close()

