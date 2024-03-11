import smtplib, ssl

def end_mail(subject, text):
    """
    Sending mail to yourself about the results of this script
    """
    # TODO: Put a lot of this info in config file
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    sender = input("Input your email and press enter: ")
    password = input("Input password and press enter: ")
    receiver = sender

    print(f'sending mail with subject: {subject} \n'
            f'and text: {text}')


# TODO: could send this mail with cgg.cgg.emailer if written for only people with access to that repo

## Did not have time to make mail work, but could have done something like this:
#    context = ssl.create_default_context()# Create a secure SSL context
#    server = smtplib.SMTP(smtp_server,smtp_port)
#    server.ehlo()
#    server.starttls(context=context) # Secure the connection
#    server.login(sender, password)
#    message ='Subject: {}\n\n{}'.format(subject, text)
#    server.sendmail(sender, receiver, message)
#    server.quit()

