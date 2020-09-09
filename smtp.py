# import necessary packages
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import random
# create message object instance
def sm(email):
    msg = MIMEMultipart()
 
    otp=random.randint(1000,9999)
    message = "Your OTP is :"+str(otp)
 
    # setup the parameters of the message
    password = "kavabh99"
    msg['From'] = "roexamination@gmail.com"
    msg['To'] = email
    msg['Subject'] = "OTP"
 
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
 
    #create server
    server = smtplib.SMTP('smtp.gmail.com: 587')
 
    server.starttls()
 
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
 
 
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
 
    server.quit()
 
    return(otp)