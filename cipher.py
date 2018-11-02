# import hashlib
# from hashlib import sha256

# hash_key = sha256(str.encode(key)).hexdigest()

# input - strip white space and punctuation. all lowercase.

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

# '''
# >>> a = ord('a') - 96
# >>> b = a + a
# >>> c = chr(b + 96)
# >>> print(c)
# '''


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
