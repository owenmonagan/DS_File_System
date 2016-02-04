import logging

password_database=[("owen","0123456789abcde1")]

def add_key(id, password):
    password_database.append((id,password))
    logging.info("{} added to the password_database".format(id))

def find_key(id):
    #the if statement is used in replication
    #if it is a primary copy atempting to talk to its replicas.
        #the Primary copy has the password of "012345678replica"
    if(not "fileserver" in id):
        tuple=[item for item in password_database if item[0]==id]
        return tuple[0][1]
    else:
        #Return a key that replicas and the primary copy use to interact
        #return "0123456789abcdef"
        return        "012345678replica"

def add_server(server_id, key,server_database):
    server_database.append((server_id,key))
    logging.info("{} added to the password_database".format(server_id))
    return server_database

def find_server_key(server_id,server_database):
    #Checks if there is a server matching the tuple of (host, port)
    # then extracts the key and returns it
    tuple=[item for item in server_database if item[0]==server_id]
    #print tuple
    return tuple[0][1]