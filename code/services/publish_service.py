from utils.email_utils import send_email

def publish_service(in_queue):
    while True:
        message = in_queue.get()
        if message == "STOP":
            break
        send_email("Team Message", message)
