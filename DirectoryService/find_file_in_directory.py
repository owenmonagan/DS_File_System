from parse_strings import parse_request

def find_file(directory, request):

    locations=directory[file_name]
    if(locations):
        #currently returning the first location in the list
        #to be upgraded with replication
        return locations[0]
    else:
        return None