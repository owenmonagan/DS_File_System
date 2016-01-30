def parse_add(request):
    lines= request.split("\n")
    file_name=lines[1]
    return file_name

def parse_find(request):
    lines= request.split("\n")
    file_name=lines[1]
    return file_name
