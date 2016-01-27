import logging

def parse_message(request_string):
    lines=request_string.split("\n")
    encyripted_message=lines[0].strip("\n")
    user_id=lines[1].strip("\n")
    logging.info("Encrypted message from {} has been parsed".format(user_id))
    return encyripted_message, user_id