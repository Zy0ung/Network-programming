from socket import *

import random

BUF_SIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 8888))
sock.listen(10)

while True:
    conn, addr = sock.accept()
    print('Connected ', addr)

    msg = conn.recv(BUF_SIZE)
    data = msg.decode()
    
    if data == 'Request':
        heartbeat = random.randint(40, 140)
        steps = random.randint(2000, 6000)
        cal = random.randint(1000, 4000)
        data = f'heartbeat={heartbeat} steps={steps} cal={cal}'
        conn.send(data.encode())

    elif data == 'quit':
        conn.close()
        break

    elif not msg:
        break

conn.close()
sock.close()
