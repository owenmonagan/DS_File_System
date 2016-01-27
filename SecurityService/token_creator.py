# Token: ticket, a session key, ID of the server for who the ticket is for, timeout period
from encrypt_decrypt import encrypt_func
def prepare_token(ticket,session_key,server_ID):
    #5000 is the timeout period
    token= "{}\n{}\n{}\n{}".format(ticket,session_key,server_ID,5000)
    return token

def prepare_ticket(session_key, server_key):
    ticket= encrypt_func(session_key,session_key)
    return ticket




