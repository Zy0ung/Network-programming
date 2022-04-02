from socket import *
import sys
import random

BUF_SIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 7777))
sock.listen(10)

while True:
    conn, addr = sock.accept()
    msg = conn.recv(BUF_SIZE).decode()

    if not msg:
        sock.close()
        continue

    elif msg == 'quit':
        print('client:', addr)
        conn.close()
        sys.exit()

    elif msg == 'Request':
        print('client:', addr)

        temp = random.randint(0, 40)
        humid = random.randint(0, 100)
        illum = random.randint(70, 150)

        data = f'Temp={temp} Himid={humid} Illum={illum}'
        conn.send(data.encode())

    conn.close()