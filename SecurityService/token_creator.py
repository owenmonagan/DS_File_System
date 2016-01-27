# Token: ticket, a session key, ID of the server for who the ticket is for, timeout period
def prepare_token(ticket,session_key,server_ID):
    #5000 is the timeout period
    token= "{}\n{}\n{}\n{}".format(ticket,session_key,server_ID,5000)
    return token




