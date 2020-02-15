import smtplib

# Set email account and password
emailAccount = 'microfarads@gmail.com '
password = 'Soapsoap10'
message = 'Hi Kyle, it is me... your server.\nHope you are have a great day!\n' \
          'I am working my butt off down here.'

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
print(type(smtpObj))

smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(emailAccount, password)
smtpObj.sendmail(emailAccount, emailAccount, 'Subject: Salutations \n\n' + message)
smtpObj.quit()