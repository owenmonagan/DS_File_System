from Crypto.Cipher import AES
from Crypto import Random
import logging

def encrypt_func(key, message):
    #print "AS: ABOUT TO ENCRYPT:{}".format(key)
    obj = AES.new(key, AES.MODE_CFB, 'This is an IV456')
    ciphertext=obj.encrypt(message)
    #print "AS: ENCRYPTED:{}".format(message)
    logging.info("Encrypted: {}".format(message))
    return ciphertext

def decrypt_func(key, encrypted_message):
    #print "AS: ABOUT TO DECRYPT:{}".format(key)
    obj= AES.new(key, AES.MODE_CFB, 'This is an IV456')
    message=obj.decrypt(encrypted_message)
    #print "AS: DECRYPTED:{}".format(message)
    logging.info("Decrypted: {}".format(message))
    return message
