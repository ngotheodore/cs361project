"""
Checks character limit for files
"""

import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5558")

while True:
    message = socket.recv()
    message = message.decode()
    print(f"Received request: {message}")
    print(len(message))

    time.sleep(1)

    if len(message) > 2000:
        socket.send(b"No")
        #break
    else:
        socket.send(b"Yes")
        #break