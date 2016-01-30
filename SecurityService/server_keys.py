import logging
from DirectoryService.Directory_server import directory_server_key, directory_host,directory_port
from DistributedFileAccess.fileserver import file_server_key, file_host,file_port


server_database=[((file_host,file_port),file_server_key),((directory_host,directory_port),directory_server_key)]

def add_server(server_id, key):
    server_database.append((server_id,key))
    logging.info("{} added to the password_database".format(server_id))

def find_server_key(server_id):
    tuple=[item for item in server_database if item[0]==server_id]
    print tuple
    return tuple[0][1]