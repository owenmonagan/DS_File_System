import socket               # Import socket module
from DistributedFileAccess.server_address_info import host, port
s = socket.socket()         # Create a socket object
#host = socket.gethostname() # Get local machine name
#port = 12345                 # Reserve a port for your service.

s.connect((host, port))
file_name='duhc.jpg'
s.send("READ\n{}\n".format(file_name)) #sned write request
#f = open(file_name,'rb')

ready_to_recv_response=s.recv(1024)
print("Server: {}".format(ready_to_recv_response))

file = open('{}'.format(file_name),'w')
chunk=s.recv(1024)
while (chunk and not chunk=="\n"):
    file.write(chunk)
    print "downloading"
    chunk=s.recv(1024)
file.close()
print s.recv(1024)