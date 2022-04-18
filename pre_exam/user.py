from socket import *
import time

while True:
    user = input('Choose the device 1 or 2: ')

    if user == '1':
        device1_s = socket(AF_INET, SOCK_STREAM)
        device1_s.connect(('localhost', 7777))
        
        device1_s.send(b'Request')
        data = device1_s.recv(1024).decode()

        now = time.strftime('%c', time.localtime(time.time()))
        req = now + data + '\n'

        f = open('data.txt', 'a')
        f.write(req)
        f.close()
        device1_s.close()

    elif user == '2':
        device2_s = socket(AF_INET, SOCK_STREAM)
        device2_s.connect(('localhost', 8888))

        device2_s.send(b'Request')
        data = device2_s.recv(1024).decode()

        now = time.strftime('%c', time.localtime(time.time()))
        req = now + data + '\n'

        f = open('data.txt', 'a')
        f.write(req)
        f.close()
        device2_s.close()

    elif user == 'quit' :
        device1_s = socket(AF_INET, SOCK_STREAM)
        device1_s.connect(('localhost', 7777))

        device2_s = socket(AF_INET, SOCK_STREAM)
        device2_s.connect(('localhost', 8888))

        device1_s.send(b'quit')
        device2_s.send(b'quit')

        device1_s.close()
        device2_s.close()
        break