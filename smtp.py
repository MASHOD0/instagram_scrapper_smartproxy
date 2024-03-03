import smtplib
from .cred import password
def send_mail(email, receiver_email, subject, message):
    

    text = f"Subject: {subject}\n\n{message}"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls() # Secure the connection,
    server.login(email, password)
    server.sendmail(email, receiver_email, text)
    print("Email has been sent to "+receiver_email)