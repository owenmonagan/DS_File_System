import socket               # Import socket module
from SecurityService.authentication_server import host, port
from DistributedFileAccess.server_address_info import file_host, file_port
from SecurityService.encrypt_decrypt import encrypt_func,decrypt_func

#host = socket.gethostname() # Get local machine name
#port = 12345                 # Reserve a port for your service.

#USERNAME
#ENCYRPITED
    #SERVERIP
    #SERVERPORT

def generate_login_message(username, serverIP,serverPort, password):
    serverinfo="{}\n{}".format(serverIP,serverPort)
    encrypted_message= encrypt_func( password, serverinfo)
    return "{}\n{}".format(username,encrypted_message)

def generate_request(ticket, session_key, message):
    encrypted_message=encrypt_func(session_key,message)
    final_request="{}\n{}".format(ticket,encrypted_message)
    return final_request


if __name__ == "__main__":
    #start logon
    s = socket.socket()         # Create a socket object
    s.connect((host, port))
    login_message=generate_login_message("owen","0.0.0.0",8040,"0123456789abcde1")
    s.send(login_message)
    Authentication_server_reply=s.recv(1024)
    #print Authentication_server_reply
    decrypted_reply=decrypt_func("0123456789abcde1",Authentication_server_reply)
    lines=decrypted_reply.split("\n")
    print decrypted_reply
    print decrypt_func("0123456789abcde2",lines[0])
    print "\n\n"

    print decrypted_reply
    s.close()

    #start read
    file_name='duhc.jpg'
    request=generate_request(lines[0],lines[1],"READ\n{}\n".format(file_name))
    file_socket= socket.socket()
    file_socket.connect((file_host,file_port))
    file_socket.send(request)
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
    #encrypt message/request for file server with session key
    #add the encrypted ticket to the encrypted message
    #send the combined message in format ticket+encrypted message
    #s.send()



#connect to AS server
#send log on message to authenticator server

#once given ticket and session key atempt to transfer files with with normal service