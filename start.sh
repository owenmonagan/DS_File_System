#!/usr/bin/env bash
primary_port= $1

python SecurityService/authentication_server.py "0.0.0.0" $((primary_port+4))

python DirectoryService/Directory_server.py "0.0.0.0" $((primary_port+5))


python DistributedFileAccess/filesever.py True "0.0.0.0" primary_port primary_port
python DistributedFileAccess/filesever.py False "0.0.0.0" primary_port $((primary_port+1))
python DistributedFileAccess/filesever.py False "0.0.0.0" primary_port $((primary_port+2))
python DistributedFileAccess/filesever.py False "0.0.0.0" primary_port $((primary_port+3))
