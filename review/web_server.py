from socket import *

s = socket()
s.bind(('', 80))
s.listen(10)

while True:
    c, addr = s.accept()

    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')

    print(req)

    filename = req[0].split()[1][1:]

    if filename == 'index.html':
        http_open = open(filename, 'r', encoding='utf-8')
        mimType = 'text/html'
        Res_msg = 'HTTP/1.1 200 OK\r\n' + "Content-Type: " + mimType + '\r\n' + '\r\n'
        c.send(Res_msg.encode())
        data = http_open.read()
        c.send(data.encode('euc-kr'))

    elif filename == 'iot.png':
        png_open = open(filename, 'rb')
        mimType = 'image/png'
        Res_msg = 'HTTP/1.1 200 OK\r\n' + "Content-Type: " + mimType + '\r\n' + '\r\n'
        c.send(Res_msg.encode())
        data = png_open.read()
        c.send(data)

    elif filename == 'favicon.ico':
        ico_open = open(filename, 'rb')
        mimType = 'image/x-icon'
        Res_msg = 'HTTP/1.1 200 OK\r\n' + "Content-Type: " + mimType + '\r\n' + '\r\n'
        c.send(Res_msg.encode())
        data = ico_open.read()
        c.send(data)
    
    else:
        not_found = 'HTTP/1.1 404 Not Found\r\n' + '\r\n' + '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>'+ '<BODY>Not Found</BODY></HTML>'
        c.send(not_found.encode())

    c.close()
