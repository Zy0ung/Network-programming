import socket
import select
import time

socks = []
s_sock = socket.socket()
s_sock.bind(('', 5555))
s_sock.listen(5)

socks.append(s_sock)
print('Server Started')

while True:
    r_sock, w_sock, e_sock = select.select(socks, [], [])

    for s in r_sock:
        if s == s_sock:
            conn, addr = s_sock.accept()
            socks.append(conn)
            print(f'Client ({addr} connected.')
        else:
            data = s.recv(1024)
            if 'quit' in data.decode():
                print(addr, 'exited')
                s.close()
                socks.remove(s)
                continue

            print(time.asctime() + str(s.getsockname()) + ':' + data.decode())
            for client in socks:
                if client != s and client != s_sock:
                    client.send(data)