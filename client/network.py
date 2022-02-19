from base64 import encode
import socket

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.server = "192.168.56.15"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.server_msg = self.connect()

    def connect(self):
        try:
            self.client.settimeout(10)
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            raise socket.error("Cannot connect")

    def send(self, data):
        try:
            self.client.settimeout(20)
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except:
            raise socket.error("Cannot connect")