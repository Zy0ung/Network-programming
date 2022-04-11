from socket import *
import random

port = 3333
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

while True:
    sock.settimeout(None) # socket의 블로킹 모드 timeout 설정
    while True: # None인 경우, 무한정 블로킹 됨
        data, addr = sock.recvfrom(BUFFSIZE)
        if(data.decode() == 'fail'):
            sock.sendto(b'nack', addr)
            break
        if random.random() <= 0.5:
            continue
        else:
            sock.sendto(b'ack', addr)
            print('<- ', data.decode())
            break
    msg = input('-> ')
    reTx = 0
    
    while reTx <= 3:
        resp = str(reTx) + ' ' + msg
        sock.sendto(resp.encode(), addr)
        sock.settimeout(2)

        try:
            data, addr = sock.recvfrom(BUFFSIZE)
        except timeout:
            reTx += 1
            continue
        else:
            break

    if reTx > 3:
        sock.sendto(b'fail', addr)
        sock.settimeout(None)
        while True:
            try:
                ndata, naddr = sock.recvfrom(BUFFSIZE)
            except timeout:
                break
            if ndata.decode() == 'nack':
                print('NACK!')
                break