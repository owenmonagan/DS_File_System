import SocketServer
import logging
import sys
import random
import threading
import logging
from parse_request import parse_message
from key_store import find_key, find_server_key, add_server
#from DistributedFileAccess.server_address_info import get_lan_ip
from encrypt_decrypt import decrypt_func, encrypt_func
from session_key_generator import session_key
from token_creator import prepare_token, prepare_ticket
#auth_host, auth_port= "0.0.0.0", 9998
import datetime
auth_host, auth_port= sys.argv[1], int(sys.argv[2])
directory_host, directory_port= sys.argv[1], int(sys.argv[3])
file_host, file_port= sys.argv[1], int(sys.argv[4])

class ThreadedTCPHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        #log_in_request form #####\nUserID
        self.log_in_request = self.request.recv(1024)
        #seperating the id from the encrypted message
        self.encyripted_message, self.id = parse_message(self.log_in_request)
        #finding the requests key from the database
        self.key=find_key(self.id)
        #print self.key
        #Decrypting message
        self.message= decrypt_func(self.key, self.encyripted_message)
        #print self.message
        serverinfo=self.message.split("\n")
        print int(serverinfo[1])
        print authentication_server.server_database
        self.session_key=str(session_key)
        #print self.session_key

        self.server_encryption_key=find_server_key((serverinfo[0],int(serverinfo[1])),authentication_server.server_database)
        #create ticket
        self.ticket=prepare_ticket(self.server_encryption_key, self.session_key)

        #Sending Token
        self.token= prepare_token(self.ticket,session_key,(serverinfo[0],serverinfo[1]))
        self.encryipted_token=encrypt_func(self.key,self.token)
        self.request.send(self.encryipted_token)

        #prepare token
        #send token

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass




if __name__ == "__main__":
    print "AUTHENTICATION_SERVER_ON_PORT: {}".format(auth_port)
    logging.basicConfig(filename='logging.log',level=logging.DEBUG)
    #my_ip = get_lan_ip()
    #h, p = my_ip, int(sys.argv[1])
    authentication_server = ThreadedTCPServer((auth_host, auth_port), ThreadedTCPHandler)
    serverIP, serverPort = authentication_server.server_address  # find out what port we were given
    authentication_server.server_database=[]

    key="0123456789ab{}".format(directory_port)
    authentication_server.server_database= add_server((directory_host,directory_port), key,authentication_server.server_database)

    key="0123456789ab{}".format(file_port)
    authentication_server.server_database= add_server((file_host,file_port), key,authentication_server.server_database)


    #this is for replication
    #Assums that replication servers are within a few ports range of the primary file server.....
    for file_servers_index in range(-10,10):
        server_id= (file_host, file_port+file_servers_index)
        key="0123456789ab{}".format(file_port+file_servers_index)
        authentication_server.server_database= add_server(server_id, key,authentication_server.server_database)
    #print(serverIP)
    #print(serverPort)
    authentication_server.server_alive=True
    #add_user("owen",1234)
    #add_user("jam",4321)
    current_min=datetime.datetime.now().minute
    try:
        server_thread = threading.Thread(target=authentication_server.serve_forever)
        server_thread.daemon = True
        server_thread.start()


        #servertimes out after 10 minutes
        while(authentication_server.server_alive==True and current_min>datetime.datetime.now().minute-10):
            pass

        authentication_server.shutdown()
        authentication_server.server_close()
        exit()

    except KeyboardInterrupt:
        print("Key board interrupt \nServer Shutting Down")
        authentication_server.shutdown()
        authentication_server.server_close()
        exit()