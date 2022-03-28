from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)
print('waiting...')

def cal(a, b, op):
    if op == '+':
        return int(a) + int(b)
    elif op == '-':
        return int(a) - int(b)
    elif op == '*':
        return int(a) * int(b)
    elif op == '/':
        return round(float(a) / float(b), 1)

while True:
    client, addr = s.accept()
    print('connection from ', addr)
    while True:
        try:
            data = client.recv(1024)
        except:
            break
        else:
            if not data or data == 'q':
                print("Connection closed")
                break

        try:
            a, op, b = data.decode().split()
            result = cal(a, b, op)
            
        except:
            client.send(b'Try Again')
        else:
            client.send(str(result).encode())

    client.close()
