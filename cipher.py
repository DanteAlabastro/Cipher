# import hashlib
# from hashlib import sha256
import re

# hash_key = sha256(str.encode(key)).hexdigest()

print('\n', '{:^80}'.format('Dante\'s de Vigenére cipher\n'))
print('{:^80}'.format('*Numbers, spaces and special characters are removed.*'))


# input
def user_input():
    toggle = True
    while toggle:
        input_text = input('\nEnter secret your message...')
        clean_text = re.sub('[^a-z]', '', input_text.lower())
        print(clean_text)

        input_key = input('\nEnter the cipher key...')
        clean_key = re.sub('[^a-z]', '', input_key.lower())

        while len(clean_key) < len(clean_text):
            print('\n', '{:^80}'.format('Please enter a cipher key longer than {} characters.'.format(len(clean_text))))
            print('{:^80}'.format('*Numbers, spaces and special characters are removed.*'))
            input_key = input('\nEnter the cipher key.')
            clean_key = re.sub('[^a-z]', '', input_key.lower())
        print(clean_key)

        input('\nPress Enter to encrypt...')
        cipher2(clean_text, clean_key)
        toggle = False


# With user input
def cipher2(text2, key2):
    ciphertext = []
    i = 0

    while i < len(text2):
        d = (ord(text2[i]) - 96) + (ord(key2[i]) - 96)
        if d > 26:
            # Subtract 26 and add 96
            ciphertext.append(chr(d + 70))
            i += 1
        else:
            ciphertext.append(chr(d + 96))
            i += 1

    joined_ciphertext = (''.join(ciphertext)).upper()
    print('\n', '{:^80}'.format('Your encrypted message is:'))
    print('\n', '{:^80}'.format(joined_ciphertext))

    return user_input()


user_input()

'''
# Testing Functions and params

# key
key = 'tests'

# Text
text = 'hello'

# Caesar cipher 'Character + int = chr(ord(a)+n)'
def caesar(amount):
    shifted = [chr(ord(i) + amount) for i in list(text)]
    print(''.join(shifted))


# Return
print(text)

print(key)

list1 = [1, 2, 3, 4]

list2 = [5, 6, 7, 8]

# 
# >>> a = ord('a') - 96
# >>> b = a + a
# >>> c = chr(b + 96)
# >>> print(c)
# 


# Add two characters
def letter_test(a, b):
    d = (ord(a) - 96) + (ord(b) - 96)
    if d > 26:
        # Subtract 26 and add 96
        print(chr(d + 70))
    else:
        print(chr(d + 96))

# Add two lists
def combine_lists():
    i = 0
    while i < len(list1):
        list1[i] += list2[i]
        i += 1
    print(list1)

# Shift text by key
def cipher():
    ciphertext = []
    i = 0
    while i < len(text):
        d = (ord(text[i]) - 96) + (ord(key[i]) - 96)
        if d > 26:
            # Subtract 26 and add 96
            ciphertext.append(chr(d + 70))
            i += 1
        else:
            ciphertext.append(chr(d + 96))
            i += 1
    print(''.join(ciphertext))


cipher()
'''