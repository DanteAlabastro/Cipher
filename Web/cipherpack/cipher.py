BLANK = ''

import re


# Test
def test(word):
    return word


def clean(i):
    input = i
    clean_input = re.sub('[^a-z]', '', input.lower())
    return clean_input


# Input for encryption
def user_input(m, k):
    input_text = m
    input_key = k

    clean_text = re.sub('[^a-z]', '', input_text.lower())
    clean_key = re.sub('[^a-z]', '', input_key.lower())

    if len(clean_key) < len(clean_text):
        return 'Please enter a cipher key longer than {} characters. Numbers, spaces and special characters are removed.'.format(
            len(clean_text))

    return encrypt(clean_text, clean_key)


# Input for decryption
def user_input_decrypt(c, k):
    input_text = c
    clean_text = re.sub('[^a-z]', '', input_text.lower())

    input_key = k
    clean_key = re.sub('[^a-z]', '', input_key.lower())

    if len(clean_key) < len(clean_text):
        return 'Please enter a cipher key longer than {} characters. Numbers, spaces and special characters are removed.'.format(
            len(clean_text))

    return decrypt(clean_text, clean_key)


# Encrypt user input with key
def encrypt(text2, key2):
    ciphertext = []

    for i in range(len(text2)):
        d = (ord(text2[i]) - 96) + (ord(key2[i]) - 96)
        if d > 26:
            # Subtract 26 and add 96
            ciphertext.append(chr(d + 70))
            i += 1
        else:
            ciphertext.append(chr(d + 96))
            i += 1

    joined_ciphertext = (''.join(ciphertext)).upper()

    return joined_ciphertext


# Decrypt ciphertext based on key
def decrypt(encrypted, key):
    cleartext = []

    for i in range(len(encrypted)):
        d = (ord(encrypted[i]) - 96) - (ord(key[i]) - 96)
        if d < 0:
            # Add 26 and 96
            cleartext.append(chr(d + 122))
            i += 1
        else:
            cleartext.append(chr(d + 96))
            i += 1

    joined_cleartext = (''.join(cleartext)).upper()
    return joined_cleartext
