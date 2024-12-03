import queue

def scream_service(in_queue, out_queue):
    while True:
        try:
            message = in_queue.get()
            if message.text == "STOP":
                break
            message.text = message.text.upper()
            out_queue.put(message)
        except queue.Empty:
            continue
