from Crypto.Cipher import AES
from Crypto import Random
import logging
#from SecurityService.encrypt_decrypt import decrypt_func
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

def encrypt_func(key, message):
    obj = AES.new(key, AES.MODE_CFB, 'This is an IV456')
    ciphertext=obj.encrypt(message)
    logging.info("Encrypted: {}".format(message))
    return ciphertext

def decrypt_func(key, encrypted_message):
    obj= AES.new(key, AES.MODE_CFB, 'This is an IV456')
    message=obj.decrypt(encrypted_message)
    logging.info("Decrypted: {}".format(message))
    return message