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
    print(f"Received request: {message}")

    time.sleep(1)

    if len(message) > 100:
        socket.send(False)
    else:
        socket.send(True)