directory_host, directory_port= "0.0.0.0", 6666



auth_host, auth_port= "0.0.0.0", 9998

file_host1, file_por1="0.0.0.0", 7771
file_host2, file_por2="0.0.0.0", 6563
file_host3, file_por3="0.0.0.0", 9966
file_host4, file_por4="0.0.0.0", 8632


#start.sh script
#file server arg[1], arg[2] arg[3]
#file server primary_copy=true primary_address address

#run multiple file servers
#start file server, file server becomes primary after sending election message to all fileservers and not receiving a reply
#start second file server, and set primary copy to original