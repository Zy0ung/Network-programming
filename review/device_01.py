from socket import *
from random import randint

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 7777))
s.listen(3)

print('Waiting...')

while True:
    c, addr = s.accept()

    data = c.recv(1024).decode()

    if data == 'Request':
        Temp = str(randint(0, 40))
        Humid = str(randint(0, 100))
        Illum = str(randint(70, 150))
        
        msg = 'Device 1: ' + 'Temp=' + Temp + 'Humid=' + Humid + 'Illum=' + Illum
        c.send(msg.encode())
        
    elif data == 'quit':
        c.send(b'device 1 quit')
        c.close()
        break
    
c.close()
s.close()