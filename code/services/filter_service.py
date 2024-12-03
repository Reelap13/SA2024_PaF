from config.settings import STOP_WORDS
import queue

def filter_service(in_queue, out_queue):
    while True:
        try:
            message = in_queue.get()
            if message.text == "STOP":
                break
            if any(word in message.text.lower() for word in STOP_WORDS):
                print(f"Message filtered: {message.text}")
            else:
                out_queue.put(message)
        except queue.Empty:
            continue
