import logging
#from DirectoryService.Directory_server import directory_server_key, directory_host,directory_port
#from DistributedFileAccess.fileserver import file_server_key, file_host,file_port

#host="0.0.0.0"
#port=4300
#((host,port+1),"0123456789ab{}".format(port+1)),((host,port+5),"0123456789ab{}".format(port+5))
#server_database=[]
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
        #return "0123456789abcdef"
        return        "012345678replica"

def add_server(server_id, key,server_database):
    server_database.append((server_id,key))
    logging.info("{} added to the password_database".format(server_id))
    return server_database

def find_server_key(server_id,server_database):
    #print "searching for {}".format(server_id)
    #print "SERVER DATABASE"
    #print server_database
    #print "\n\n"
    tuple=[item for item in server_database if item[0]==server_id]
    print tuple
    return tuple[0][1]