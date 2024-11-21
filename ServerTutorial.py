import socket

#need to test this with the new receive and send functions!
#work on simulating a client for confirmation tonight!!
#also need to include timeouts for clients!!!

state_array = [0, 1, 2] #0 = SEND, 1 = RECEIVE, 2 = WAIT


class testServer:
    def __init__(self, ip, port):
        self.sock = socket.socket()
        self.ip = ip
        self.port = port
        self.clients = {}
        self.client_states = {}
        self.msg_log = {}
    def start(self, num):
        self.sock.bind((self.ip, self.port))
        self.sock.listen(num)
    def accept(self):
        c, addr = self.sock.accept()
        self.clients[addr] = c
        self.client_states[addr] = state_array[0]
    def send(self, msg): # I need feedback on the client logic to make certain of what args besides 'self' to pass to the send & receive functions
        #for item in self.clients: #following line may replace this one!
        for item in self.msg_log:
            #self.clients[item].send(msg.encode()) #following line may replace this one!
            self.msg_log[item].send(msg.encode())
            state = self.client_states[item] = state_array[1]
            #state = self.client_states[item]: May not need this line
            print("State for " + str(item) + " is: " + str(state))
    def receive(self): 
        #note: that we don't want to send to each and every client, just the ones who sent to the server; line 28 'should' resolve that
        #pass
        for item in self.clients:
            msg = self.clients[item].recv(2048).decode()
            delimiter = '/'
            if delimiter in msg:
                parsed_msg = msg.split(delimiter)
                self.client[item].send("Message received, please wait")
                #need to update dict for each time client sends new msg rather than using append, would look something like this:
                upd_log = {'item': parsed_msg} #might be a problem here, don't be surprised. May need refer to item index [0] (ip address) or "item[0]"
                self.msg_log.update(upd_log)
                state = self.client_states[item] = state_array[2]
                print("State for " + str(item) + " is: " + str(state))
            else:
                self.client[item].send('{IV}') #sends back invalid msg reply
    
test = testServer("", 5000)
test.start(3)

msg = "{trade/0/20/20/20}"
print(msg)

    
while True:
    test.accept()
    test.send(msg)
