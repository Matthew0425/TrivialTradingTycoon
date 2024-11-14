import gNation
import socket

class client():

    def __init__(self, ip, port):
        self.s = socket.socket()
        self.connected = False
        self.s.connect((ip, port))
        self.data_type = ""
        self.data_id = 0
        self.data = []
        self.states = {"SEND": 0,
                       "RECEIVE": 1,
                       "WAIT": 2}
        self.currentState = 0
        self.ip = ip
        self.port = port
    
    def connect(self, ip, port):
        if not self.connected == False:
            self.s.connect((ip, port))

    def send(self, data):
        if self.currentState == states["SEND"]:   
            self.s.send(data)

    def recv(self):
        if self.currentState == states["RECEIVE"]:
            msg = str(self.s.recv())
            print(msg)
            if msg[0] != '{' and msg[len(msg) - 1] != '}':
                return
            else:
                temp = msg[1:len(msg)-1].split('/')
                for item in temp:
                    if item == temp[0]:
                        self.data_type = item
                    elif item == temp[1]:
                        self.data_id = item
                    else:
                        data.append(item)

    def wait():
        if self.currentState == states["WAIT"]:
            pass

cli = client("127.0.0.1", 5000)
cli.currentState = 1

while True:
    cli.connect(cli.ip, cli.port)
    cli.recv()
    
