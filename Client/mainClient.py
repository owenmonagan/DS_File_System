import socket               # Import socket module
from SecurityService.authentication_server import auth_host, auth_port
from DistributedFileAccess.server_address_info import file_host, file_port
from SecurityService.encrypt_decrypt import encrypt_func, decrypt_func
from DirectoryService.Directory_server import directory_host,directory_port

#host = socket.gethostname() # Get local machine name
#port = 12345                 # Reserve a port for your service.

#USERNAME
#ENCYRPITED
    #SERVERIP
    #SERVERPORT

#login in to directory server via AS


#if(download)
    #send file_name request to directory
    #returns file_location (serverip,serverport)
    #if(not None)
        #logon to requested server via AS
        #download_file
    #else
        #file does not exist

#if(upload)
    #send file_name request to directory
    #returns file_location (serverip,serverport)
    #if(file_exists)
        #logon to requested server via AS
        #uploadfile
    #else
        #directory server balancer
        #returns a location to store the file
        #adds the file to the directory
        #logon to requested location via AS
        #upload




def generate_login_message(username, serverIP,serverPort, password):
    serverinfo="{}\n{}".format(serverIP,serverPort)
    encrypted_message= encrypt_func( password, serverinfo)
    return "{}\n{}".format(username,encrypted_message)

def generate_request(ticket, session_key, message):
    encrypted_message=encrypt_func(session_key,message)
    final_request="{}\n{}".format(ticket,encrypted_message)
    return final_request

def read_file_from_server(read_message, file_name):
    #connect to directory server to find file location on the server
    ticket, session_key= logon("owen",directory_host,directory_port,"0123456789abcde1")
    write_request=generate_request(ticket,session_key,read_message)
    server_file_location=get_server_file_location_from_directory(write_request)
    if(not server_file_location=="File Does Not Exist"):

        server_file_location=server_file_location.split("\n")
        print server_file_location
        print "server_file_location_above"
        file_ticket, file_session_key= logon("owen",server_file_location[0],int(server_file_location[1]),"0123456789abcde1")
        download_request=generate_request(file_ticket,file_session_key,read_message)
        file_socket= socket.socket()
        file_socket.connect((server_file_location[0],int(server_file_location[1])))
        file_socket.send(download_request) #"WRITE\n{}\n".format(file_name)
        ready_to_rec_response=file_socket.recv(1024)
        print("Server: {}".format(ready_to_rec_response))

        file = open('{}'.format(file_name),'w')
        chunk=file_socket.recv(1024)
        while (chunk and not chunk=="\n"):
            file.write(chunk)
            print "downloading"
            chunk=file_socket.recv(1024)
        file.close()
        print file_socket.recv(1024)

    else:
        print "ERROR WHEN READING {}".format(file_name)
        print "File does not exists on the server"

def write_file_to_server(write_message, file_name):
    #connect to directory server to find file location on the server
    ticket, session_key= logon("owen",directory_host,directory_port,"0123456789abcde1")
    write_request=generate_request(ticket,session_key,write_message)
    server_file_location=get_server_file_location_from_directory(write_request)
    server_file_location=server_file_location.split("\n")
    print server_file_location
    print "server_file_location_above"
    file_ticket, file_session_key= logon("owen",server_file_location[0],int(server_file_location[1]),"0123456789abcde1")
    upload_request=generate_request(file_ticket,file_session_key,write_message)
    file_socket= socket.socket()
    file_socket.connect((server_file_location[0],int(server_file_location[1])))
    file_socket.send(upload_request) #"WRITE\n{}\n".format(file_name)
    f = open(file_name,'rb')

    ready_to_send_response=file_socket.recv(1024)
    print("Server: {}".format(ready_to_send_response))
    l = f.read(1024)
    while (l):
        print 'Sending...'
        file_socket.send(l)
        l = f.read(1024)
    f.close()
    print "Done Sending"
    file_socket.shutdown(socket.SHUT_WR)
    print file_socket.recv(1024)
    file_socket.close

def logon(username,server_ip,server_port, password):
    s = socket.socket()         # Create a socket object
    s.connect((auth_host, auth_port))
    login_message=generate_login_message(username,server_ip,server_port,password)
    s.send(login_message)
    Authentication_server_reply=s.recv(1024)
    decrypted_reply=decrypt_func(password,Authentication_server_reply)
    lines=decrypted_reply.split("\n")
    s.close()
    #returns ticket and session key
    return lines[0], lines[1]

def get_server_file_location_from_directory(request):
    s=socket.socket()
    s.connect((directory_host, directory_port))
    s.send(request)
    server_file_location=s.recv(1024)
    return server_file_location

if __name__ == "__main__":


    #testing writing a file to the server
    file_name="duhc.jpg"
    write_message="WRITE\n{}\n".format(file_name)
    write_file_to_server(write_message,file_name)
    #testing reading a file from the server
    read_message="READ\n{}\n".format(file_name)
    read_file_from_server(read_message,file_name)
    #testing reading a non existant file from the server
    fake_file_name="distributed.reallyfun"
    read_message="READ\n{}\n".format(fake_file_name)
    read_file_from_server(read_message,fake_file_name)




#connect to AS server
#send log on message to authenticator server

#once given ticket and session key atempt to transfer files with with normal service