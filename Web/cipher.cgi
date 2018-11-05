#!/usr/bin/env python3
print("Content-type: text/html\n\n")

import cgi
import cgitb
cgitb.enable()

import sys
import os

# We append the python path so that you can do import from your own mypylabs.
mypylabs_dir = os.path.join(os.path.expanduser('~'), 'mypylabs')
sys.path.append(mypylabs_dir)

import mynamespack

import cipherpack

import cipherpack.cipher

form = cgi.FieldStorage()

mystring = form.getvalue('mystring', '')
lastnames = form.getvalue('lastnames', '')
firstnames = form.getvalue('firstnames', '')

cleartext = form.getvalue('cleartext','')
key = form.getvalue('key','')
key2 = form.getvalue('key2','')
ciphertext = form.getvalue('ciphertext', '')


PAGE = """
<html>
  <head>
    <title>Vigenere Cipher by Dante A.</title>
    <link rel="stylesheet" type="text/css" href="/~dalabast/cs131a/css/labstyle.css">
  </head>

  <body>
    <h1>de Vignere Cipher</h1>
    <h4>coding by {author} for {course}</h4>    
  <a name='encrypt'></a>
  <form id="encrypt" method='POST'>
    <fieldset><legend>Encryption</legend>
	<p>Enter a message to send: 
    <input type='text' name='cleartext' value='{cleartext}' size='40' />
    </p>
	<p>Enter a key to encrypt the message: 
    <input type='text' name='key' value='{key}' size='40'/>
    </p>
	<h5>Be aware: All capitalization, punctuation, numbers and special characters are removed from all fields.</h5>
    <p><input type='submit' value='Encrypt!' onClick="location.href='cipher.cgi#encrypt'"> </p>
  </form>
    <fieldset><legend>output</legend>
    <table>
		<tr><th>Message</th><td>{clean_cleartext}</td></tr>
        <tr><th>Encryption Key</th><td>{clean_key}</td></tr>
		<tr><th>Encrypted Message</th><td>{encrypt}</td></tr>
    </table>
    </fieldset>
    </fieldset>
  <a name='decrypt'></a>
  <form id ="decrypt" method='POST'>
    <fieldset><legend>Decryption</legend>
	<p>Enter the encrypted message: 
    <input type='text' name='ciphertext' value='{ciphertext}' size='40' />
    </p>
    <p>
    Enter the key used for encryption: 
    <input type='text' name='key2' value='{key2}' size='40' />
	</p>
    <p><input type='submit' value='Decrypt!' onClick="location.href='cipher.cgi#decrypt'"> </p>
  </form>
    <fieldset><legend>output</legend>
    <table>
        <tr><th>Ciphertext</th><td>{ciphertext}</td></tr>
        <tr><th>Key</th><td>{clean_key2}</td></tr>
        <tr><th>Decrypted Message</th><td>{decrypt}</td></tr>
    </table>
    </fieldset>
    </fieldset>
	
</body>
</html>
"""

d = dict()

d['cleartext'] = cleartext
d['key'] = key
d['key2'] = key2
d['ciphertext'] = ciphertext
d['clean_cleartext'] = cipherpack.cipher.clean(cleartext)
d['clean_key'] = cipherpack.cipher.clean(key)
d['clean_key2'] = cipherpack.cipher.clean(key2)

d['encrypt'] = cipherpack.cipher.user_input(cleartext, key)
d['decrypt'] = cipherpack.cipher.user_input_decrypt(ciphertext, key2)

d['style'] = 'h1, h2, h3 {color: black}; '
d['style'] += 'th {color: black};'

# Hills server local import
d['author'] = mynamespack.__author__
d['course'] = mynamespack.__course__
print(PAGE.format(**d))

