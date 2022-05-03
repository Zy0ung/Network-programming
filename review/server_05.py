import socket
import threading
import time

clients = []
PORT = 2500

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', PORT))

print('Server Started')

def server_task(sock, addr):
    while True:
        data = sock.recv(1024)

        if 'quit' in data.decode():
            if sock in clients:
                print(addr, ': exited')
                clients.remove(sock)
                #continue
                break

        print(time.asctime() + str(addr) + ':' + data.decode())

        for c in clients:
            if c != sock:
                c.send(data)


s.listen(50)

while True:
    conn, addr = s.accept()
    clients.append(conn)
    print(addr)
    threading.Thread(target=server_task, args=(conn, addr)).start()