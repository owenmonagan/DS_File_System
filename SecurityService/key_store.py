import logging
from DirectoryService.Directory_server import directory_server_key, directory_host,directory_port
from DistributedFileAccess.fileserver import file_server_key, file_host,file_port

server_database=[((file_host,file_port),file_server_key),((directory_host,directory_port),directory_server_key)]
password_database=[("owen","0123456789abcde1")]

def add_key(id, password):
    password_database.append((id,password))
    logging.info("{} added to the password_database".format(id))

def find_key(id):
    if(not "server" in id):
        tuple=[item for item in password_database if item[0]==id]
        return tuple[0][1]
    else:
        #Return a key that replicas and the primary copy use to interact
        return "012345678replica"





def add_server(server_id, key):
    server_database.append((server_id,key))
    logging.info("{} added to the password_database".format(server_id))

def find_server_key(server_id):
    tuple=[item for item in server_database if item[0]==server_id]
    print tuple
    return tuple[0][1]