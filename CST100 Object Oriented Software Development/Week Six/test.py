## Robert McKinney
## Week 4 Assignment 4 Part 2

## ----------
## Encryption
## ----------

def encrypt_character(original_char, key):
    """Accept original character and key as parameters, return encrypted character"""
    original_char = ord(original_char)
    if (original_char + key > 126):
        return chr(original_char + key + 32 - 127)
    else:
        return chr(original_char + key)

def encrypt_string(message, key):
    """Accept string and key as parameter, return encrypted message"""
    result = ""
    for original_char in message:
        temp_char = ""
        temp_char = encrypt_character(original_char, key)
        result = result + temp_char
    return result

def encrypt_input_output():
    """Accept regular message and key from user, print encrypted message"""
    message = input("Enter a message to encrypt: ")
    key = int(input("Enter a key as an integer from 1 to 100: "))
    print("The encrypted message is: " + encrypt_string(message, key))


## ----------
## Decryption
## ----------

def decrypt_character(encrypted_char, key):
    """Accept encrypted character and key as parameters, return decrypted character"""
    encrypted_char = ord(encrypted_char)
    if (encrypted_char - key < 32):
        return chr(encrypted_char - key - 32 + 127)
    else:
        return chr(encrypted_char - key)

def decrypt_string(encrypted_message, key):
    """Accept encrypted message and key as parameters, return decrypted message"""
    result = ""
    for encrypted_char in encrypted_message:
        temp_char = ""
        temp_char = decrypt_character(encrypted_char, key)
        result = result + temp_char
    return result

def decrypt_input_output():
    """ Accept encrypted message from user, print possible decryptions"""
    encrypted_message = input("Enter an encrypted message you would like to decrypt: ")
    print("The following are the decrypted messages for keys 1 to 100: ")
    ##  For loop, range 1 through 100, to cycle through all keys
    for key in range(1, 101):
        decrypted_message = decrypt_string(encrypted_message, key)
        print("Key:", key, "-> Decoded Message: ", decrypted_message)


## -----------
## Run Program
## -----------

encrypt_input_output()
decrypt_input_output()






