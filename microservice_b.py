"""
Password verifier that checks if a password meets the password criteria
"""

import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5556")

while True:
    message = socket.recv()
    message = message.decode()
    print(f"Received request: {message}")

    time.sleep(1)

    if len(message) >= 10:
        socket.send(b"Yes")
        #break
    else:
        socket.send(b"No")
        #break

    