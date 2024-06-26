from comm.move_data import MoveData
from comm import network
import socket
import pickle
import cv2

class Server:
    def __init__(self):
        self.connection = None
        self.server_socket = None
        self.SOCKET_ADDRESS = None

    def step(self):
        current_frame = self.receive_frame()

        # VVV PUT MOVE LOGIC IN THIS VVV
        move = self.process_movement()
        # ^^^ PUT MOVE LOGIC IN THIS ^^^

        self.send_movement(move)

        cv2.imshow("Stream", current_frame)
        if cv2.waitKey(1) == ord('q'): quit(0)

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)  # "192.168.43.105"

        print("IP: ", host_ip)

        self.SOCKET_ADDRESS = (host_ip, network.PORT)

        self.server_socket.bind(self.SOCKET_ADDRESS)
        self.server_socket.listen(5)
        print("Listening.")

        self.connection, _ = self.server_socket.accept()

    def receive_frame(self):
        header = self.connection.recv(network.HEADER_LENGTH).decode(network.HEADER_FORMAT)

        if header:
            data = b''

            while True:
                data += self.connection.recv(int(header))
                if data[-len(network.END):] == network.END: break

            return pickle.loads(data)
            # ^^^ This is the frame ^^^

    def process_movement(self) -> MoveData:
        return MoveData(5, 7) # Replace with real code

    def send_movement(self, move_data):
        pass
        move_bytes = pickle.dumps(move_data)

        header = str(len(move_bytes)).encode(network.HEADER_FORMAT)
        header += b' ' * (network.HEADER_LENGTH - len(header))
        self.connection.send(header)

        self.connection.sendall(move_bytes + network.END)