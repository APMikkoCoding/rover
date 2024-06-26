import socket
import network

ADDR = (input("IP: "), network.PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(network.FORMAT)
    msg_len = len(message)
    send_length = str(msg_len).encode(network.FORMAT)
    send_length += b' ' * (network.HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(network.FORMAT))

m = input("Send a message: ")

while m != network.DC_NOTIF:
    send(m)
    m = input("Send a message: ")

send(m)
client.close()
