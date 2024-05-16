from venv import logger
import bcrypt

def encrypt_password(password):
    """
    sets pass hash
    """
    # converting password to array of bytes 
    bytes = password.encode('utf-8') 
    
    # generating the salt 
    salt = b'$2b$12$WDt5z5jjsF6UW2fG7Ulz0O' 

    # Hashing the password 
    hash = bcrypt.hashpw(bytes, salt) 

    return hash

def decrypt_check_pass(usrPassword, dataBasePassword):
    
    # hash_to_vali = encrypt_password(dataBasePassword)
    hash_to_vali = dataBasePassword.encode('utf-8')
    bytes_object = usrPassword.encode('utf-8')

    logger.debug(f"{bytes_object} - bytes_object")
    print(f"bytes_object -> {bytes_object}")
    logger.debug(f"{hash_to_vali} - hash_to_vali")
    print(f"hash_to_vali -> {hash_to_vali}")

    result = bcrypt.checkpw(password=hash_to_vali, hashed_password=bytes_object)

    print(result)
    return result