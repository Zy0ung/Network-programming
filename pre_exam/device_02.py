from socket import *
from random import randint

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 8888))
s.listen(3)

print('Waiting...')

while True:
    c, addr = s.accept()

    data = c.recv(1024).decode()

    if data == 'Request':
        Heartbeat = str(randint(40, 140))
        Steps = str(randint(2000, 6000))
        Cal = str(randint(1000, 4000))
        
        msg = 'Device 2: ' + 'Heartbeat=' + Heartbeat + 'Steps=' + Steps + 'Cal=' + Cal
        c.send(msg.encode())

    elif data == 'quit':
        c.send(b'device 2 quit')
        c.close()
        break
    
c.close()
s.close()