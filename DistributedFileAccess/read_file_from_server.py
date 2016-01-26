import logging

def read_file(socket, read_string):
    logging.info("\n\nReading file started")
    file_name =parse_read_info(read_string)
    socket.request.send("Ready to read {} to the client".format(file_name))
    upload_read_to_user(socket,file_name)

def parse_read_info(read_string):
    lines=read_string.split("\n")
    file_name= lines[1].strip("\n")
    logging.info("{} to be added to the server".format(file_name))
    return file_name

def upload_read_to_user(socket, file_name):
    file = open('{}'.format(file_name),'rb')
    logging.info("File opened and beginning upload")
    chunk = file.read(1024)
    socket.request.send(chunk)
    while (chunk):
        logging.info("uploading...")
        chunk = file.read(1024)
        socket.request.send(chunk)
    file.close()
    socket.request.send("\n")
    socket.request.send("{} has been successfully downloaded".format(file_name))
    logging.info("Reading File Complete")