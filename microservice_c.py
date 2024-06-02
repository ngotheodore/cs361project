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
    print(f"Received request: {message}")

    time.sleep(1)

    for i in message:
        if i in char_list:
            socket.send(False)
        else:
            socket.send(True)