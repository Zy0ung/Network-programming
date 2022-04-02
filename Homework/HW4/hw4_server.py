from socket import *

#웹 서버 소켓(포트번호 80)을 열고 웹 클라이언트의 연결을 기다림
s = socket()
s.bind(('', 80))
s.listen(10)


Res_error = "HTTP/1.1 404 Not Found\r\n" + "\r\n" + "<HTML><HEAD><TITLE><Not Found></TITLE></HEAD>"+ "<BODY>Not Found</BODY></HTML>"

while True:
    c, addr = s.accept()

    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')

    print(req)
    filename = req[0].split()[1][1:]

    if filename == 'index.html':
        http_file = open(filename, 'r', encoding='utf-8')
        mimeType = 'text/html'
        Res_msg = ("HTTP/1.1 200 OK\r\n" + "'Content-Type: '" + mimeType + "\r\n" + "\r\n")
        c.send(Res_msg.encode())
        data = http_file.read()
        c.send(data.encode('euc-kr'))

    elif filename == 'iot.png':
        png_file = open(filename, 'rb')
        mimeType = 'image/png'
        Res_msg = ("HTTP/1.1 200 OK\r\n" + "'Content-Type: '" + mimeType + "\r\n" + "\r\n")
        c.send(Res_msg.encode())
        data = png_file.read()
        c.send(data)

    elif filename == 'favicon.ico':
        icon_file = open(filename, 'rb')
        mimeType = 'image/x-icon'
        Res_msg = ("HTTP/1.1 200 OK\r\n" + "'Content-Type: '" + mimeType + "\r\n" + "\r\n")
        c.send(Res_msg.encode())
        data = icon_file.read()
        c.send(data)

    else:
        c.send(Res_error.encode())

    c.close()