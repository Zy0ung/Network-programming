import smtplib
from email.message import EmailMessage

# 보내는 메일 서버
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

# 송신자, 수신자, 비밀번호
sender = 'thdwldud8@gmail.com'
recipient = 'thdwldud8@naver.com'
<<<<<<< HEAD
password = '앱비밀번호'
=======
password = 'tiqoomeyckfnsofp'
>>>>>>> c1c5a5efa8d1cca97bb755d820d6236317fb4159

# 메시지 생성하기
msg = EmailMessage()
msg['Subject'] = '이메일 테스트'
msg['From'] = sender
msg['To'] = recipient
text = '네트워크 프로그래밍 e-mail test 중'
msg.set_content(text)

# SMTP 객체 생성 후, 메시지 전송
s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
s.ehlo()
s.starttls()
s.login(sender, password)
s.send_message(msg)
s.quit()