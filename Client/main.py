import socket               # Import socket module
from DistributedFileAccess.server_address_info import host, port
s = socket.socket()         # Create a socket object
#host = socket.gethostname() # Get local machine name
#port = 12345                 # Reserve a port for your service.

s.connect((host, port))
file_name='dog.jpg'
s.send("WRITE\n{}\n".format(file_name)) #sned write request
f = open(file_name,'rb')

ready_to_send_response=s.recv(1024)
print("Server: {}".format(ready_to_send_response))

l = f.read(1024)
print
while (l):
    print 'Sending...'
    print l
    s.send(l)
    l = f.read(1024)
f.close()
print "Done Sending"
s.shutdown(socket.SHUT_WR)
print s.recv(1024)
s.close