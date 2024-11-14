import socket

class testServer:
    def __init__(self, ip, port):
        self.sock = socket.socket()
        self.ip = ip
        self.port = port
        self.clients = {}
    def start(self, num):
        self.sock.bind((self.ip, self.port))
        self.sock.listen(num)
    def accept(self):
        c, addr = self.sock.accept()
        self.clients[addr] = c
    def send(self, msg):
        for item in self.clients:
            self.clients[item].send(msg.encode())
test = testServer("127.0.0.1", 5000)
test.start(3)

msg = "{trade/0/20/20/20}"
print(msg)

    
while True:
    test.accept()
    test.send(msg)
