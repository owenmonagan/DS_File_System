import socket               # Import socket module
from SecurityService.authentication_server import host, port
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


if __name__ == "__main__":
    s = socket.socket()         # Create a socket object
    s.connect((host, port))
    login_message=generate_login_message("owen","0.0.0.0",8040,"0123456789abcde1")
    s.send(login_message)
    Authentication_server_reply=s.recv(1024)
    print Authentication_server_reply



#connect to AS server
#send log on message to authenticator server

#once given ticket and session key atempt to transfer files with with normal service