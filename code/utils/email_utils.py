import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config.settings import EMAIL_ADDRESS, EMAIL_PASSWORD, EMAIL_RECIPIENTS

def send_email(subject, body):
    try:
        with smtplib.SMTP('smtp.yandex.ru', 587) as server:
            server.starttls()  
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            for recipient in EMAIL_RECIPIENTS:
                msg = MIMEMultipart()
                msg['From'] = EMAIL_ADDRESS
                msg['To'] = recipient
                msg['Subject'] = subject
                msg.attach(MIMEText(body, 'plain'))

                server.send_message(msg)
                # print(f"Email sent to {recipient} from {EMAIL_ADDRESS}:\n" +
                #       f"Subject: {subject}\n" +
                #       f"Body: {body}")
    except Exception as e:
        print(f"Error sending email: {e}")