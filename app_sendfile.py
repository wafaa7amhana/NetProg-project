import smtplib, ssl

port = 465
context = ssl.create_default_context()
server = smtplib.SMTP_SSL('smtp.gmail.com', port, context=context)

sender_email = 'nadaalouf1234@gmail.com'
rec_email = 'alimohammad24496@gmail.com'
subject = 'programming network'
with open("email.txt",'r') as f:
    msg_body=f.read()
message = 'Subject: {}\n\n{}'.format(subject, msg_body)

password = input('Type your password and press enter: ')
server.login(sender_email, password)

server.sendmail(sender_email, rec_email, message)
server.quit()
