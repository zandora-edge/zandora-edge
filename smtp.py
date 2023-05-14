import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(receiver_email, message):
    # Email information
    sender_email = 'zandora.help@gmail.com'
    sender_password = 'zqiraljkmkoiatzy'
    subject = 'Message Recived (Zandora Edge) - Contact Form'

    # HTML content of the email
    html_content = f"""
    <!DOCTYPE html>

    <html lang="en">
    <head>
    <body>
    {message}
    </body>
    </html>
    """

    # Create a multipart message and set headers
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Add HTML content to the message
    msg.attach(MIMEText(html_content, 'html'))

    # Create SMTP session and send the message
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)


# Get form data
name = input('Your Name: ')
email = input('Your Email: ')
message = input('Subject: ')

send_email(receiver_email= email, message= message )