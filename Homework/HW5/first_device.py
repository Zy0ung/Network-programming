from socket import *

import random

BUF_SIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 7777))
sock.listen(10)

while True:
    conn, addr = sock.accept()
    print('Connected ', addr)

    msg = conn.recv(BUF_SIZE)
    data = msg.decode()
    
    if data == 'Request':
        temp = random.randint(0, 40)
        humid = random.randint(0, 100)
        illum = random.randint(70, 150)
        msg = f'Temp={temp} Himid={humid} Illum={illum}'
        conn.send(msg.encode())

    elif data == 'quit':
        conn.close()
        break

    elif not msg:
        break

conn.close()
sock.close()