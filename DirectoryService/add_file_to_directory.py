from parse_strings import parse_add
#from DistributedFileAccess.fileserver import file_host, file_port

def add_file(directory, request, file_location):
    file_name= parse_add(request)
    #if directory has an entry of the file name, add the file to the list, then remove duplicates (set())
    try:
        directory[file_name]
        directory[file_name]=directory['file_name'].append(file_location)
        set(directory[file_name])
    except:
        directory[file_name]=[file_location]

    return directory


def find_suitable_server():
    #curently just returns the file server, needs to be updated for replication
    return (file_host, file_port)


#cycles through the servers selecting the new server to upload a file too
def balance_adding_file_to_servers(servers,count):
    newCount=0
    if(count==len[servers]):
       newCount=0
    else:
        newCount=count+1
    return servers[count], newCount








def find_server(directory, server_id):
    server_position=-1
    count=0;
    for position in directory:
        if position[0]==server_id:
            server_position=count
        else:
            count=count+1

    return server_position

#use a dict
#hash each file name
#store server/directory, filename

def notused(directory, server_id , file_name):

    server_position=find_server(directory, server_id)
    if(server_position>-1):
        server_directory=directory[server_position]
        server_directory[1].append(file_name)
        set(server_directory[1])
        directory[server_position]=server_directory
        return directory
    else:
        directory.append((server_id, [file_name]))
        return directory

    #searchforserver
    #iffound then append file
    #then set the files
    #else
    #append the new tupel ("server_id", [filename])