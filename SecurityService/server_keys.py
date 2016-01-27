import logging

server_database=[(("0.0.0.0",8040),"0123456789abcde2")]

def add_server(server_id, key):
    server_database.append((server_id,key))
    logging.info("{} added to the password_database".format(server_id))

def find_server_key(server_id):
    tuple=[item for item in server_database if item[0]==server_id]
    print tuple
    return "0123456789abcde2"