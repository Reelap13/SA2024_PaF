from utils.email_utils import send_email
import queue

def publish_service(in_queue):
    while True:
        try:
            message = in_queue.get(timeout=1)
            if message == "STOP":
                break
            send_email("Team Message", message)
        except queue.Empty:
            continue
