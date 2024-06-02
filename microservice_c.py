"""
Title Manager: Checks for invalid characters in titles
"""

char_list = ['!','@','#','$','%','^','&','*']

import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5557")

while True:
    message = socket.recv()
    message = message.decode()
    print(f"Received request: {message}")

    time.sleep(1)

    char_count = 0

    for i in message:
        if i in char_list:
            socket.send(b"No")
            break
        elif char_count == len(message) - 1:
            socket.send(b"Yes")
            break
        char_count += 1