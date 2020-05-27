#using smtp lib library
#basic program only to 2 people. can import csv lib and send to hundred of people by creating loop
#To enable less secure app
#https://myaccount.google.com/lesssecureapps?pli=1


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


from_addr='send2prakashkumar@gmail.com'
to_addr=['send.2prakashkumar@gmail.com','send2prakash.kumar@gmail.com']

msg=MIMEMultipart()       #Variable in which the multipart will be saved
msg['From']=from_addr
msg['To']=" ,".join(to_addr)  #join the receipient email address
msg['subject']='just to check'

body='Hi there this is a test'

msg.attach(MIMEText(body,'plain'))

email='send2prakashkumar@gmail.com'
password='**********'

mail=smtplib.SMTP('smtp.gmail.com',587) #establish connection with the gmail
mail.ehlo()
mail.starttls() #for encoding
mail.login(email,password) #log into the senders account
text=msg.as_string()  #message was converted into the string format and stored into the text variable
mail.sendmail(from_addr,to_addr,text)
mail.quit()
