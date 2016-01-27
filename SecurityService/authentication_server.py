import SocketServer
import logging
import threading
import logging
import os
import sys
import socket
from parse_request import parse_message
from password_store import add_user, find_user_password
from DistributedFileAccess.server_address_info import get_lan_ip

studentNumber = "8225096d25e2f49ea3efabe515fd9f58707934a0cb3a9494aea8d64ec363cd17"

class ThreadedTCPHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        #log_in_request form #####\nUserID
        log_in_request = self.request.recv(1024)
        encyripted_message, user_id = parse_message(log_in_request)
        password=find_user_password(user_id)

        #dycript msg
        #prepare token
        #send token

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass




if __name__ == "__main__":
    logging.basicConfig(filename='logging.log',level=logging.DEBUG)
    my_ip = get_lan_ip()
    #h, p = my_ip, int(sys.argv[1])
    file_server = ThreadedTCPServer((host, port), ThreadedTCPHandler)
    serverIP, serverPort = file_server.server_address  # find out what port we were given

    print(serverIP)
    print(serverPort)
    file_server.server_alive=True
    add_user("owen",1234)
    add_user("jam",4321)
    try:
        server_thread = threading.Thread(target=file_server.serve_forever)
        server_thread.daemon = True
        server_thread.start()

        while(file_server.server_alive==True):
            pass

        file_server.shutdown()
        file_server.server_close()
        exit()

    except KeyboardInterrupt:
        print("Key board interrupt \nServer Shutting Down")
        file_server.shutdown()
        file_server.server_close()
        exit()