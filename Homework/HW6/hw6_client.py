from socket import *

BUFF_SIZE = 1024
port = 7777

sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('Enter the message "send [mboxID] message" or "receive [mboxID]" ')
    msg_list = msg.split(' ')

    if msg_list[0] == 'send':
        sock.sendto(msg.encode(), ('localhost', port))
        data, addr = sock.recvfrom(BUFF_SIZE)
        print(data.decode())
    
    elif msg_list[0] == 'receive':
        sock.sendto(msg.encode(), ('localhost', port))
        data, addr = sock.recvfrom(BUFF_SIZE)
        print(data.decode())
    
    else:
        sock.sendto(msg.encode(), ('localhost', port))
    
    if msg == 'quit':
        sock.sendto('quit'.encode(), ('localhost', port))
        break