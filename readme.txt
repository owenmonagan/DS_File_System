This project features a working Authentication Server, Directory Server and File Server.
I have also implemented many of the features of primary copy replication and the bully algorithm
I got bogged down regarding issues with propogating updates to slaves.
Running the client shows working upload and download of files in AFS system.

To test the application in non-replication mode launch by:
NOTE: In its current state it is assumed that all hosts are the same Eg "0.0.0.0"
NOTE: Ensure ports are 4 digits in length

Authentication service (in SecurityService):
python authentication_server.py host port directory_port, file_port

Directory service (in DirectoryService):
python Directory_server.py host port authentication_port file_port


File service (in DistributedFileAccess):
IMPORTANT: TO TEST WITHOUT REPLICATION ENSURE : primary_port!=port
python fileserver.py host port authentication_port primary_port


Client (in Client):
python mainClient.py file_host, file_port, authentication_port, directory_port



REPLICATION (not working):

Authentication service (in SecurityService):
python authentication_server.py host port directory_port, primary_file_port

Directory service (in DirectoryService):
python Directory_server.py host port authentication_port primary_file_port


File service (in DistributedFileAccess):
IMPORTANT: MAKE FIRST FILESERVER A PRIMARY VIA : primary_port=port
python fileserver.py host port authentication_port primary_port

When Adding replication file servers follow this rule
this limits the number of replication servers and ensures the primary copy will be aware of it on start up.
primary_port<port where port<primary_port+10


Client (in Client):
python mainClient.py primary_host, primary_port, authentication_port, directory_port