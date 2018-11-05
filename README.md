#  Blaise de Vigenére Cipher
Cipher.py is a standalone Python creation of the [Vigenére cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher). It can be downloaded and ran in a Python 3 console.

## Summary:

A `message` is encrypted by using a `keyword`.
<br>Each letter within the `message` is shifted by the corresponding letter of the `keyword` to create the `ciphertext`.
<br>The `ciphertext` is decrypted by using the `keyword` to reverse the [Caesar ciphers](https://en.wikipedia.org/wiki/Caesar_cipher) of the `message`.

## Use:

#### 1. Selection
```
Encryption or Decryption?
```
Type either 'Encryption' or 'Decryption'. Captitalization does not matter.
> *'e', 'n', 'en' and 'encrypt' or 'd', 'de' and 'decrypt' are also accepted respectively.*

#### 2a. Encryption
```
Enter secret your message...
```
Type out the message you want to be encrypted.
> This cipher is **alphabetic only**. Capitalization will be converted to lowercase.
> <br>Punctuation, numbers, special characters and spaces **will all be removed!**

<br>

```
Enter the cipher key...
```
Enter a key for the encryption. The key must be at least as long as the original message.
<br>*Make sure to share this key with the recipient or store it for decryption!*
> Remember, This cipher is **alphabetic only**.
> <br>It is best if the key is as random as possible with little repetition.
> <br>Dictionary words are known to cause weaknesses in this encryption method.

<br>

```
Press Enter to encrypt
```
Any key will do really.

#### 2b. Decryption
```
Enter your encrypted message...
```
Enter the encrypted message.
> Capitalization does not matter.

<br>

```
Enter the cipher key...
```
Enter the key used to encrypt the original message.

<br>


```
Press Enter to encrypt
```
Let's hope everything goes well!

#### 3. Result
The output of the encryption or decryption will be displayed.
> Try different encryption keys to see the difference in the encryption!

## Conclusion:

I hope you enjoy! I had a great time building this cipher and hope you like it.
<br>Hopefully I can publish it as a webapp in the near future.
<br>The encryption method can certainly be improved upon but I wanted to stay true to the original design.

##### *Disclaimer for cryptographic the nitpicks:*

*This project is based on an article in Popular Science: The Secrets of Codes. The representation of a Vigenére cipher in the article uses `1` as the value for `A`. I used this as a guide for my project and thus `'a' + 'a' = 'b'` (or `1 + 1 = 2`). Although most [tabula rectas](https://en.wikipedia.org/wiki/Tabula_recta) represent `A` as `0`, representing `A` as `1` ensures that all characters are shifted.*
