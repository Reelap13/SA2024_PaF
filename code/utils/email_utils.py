from config.settings import EMAIL_ADDRESS, EMAIL_PASSWORD, EMAIL_RECIPIENTS

def send_email(subject, body):
    try:
        for recipient in EMAIL_RECIPIENTS:
            print(f"Email sent to {recipient} from {EMAIL_ADDRESS}:\n" +
                  f"Subject: {subject}\n" +
                  f"Body: {body}")
    except Exception as e:
        print(f"Error sending email: {e}")