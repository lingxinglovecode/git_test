import socket
import threading

PORT =5050
SEVER = "192.168.31.192"
HEADER = 64
FORMAT = 'utf-8'
ADDR = (SEVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER-len(send_length))
    client.send(send_length)
    client.send(message)

send('shit')
