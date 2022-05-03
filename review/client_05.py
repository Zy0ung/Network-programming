import socket
import threading


def handler(sock):
    while True:
        msg = sock.recv(1024)
        print(msg.decode())

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('localhost', 2500))

id = input('ID를 입력하세요: ')
sock.send(('['+id+']').encode())

th = threading.Thread(target=handler, args=(sock, ))
th.daemon = True
th.start()

while True:
    msg='[' + id + ']' + input()
    sock.send(msg.encode())