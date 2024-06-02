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

    for i in message:
        if i in char_list:
            #socket.send(bytes("No", encoding='utf-8'))
            socket.send(b"No")
            break
        elif i == len(message) - 1:
            socket.send(b"Yes")
            break
    #socket.send(bytes("Yes", encoding='utf-8'))
    #socket.send(b"Yes")