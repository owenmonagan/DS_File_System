# Token: ticket, a session key, ID of the server for who the ticket is for, timeout period
from encrypt_decrypt import encrypt_func
from datetime import datetime,timedelta
def prepare_token(ticket,session_key,server_ID):
    token= "{}\n{}\n{}".format(ticket,session_key,server_ID)
    return token

def prepare_ticket(server_key, session_key):
    ticket_expiration=datetime.now()+timedelta(0,0,0,0,10)
    ticket= encrypt_func(server_key,"{}\n{}".format(session_key,ticket_expiration))
    return ticket




