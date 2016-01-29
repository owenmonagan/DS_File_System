def parse_add(request):
    lines= request.split("\n")
    file_location=lines[1]
    file_name=lines[2]
    return file_location, file_name

def parse_find(request):
    lines= request.split("\n")
    file_name=lines[1]
    return file_name