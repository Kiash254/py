import smtplib, ssl
email_from = 'codewithkiash@gmail.com'
password = '39544609'
email_to = 'samuelkiando50@gmail.com'

email_string = 'This is a test email sent by Python.'

# Connect to the Gmail SMTP server and Send Email
  # Create a secure default settings context
context = ssl.create_default_context()
  # Connect to Gmail's SMTP Outgoing Mail server with such context
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    # Provide Gmail's login information
    server.login(email_from, password)
    # Send mail with from_addr, to_addrs, msg, which were set up as variables above
    server.sendmail(email_from, email_to, email_string)