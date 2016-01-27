import logging

password_database=[]

def add_user(user_id, password):
    password_database.append((user_id,password))
    logging.info("{} added to the password_database".format(user_id))

def find_user_password(user_id):
    tuple=[item for item in password_database if item[0]==user_id]
    return tuple[1]