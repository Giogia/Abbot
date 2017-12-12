#!/usr/bin/env python2

import SocketServer

class MyTCPSocketHandler(SocketServer.BaseRequestHandler):
    

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    
    HOST, PORT = "localhost", 9999

    # instantiate the server, and bind to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPSocketHandler)

    # activate the server
    # this will keep running until Ctrl-C
    server.serve_forever()
