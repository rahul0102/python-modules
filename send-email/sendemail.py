from config import GMAIL
from smtplib import SMTP, SMTPAuthenticationError


sender_email_id = GMAIL['host']
receiver_list = ['rahulraval1997@gmail.com']
try:
    # creates SMTP session
    email_conn = SMTP(GMAIL['host'], GMAIL['port'])

    email_conn.ehlo()

    # start TLS for security
    email_conn.starttls()

    # authentication
    email_conn.login(GMAIL['username'], GMAIL['password'])

    # message tobe sent
    message = "Hi there it is test mail form python"

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
