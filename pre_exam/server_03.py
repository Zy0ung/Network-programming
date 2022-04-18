from socket import *
from collections import defaultdict
port = 5555

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', port))
print('Listening...')

dict = defaultdict(list)

while True:
    data, addr = s.recvfrom(1024)
    data = data.decode().split(' ')

    if data[0] == 'send':
        msg = ' '.join(data[2:])
        dict[data[1]].append(msg)
        print(dict)
        s.sendto("OK".encode(), addr)
    
    elif data[0] == 'receive':
        print(dict)
        if data[1] in dict:
            if not dict[data[1]]:
                print("No messages")
                s.sendto("No message".encode(), addr)
            else:
                collect = dict[data[1]].pop(0)
                print(dict)
                s.sendto(collect.encode(), addr)
        else:
            s.sendto("No messages".encode(), addr)
    
    if data[0] == 'quit':
        break