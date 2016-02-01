import logging

def parse_message(request_string):
    lines=request_string.split("\n")
    encyripted_message=lines[1].strip("\n")
    id=lines[0].strip("\n")
    logging.info("Encrypted message from {} has been parsed".format(id))
    return encyripted_message, id