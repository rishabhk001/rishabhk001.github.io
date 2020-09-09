import random
import smtplib
otp=random.randint(100000,999999)
sender="ads@asd.com"
receiver="rishabhkasana123@gmail.com"
message="Your OTP is:"+otp
sm=smtplib.SMTP('localhost')
sm.sendmail(sender,receiver,message)
print("Sent")