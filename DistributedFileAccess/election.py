from Client.mainClient import logon, generate_request
import socket

def election(server_id, list_of_servers, host, port):

    election_message="ELECTION\n{}".format(server_id)
    is_highest_id=True

    for server in list_of_servers:
        ticket, session_key= logon("server",server[0],server[1],"012345678replica")
        election_request=generate_request(ticket,session_key,election_message)
        #server_file_location=get_server_file_location_from_directory(write_request)
        try:
            s= socket.socket()
            s.connect(server[0],server[1])
            s.send(election_request)
            response=s.recv(1024)
            if(not response=="\n"):
                highest_id=False
        except:
            pass
    if(is_highest_id==True):
        elected(host, port)
        return host,port

def elected(list_of_servers,host, port):
    elected_message="ELECTED\n{},{}".format(host, port)
    for server in list_of_servers:
        ticket, session_key= logon("server",server[0],server[1],"012345678replica")
        elected_request=generate_request(ticket,session_key,elected_message)
        try:
            s= socket.socket()
            s.connect(server[0],server[1])
            s.send(elected_request)
        except:
            pass

def election_response(socket, list_of_servers, server_id, election_string, host,port):
    if (int(election_string.split("\n")[1])>server_id):
        #this indicates that this server has a larger ID
        socket.request.send("My ID is larger")
        #begin a new election
        election(server_id, list_of_servers, host, port)
    else:
        #this indicates that the server has a lower id
        socket.request.send("\n")



def parse_elected(elected_string):
    host_and_port=elected_string.split("\n")[1]
    host_and_port=host_and_port.split(",")[1]
    return host_and_port[0],int(host_and_port[1])