import logging


def write_file(socket, write_string):
    logging.info("\n\nWriting file started")
    file_name =parse_write_info(write_string)
    socket.request.send("Ready to write {} to the server".format(file_name))
    downloading_and_writing(socket,file_name)

def parse_write_info(write_string):
    lines=write_string.split("\n")
    file_name= lines[1].strip("\n")
    logging.info("{} to be added to the server".format(file_name))
    return file_name

def downloading_and_writing(socket,file_name):
    file = open('{}'.format(file_name),'w')
    logging.info("File opened and beginning download")
    chunk=socket.request.recv(1024)
    while (chunk):
        logging.info("Downloading...")
        file.write(chunk)
        print chunk
        chunk=socket.request.recv(1024)
    file.close()
    socket.request.send("{} has been successfully uploaded".format(file_name))
    logging.info("Writing File Complete")
