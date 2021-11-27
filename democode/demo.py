import smtplib
  
# creates SMTP session
s = smtplib.SMTP('mail.rbscience.co.in', 587)
  
# start TLS for security
s.starttls()
  
# Authentication
s.login("sales@rbscience.co.in", "Flax@2021")
  
# message to be sent
message = "Message_you_need_to_send"
  
# sending the mail
s.sendmail("sales@rbscience.co.in", "ritik.s10120@gmail.com", message)
print("mail is sent")
# terminating the session
s.quit()