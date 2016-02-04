import SocketServer
import logging
import sys
import threading
import logging
import random
#from server_address_info import get_lan_ip ,file_host, file_port
from write_file_to_server import write_file
from read_file_from_server import read_file
from authentication import authenticate
from primary_copy import propagate_write, ping_primary_copy, parse_tuple_server_list, propagate_write_2
from datetime import datetime
from election import election, parse_elected
file_host, file_port=sys.argv[3], int(sys.argv[4])
auth_host, auth_port="0.0.0.0" , int(sys.argv[5])
file_server_key= "0123456789ab{}".format(file_port)
#"012345678replica"
studentNumber = "8225096d25e2f49ea3efabe515fd9f58707934a0cb3a9494aea8d64ec363cd17"

class ThreadedTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        authenticated_requst=authenticate(file_server_key,self.request.recv(1024))
        print "FS {}: AuthenticatedReply below".format(file_port)
        print(authenticated_requst)


        if ("KILL_SERVICE" in authenticated_requst):
            #print ("Service killed by Client\n")
            self.client_connected=False
            file_server.server_alive = False


        elif ("HELO" in authenticated_requst):
            #print(authenticated_requst)
            lines=authenticated_requst.split()
            authenticated_requst = ("HELO {}\nIP:{}\nPort:{}\nStudentID:{}\n".format(lines[1], my_ip, p, studentNumber))
            self.request.send(authenticated_requst)


        elif("WRITE" in authenticated_requst):
            #print(authenticated_requst)
            write_file(self, authenticated_requst)
            #if it is a primary copy then the server propagates the updated file
            #to replicas, if a server can not be progagate too it is deamed failed and removed from
            #the replica server list
            if(file_server.primary_copy==True):
                file_name=authenticated_requst.split("\n")[1]
                failed_servers=propagate_write_2(file_server.server_list,file_name, auth_port)
                file_server.server_list.remove(failed_servers)


        elif("READ" in authenticated_requst):
            if(file_server.primary_copy==True):
                #send replica server info to client
                self.request.send(file_server.server_list[file_server.last_replica])
                #iterates to the next replica server, so that the following read requests are distributed fairly bewtween the replicas
                if(len(file_server.server_list)==file_server.last_replica):
                    file_server.last_replica=0
                else:
                    file_server.last_replica+=1
            else:
                #print(authenticated_requst)
                read_file(self, authenticated_requst)

        elif("Expired Ticket"):
            self.request("Your can not be completed, your ticket has expired")


        elif("PING" in authenticated_requst):
            #print "FS {}: received a ping".format(file_port)
            if(file_server.primary_copy==True):
                string_server_list=parse_tuple_server_list(file_server.server_list)
                self.request.send(string_server_list)
            else:
                self.request.send(None)


        elif("ELECTION" in authenticated_requst):
            #checks if the id in the message is larger then mine
            if(int(authenticated_requst.split("\n")[1])>file_server.server_id):
                self.request.send("\n")
            else:
                self.request.send("Whoa, I have a bigger Id, I'm a bully")


        elif("ELECTED" in authenticated_requst):
            file_server.primary_copy=parse_elected(authenticated_requst)



class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass




if __name__ == "__main__":
    print "FILE_SERVER_ON_PORT: {}".format(file_port)
    logging.basicConfig(filename='logging.log',level=logging.DEBUG)
    #my_ip = get_lan_ip()
    #h, p = my_ip, int(sys.argv[1])
    file_server = ThreadedTCPServer((file_host, file_port), ThreadedTCPHandler)
    serverIP, serverPort = file_server.server_address  # find out what port we were given

    file_server.primary_copy=(sys.argv[1]=="True")
    print "SETTING UP FILE SERVER ON PORT: {}".format(file_port)
    print file_server.primary_copy
    if (file_server.primary_copy==False):
        print "FS {}  Is not a Primary!!".format(file_port)
    file_server.last_replica=0
    file_server.server_list=[]
    range_of_replicas=10
    for potential_replica_index in range(0,range_of_replicas):
        file_server.server_list.append(("0.0.0.0",file_port-5+potential_replica_index))

    #print sys.argv[1]
    #print sys.argv[2]
    #print sys.argv[3]
    #print sys.argv[4]


    #each replica must know the primary address
    file_server.primary_copy_address="0.0.0.0",int(sys.argv[2])

    #server id is used in the bully election algorithm
    file_server.server_id= file_port

    #aims to ensure that pings are distributed within a minute: doesnt overload the primary copy
    file_server.ping_interval=random.randint(1,59)
    #print file_server.ping_interval
    #print(serverIP)
    #print(serverPort)
    file_server.server_alive=True
    current_min=datetime.now().minute
    try:
        server_thread = threading.Thread(target=file_server.serve_forever)
        server_thread.daemon = True
        server_thread.start()

        while(file_server.server_alive==True and current_min> datetime.now().minute-3):
            #print datetime.now().second            #if replica then ping_primary
            if():#file_server.primary_copy==False and datetime.now().second==file_server.ping_interval && 4==5):
                print "FS {}  Pinged!".format(file_port)
                ping_reply=ping_primary_copy(file_server.primary_copy_address, auth_port, file_port)
                #if ping fails hold an election
                if(ping_reply==None):
                    election(file_server.server_id,file_server.server_list,file_host, file_port,auth_port)
                    pass
                else:
                    file_server.server_list=ping_reply

        file_server.shutdown()
        file_server.server_close()
        exit()

    except KeyboardInterrupt:
        print("Key board interrupt \nServer Shutting Down")
        file_server.shutdown()
        file_server.server_close()
        exit()