import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = ('localhost', 3333)
sock.connect(addr)

while True:
    cal = input('TCP 계산기 ex) 27 + 21 : ')

    if cal == 'q':
        break
    else:
        sock.send(cal.encode())

    result = sock.recv(1024)
    print(result.decode())

sock.close()