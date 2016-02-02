#!/usr/bin/env bash

#primary_port = $1
#primary address = $1
python SecurityService/authentication_server.py "0.0.0.0" $(($1+4)) &

python DirectoryService/Directory_server.py "0.0.0.0" $(($1+5)) &

python DistributedFileAccess/fileserver.py True $1 "0.0.0.0" $1 &
python DistributedFileAccess/fileserver.py False $1 "0.0.0.0" $(($1+1)) &
python DistributedFileAccess/fileserver.py False $1 "0.0.0.0" $(($1+2)) &
python DistributedFileAccess/fileserver.py False $1 "0.0.0.0" $(($1+3)) &
