
import smtplib
from email.message import EmailMessage 


def send_email(subject, to, body, sender): 
    with open(body) as f: 
        msg = EmailMessage()
        msg.set_content(f.read())

    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = to

    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()

send_email("Test email", "rowan.pitt@btinternet.com", "email.txt", "localhost")

"""
Alternativley the below can be used to send an email using an external email host 

SENDER_EMAIL = $EMAIL
SENDER_PASSWORD = $PASSWORD 

def send_email(reciever_email, subject, body:
    message = f'Subject: {subject}\n\n{body}'
    with smtplib.SMTP('$SERVER, $PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, message)

"""