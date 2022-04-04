from socket import *
from collections import defaultdict

port = 7777
BUFF_SIZE = 1024
sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

dict = defaultdict(list)

while True:
    data, addr = sock.recvfrom(BUFF_SIZE)
    data = data.decode().split(' ')

    if data[0] == 'send':
        msg = ' '.join(data[2:])
        dict[data[1]].append(msg)
        print(dict)
        sock.sendto("OK".encode(), addr)
        
    elif data[0] == 'receive':
        print(dict)
        if data[1] in dict:
            if not dict[data[1]]:
                print("no message")
                sock.sendto("No message".encode(), addr)
            else:
                collect = dict[data[1]].pop(0)
                print(dict)
                sock.sendto(collect.encode(), addr)
        else:
            sock.sendto("No message".encode(), addr)
    if data[0] == 'quit':
        break