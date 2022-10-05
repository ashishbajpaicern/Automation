import smtplib

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)


smtpObj.starttls()
print(smtpObj.ehlo())
smtpObj.login('ashish.etw0@gmail.com', 'a2s6h4i5s8h1')
