from parse_strings import parse_find

def find_file(directory, request):
    file_name = parse_find(request)
    try:
        locations=directory[file_name]
        return locations[0]
    except:
        return None

    #if(locations):
        #currently returning the first location in the list
        #to be upgraded with replication
    #    return locations[0]
    #else:
    #    return None