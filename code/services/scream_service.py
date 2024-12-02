import queue

def scream_service(in_queue, out_queue):
    while True:
        try:
            message = in_queue.get(timeout=1)
            if message == "STOP":
                break
            out_queue.put(message.upper())
        except queue.Empty:
            continue
