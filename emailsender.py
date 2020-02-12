import smtplib, re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_email="sender@email.com"

def send_email_message(subject, to_email,  message):
    client = smtplib.SMTP('mail.smtp2go.com', 8025)
    client.ehlo()
    client.starttls()

    # Authentication
    client.login(from_email, "XXXXXXXXXXX")

    # message to be sent
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    # correcting mimetypes
    part1 = MIMEText(get_plain_text_message(message), 'plain')
    part2 = MIMEText(message, 'html')

    msg.attach(part1)
    msg.attach(part2)

    # sending the mail
    client.sendmail(from_email, to_email, msg.as_string())

    # terminating the session
    client.quit()
    return True


def get_plain_text_message(html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', html)
    return cleantext
