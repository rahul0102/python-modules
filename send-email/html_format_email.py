from config import GMAIL
from smtplib import SMTP, SMTPAuthenticationError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase


sender_email_id = GMAIL['host']
receiver_list = ['rahulraval1997@gmail.com']

# instance of MIMEMultipart
msg = MIMEMultipart()

# storing the senders email address
msg['From'] = sender_email_id

# storing the receivers email address
msg['To'] = receiver_list[0]

# storing the subject
msg['Subject'] = "Test Email"

txt_msg = "Hey There!"
html_msg = "<b>Tester</b>"

part_1 = MIMEText(txt_msg, 'plain')
part_2 = MIMEText(html_msg, 'html')

msg.attach(part_1)
msg.attach(part_2)

print(msg.as_string())

try:
    # creates SMTP session
    email_conn = SMTP(GMAIL['host'], GMAIL['port'])

    email_conn.ehlo()

    # start TLS for security
    email_conn.starttls()

    # authentication
    email_conn.login(GMAIL['username'], GMAIL['password'])

    # message tobe sent
    message = msg.as_string()

    # send email
    email_conn.sendmail(sender_email_id, receiver_list, message)

    print('Successfully sent')
except SMTPAuthenticationError:
    print("Username/Password comnination is not valid")
except Exception as e:
    print("Some error occured\n", e)
finally:
    # close the session
    email_conn.quit()
