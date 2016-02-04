#!/usr/bin/env bash

#primary_port = $1
#primary address = $1
python SecurityService/authentication_server.py "0.0.0.0" $(($1+4)) &

python DirectoryService/Directory_server.py "0.0.0.0" $(($1+5)) &

<<<<<<< HEAD

#sleep 5

python DistributedFileAccess/fileserver.py True $1 "0.0.0.0" $1 &
python DistributedFileAccess/fileserver.py False $1 "0.0.0.0" $(($1+1)) &
#python DistributedFileAccess/fileserver.py False $1 "0.0.0.0" $(($1+2)) &
#python DistributedFileAccess/fileserver.py False $1 "0.0.0.0" $(($1+3)) &
=======
sleep 7  # Waits 5 seconds.
#                               isPrimary PrimaryPort FileHost FilePort AuthPort
python DistributedFileAccess/fileserver.py True  $1 "0.0.0.0" $1        $(($1+4)) &
python DistributedFileAccess/fileserver.py False $1 "0.0.0.0" $(($1+1)) $(($1+4)) &
python DistributedFileAccess/fileserver.py False $1 "0.0.0.0" $(($1+2)) $(($1+4)) &
python DistributedFileAccess/fileserver.py False $1 "0.0.0.0" $(($1+3)) $(($1+4)) &

sleep 5 #waits 5 seconds

python Client/mainClient.py $1 &
>>>>>>> replication_concept
