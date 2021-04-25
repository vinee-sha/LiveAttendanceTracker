# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib
from email.mime.text import MIMEText

def send_mail(receiver, Username, Password) :
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    
    # start TLS for security
    s.starttls()
    print(Password)
    # Authentication
    s.login("18b01a05a7@svecw.edu.in", "SVECW@123")
    message = "Subject: Regarding Password\n\n Your Password for Username: {} is {}".format(Username, Password)
    
    # sending the mail
    s.sendmail("18b01a05a7@svecw.edu.in", receiver, message)
    
    # terminating the session
    s.quit()