### IMPORTANT !!!!
###
### this is still very unstable. Always with the errors. Right now trying no spaced lower case entries with numerals for a key.
### I could make it where the user HAS to do this, but I would rather try and fix it. Sometimes multi all case words
### work, however I have not gotten to be able to figure out why yet. Please bare with me. 
### Also I will make it to where you dont need to relaunch it everytime, this will be mostly for bugtesting purposes. 

## Quick note on some of the things used later in the code. 
## This was a very difficult undertaking that required much outside studying which became harder and harder to do.
## However this was not in vain, as I learned tons about python and what I can potentially do with it.
## A few things I would like to note at the start as it would become messy to do at the points in the code.
## I had to discover how to use .join() which basically just combines things together which is super usefull when using XOR.
## cycle() from itertools is something I only fundamentaly understand to be honest, but it is feeding information from the
## key continously (repeating in case of an end) in this program. I had to enlist help from my friend Viking on how to get 
## it to work right here. 
## ord() and chr() are used in the changing of plain text to unicode and vice versa. Easy to mix up, dont it.
## these double hash comments will be deleted when I present this at lecture on thursday. 




# itertools lets me xor non intigers which is needed. 
from itertools import cycle, izip

# Program greting that will also let the program know what the user intends to use it for this time

print 'Welcome to GeoCryptr! '

taskask = raw_input('encrpyt or decrypt?')

print taskask

#Nitty Gritty

#Encryption option follows

if taskask == 'encrypt': 
    
    text = raw_input('Encrypt the following text: ')
    
    key = raw_input('Use the following key: ')
    
    encrypt = ''.join(chr(ord(a)^ord(b)) for a,b in izip(text, cycle(key))) # refrence double hash comments to see what this is doing
    
    print'Encrypted text follows: '
    
    print encrypt

#Decryption option follows

elif taskask == 'decrypt':
   
    text = raw_input('Decrypt the following text: ')
   
    key = raw_input('Use the following key: ')
   
    decrypt = ''.join(chr(ord(y)^ord(z)) for y,z in izip(text, cycle(key))) # refrence double hash comments to see what this is doing
   
    print 'Decrypted text follows: '
   
    print decrypt

#Decryption option follows

else:
   
    print 'That is not an opperation this program can run at this time. Please type encrypt or decrypt.'

# I will use libraries in the future for more input options from the user! Such options could be credits, purpose, how to win life etc....