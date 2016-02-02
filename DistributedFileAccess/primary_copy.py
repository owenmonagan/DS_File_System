#accepts all request
#also talks to other slaves
from logon_to_AS import logon, generate_request
import logging
import socket


def propagate_write(list_of_servers, file_name):
    write_message="WRITE\n{}\n".format(file_name)
    failed_servers=[]
    for server in list_of_servers:
        ticket, session_key= logon("server",server[0],server[1],"012345678replica")
        write_request=generate_request(ticket,session_key,write_message)
        #server_file_location=get_server_file_location_from_directory(write_request)
        server_file_location=server_file_location.split("\n")
        print server_file_location
        print "server_file_location_above"
        try:
            s= socket.socket()
            s.connect(server[0],server[1])
            file = open('{}'.format(file_name),'w')
            logging.info("File opened and beginning download")
            chunk=s.request.recv(1024)
            while (chunk):
                logging.info("Downloading...")
                file.write(chunk)
                print chunk
                chunk=s.request.recv(1024)
            file.close()
            s.request.send("{} has been successfully uploaded".format(file_name))
            logging.info("Writing File Complete")
        except:
            failed_servers.append(server)
    return failed_servers

def ping_primary_copy(primary_address):
    ping_message="PING"
    ticket, session_key= logon("server",primary_address[0],primary_address[1],"012345678replica")
    ping_request=generate_request(ticket,session_key,ping_message)
    try:
        s=socket.socket()
        s.connect(primary_address[0],primary_address[1])
        s.send(ping_request)
        ping_info=s.recv(1024)

        return parse_string_server_list(ping_info)
    except:
        return None

def parse_tuple_server_list(server_list):
    server_string=""
    for server in server_list:
        server_string= "{}\n{},{}".format(server_string,server[0],server[1])
    return server_string

def parse_string_server_list(server_list):
    server_list=[]
    #host,port
    server_strings=server_list.split("\n")
    for servers in server_strings:
        server_address=servers.split(",")
        #adding the host and port (in int form) to the server list
        server_list.append((server_address[0],int(server_address[1])))
    return server_list


