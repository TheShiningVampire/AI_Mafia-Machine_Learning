import smtplib
import getpass
from email.mime.text import MIMEText

def send_meail():
    sender_address = "awale.vinit@gmail.com"
    password = getpass.getpass()
    subject = "AI Mafia - Machine Learning"
    msg = '''
    Hi!
    This is my first attempt to send an email using python

    Thank you!
    Vinit  
    '''
    #Server initialisation
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_address , password)

    #draft message body
    msg = MIMEText(msg)
    msg['Subject'] = subject
    msg['From'] =  
       