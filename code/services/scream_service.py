def scream_service(in_queue, out_queue):
    while True:
        message = in_queue.get()
        if message == "STOP":
            break
        out_queue.put(message.upper())
