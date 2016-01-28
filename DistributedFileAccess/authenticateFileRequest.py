from SecurityService.encrypt_decrypt import decrypt_func
server_key="0123456789abcde2"

def authenticate(request_message):
    lines=request_message.split("\n")
    ticket=lines[0]
    encrypted_message=lines[1]
    print(request_message)
    session_key =decrypt_func(server_key,ticket)
    message=decrypt_func(session_key,encrypted_message)
    return message