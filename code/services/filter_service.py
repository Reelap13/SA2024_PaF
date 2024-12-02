from config.settings import STOP_WORDS

def filter_service(in_queue, out_queue):
    while True:
        message = in_queue.get()
        if message == "STOP":
            break
        if any(word in message.lower() for word in STOP_WORDS):
            print(f"Message filtered: {message}")
        else:
            out_queue.put(message)
