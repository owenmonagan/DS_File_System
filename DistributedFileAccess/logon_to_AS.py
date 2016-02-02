import socket
#from SecurityService.authentication_server import auth_port, auth_host
from authentication import encrypt_func, decrypt_func

def logon(username,server_ip,server_port, password):
    s = socket.socket()         # Create a socket object
    s.connect(("0.0.0.0", 7074))
    login_message=generate_login_message(username,server_ip,server_port,password)
    s.send(login_message)
    Authentication_server_reply=s.recv(1024)
    decrypted_reply=decrypt_func(password,Authentication_server_reply)
    lines=decrypted_reply.split("\n")
    s.close()
    #returns ticket and session key
    return lines[0], lines[1]

def generate_login_message(username, serverIP,serverPort, password):
    serverinfo="{}\n{}".format(serverIP,serverPort)
    encrypted_message= encrypt_func( password, serverinfo)
    return "{}\n{}".format(username,encrypted_message)

def generate_request(ticket, session_key, message):
    encrypted_message=encrypt_func(session_key,message)
    final_request="{}\n{}".format(ticket,encrypted_message)
    return final_request