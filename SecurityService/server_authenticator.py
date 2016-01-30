from SecurityService.encrypt_decrypt import decrypt_func
from datetime import datetime

def authenticate(server_key,request_message):
    lines=request_message.split("\n")
    ticket=lines[0]
    encrypted_message=lines[1]
    print(request_message)
    session_key_and_ticket_expiration =decrypt_func(server_key,ticket)
    session_key=session_key_and_ticket_expiration.split("\n")[0]
    ticket_expiration=session_key_and_ticket_expiration.split("\n")[1]
    if(datetime.strptime(ticket_expiration,"%Y-%m-%d %H:%M:%S.%f")>datetime.now()):
        message=decrypt_func(session_key,encrypted_message)
        return message
    else:
        return "Expired Ticket"