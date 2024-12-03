from utils.email_utils import send_email
import queue
from datetime import datetime

def publish_service(in_queue):
    while True:
        try:
            message = in_queue.get()
            if message.text == "STOP":
                break
            send_email("Team Message", message.text)
            
            processing_delay = (datetime.now() - message.timestamp).total_seconds()
            print(f"Publishing message: {message.text} | Delay: {processing_delay:.2f} seconds")
        except queue.Empty:
            continue
