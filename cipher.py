import hashlib
from hashlib import sha256

letter = 'a'
n = 1
# input - strip white space and punctuation. all lowercase.

# key
key = 'tests'
hash_key = sha256(str.encode(key)).hexdigest()

# key as list
keyL = list(key)

# key fit text len
key_fit = 1

# Text
text = 'hello'

# Encrypted  'Character + int = chr(ord(a)+n)'
encrypted = [chr(ord(i) + ord('s') - 90) for i in list(text)]

# Return
print(text)
print(''.join(encrypted))


# '''
# >>> a = ord('a') - 96
# >>> b = a + a
# >>> c = chr(b + 96)
# >>> print(c)
# '''


# Add two characters

def c(a, b):
    d = (ord(a) - 96) + (ord(b) - 96)
    if d > 26:
        # Subtract 26 and add 96
        print(chr(d + 70))
    else:
        print(chr(d + 96))


def encrypt():
    for i in text:
        print(i)


encrypt()

list1 = [1, 2, 3, 4]

list2 = [5, 6, 7, 8]

# Add two lists
def combine_0():
    i = 0
    while i < len(list1):
        list1[i] += list2[i]
        i += 1
    print(list1)


def combine_1():
    i = 0
    while i < len(list1):
        list1[i] += list2[i]
        i += 1
    print(list1)

def combine_2():
    cipher = []
    i = 0
    while i < len(text):
        d = (ord(text[i]) - 96) + (ord(key[i]) - 96)
        if d > 26:
            # Subtract 26 and add 96
            cipher.append(chr(d + 70))
            i += 1
        else:
            cipher.append(chr(d + 96))
            i += 1
    print(''.join(cipher))


# cipher[i] = chr(ord(text[i]) + ord(key[i]))
