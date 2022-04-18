from socket import *

port = 5555

s = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('Enter the message "send [mboxID] message" or "receive [mboxID]" ')
    msg_list = msg.split(' ')

    if msg_list[0] == 'send':
        s.sendto(msg.encode(), ('localhost', port))
        data, addr = s.recvfrom(1024)
        print(data.decode())
    
    elif msg_list[0] == 'receive':
        s.sendto(msg.encode(), ('localhost', port))
        data, addr = s.recvfrom(1024)
        print(data.decode())

    else:
        s.sendto(msg.encode(), ('localhost', port))

    if msg == 'quit':
        s.sendto('quit'.encode(), ('localhost', port))
        break