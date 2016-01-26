
def write_file(socket, write_string):
    file_name =parse_write_info(write_string)
    check_for_file(file_name)
    socket.request.send("Ready to write {} to the server".format(file_name))
    downloading_and_writing(socket,file_name)

def check_for_file(file_name):
    #return if file exists in the location
    pass

def parse_write_info(write_string):
    lines=write_string.split("\n")
    file_name= lines[1].strip("\n")
    print(file_name)
    return file_name

def downloading_and_writing(socket,file_name):
    file = open('{}'.format(file_name),'w')
    chunk=socket.request.recv(1024)
    while (chunk):
        print "received chunk"
        file.write(chunk)
        print chunk
        chunk=socket.request.recv(1024)
    print "finished chunk loop"
    file.close()
    socket.request.send("{} has been successfully uploaded".format(file_name))
