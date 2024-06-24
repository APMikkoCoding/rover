import socket
import threading
import network

SERVER = "192.168.43.105" # socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, network.PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[LOG]: New connection from {addr}.")

    connected = True
    while connected:
        msg_len = conn.recv(network.HEADER).decode(network.FORMAT)
        if msg_len:
            msg_len = int(msg_len)
            msg = conn.recv(msg_len).decode(network.FORMAT)

            if msg == network.DC_NOTIF:
                connected = False
                print(f"[DISCONNECT]: {addr} has left.")
                conn.send("Received.".encode(network.FORMAT))
                continue

            conn.send("Received.".encode(network.FORMAT))
            print(f"[{addr}]: {msg}")



    conn.close()

def start():
    server.listen()
    print(f"[LOG]: Server started. Listening on port {network.PORT}.")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[LOG]: There are currently {threading.active_count() - 1} active connections.")

print(f"[LOG]: Server starting on port {network.PORT} at IPv4 address {SERVER}.")
start()
