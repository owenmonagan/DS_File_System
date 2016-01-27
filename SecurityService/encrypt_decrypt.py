from Crypto.Cipher import AES
from Crypto import Random
import logging

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
