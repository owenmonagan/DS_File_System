import SocketServer
import threading
import logging
import sys
#from DistributedFileAccess.server_address_info import get_lan_ip
from add_file_to_directory import add_file, find_suitable_server
from find_file_in_directory import find_file
from authentication import authenticate

#directory_host, directory_port= "0.0.0.0", 6666
directory_host, directory_port= sys.argv[1], int(sys.argv[2])

directory_server_key="0123456789ab{}".format(directory_port)

class ThreadedTCPHandler(SocketServer.BaseRequestHandler):

    def handle(self):

        request = self.request.recv(1024)
        authenticated_request=authenticate(directory_server_key, request)
        if("READ" in authenticated_request):
            server_address=find_file(directory_server.directory_of_files,authenticated_request)
            if(not server_address == None):
                formated_server_address="{}\n{}".format(server_address[0],server_address[1])
                print formated_server_address
                self.request.send(formated_server_address)
            else:
                self.request.send("File Does Not Exist")

        elif("WRITE" in authenticated_request):
            #request in form ADD\nfile_location\nfile_name
            server_address=find_file(directory_server.directory_of_files,authenticated_request)
            if(server_address==None):
                server_address= find_suitable_server(int(sys.argv[2]))
            directory_server.directory_of_files=add_file(directory_server.directory_of_files,authenticated_request,server_address)
            formated_server_address="{}\n{}".format(server_address[0],server_address[1])
            print formated_server_address
            self.request.send(formated_server_address)




class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass



if __name__ == "__main__":
    print "DIRECTORY_SERVER_ON_PORT: {}".format(directory_port)
    logging.basicConfig(filename='logging.log',level=logging.DEBUG)
    #my_ip = get_lan_ip()
    #h, p = my_ip, int(sys.argv[1])
    directory_server = ThreadedTCPServer((directory_host, directory_port), ThreadedTCPHandler)
    serverIP, serverPort = directory_server.server_address  # find out what port we were given
    directory_server.directory_of_files={}
    directory_server.server_alive=True
    #print(serverIP)
    #print(serverPort)
    try:
        server_thread = threading.Thread(target=directory_server.serve_forever)
        server_thread.daemon = True
        server_thread.start()

        while(directory_server.server_alive==True):
            pass

        directory_server.shutdown()
        directory_server.server_close()
        exit()

    except KeyboardInterrupt:
        print("Key board interrupt \nServer Shutting Down")
        directory_server.shutdown()
        directory_server.server_close()
        exit()