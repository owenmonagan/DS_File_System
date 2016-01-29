import SocketServer
import threading
import logging
from DistributedFileAccess.server_address_info import get_lan_ip
from add_file_to_directory import add_file
from find_file_in_directory import find_file

host, port= "0.0.0.0", 4940

class ThreadedTCPHandler(SocketServer.BaseRequestHandler):

    def handle(self):

        request = self.request.recv(1024)

        if("FIND" in request):
            server_address=find_file(directory_server.directory_of_files,request)

        elif("REMOVE" in request):
            pass

        elif("ADD" in request):
            #request in form ADD\nfile_location\nfile_name
            directory_server.directory_of_files=add_file(directory_server.directory_of_files,request)




class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass



if __name__ == "__main__":
    logging.basicConfig(filename='logging.log',level=logging.DEBUG)
    my_ip = get_lan_ip()
    #h, p = my_ip, int(sys.argv[1])
    directory_server = ThreadedTCPServer((host, port), ThreadedTCPHandler)
    serverIP, serverPort = directory_server.server_address  # find out what port we were given
    directory_server.directory_of_files={}
    print(serverIP)
    print(serverPort)
    #directory_server.server_alive=True
    #directory=[]
    #directory.append(("server1",[]))
    #directory.append(("server2",[]))
    #add_user("owen",1234)
    #add_user("jam",4321)
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