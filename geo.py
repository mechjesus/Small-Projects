### IMPORTANT !!!!
###
### this is still very unstable. Always with the errors. Please bare with me. 
### For right now your key has to be numerical, some really wierd things will happen if you ignore this.
### I saw a computer set on fire once. I can't proove that a non numeric key generation started it,
### But I am pretty sure they have to be connected. Seriously, dont do it. 
### In the next couple days I will either fix that, or prevent the user from puting in non int. characters for the key.
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
    
    print encrypt # I will change this to pushing the information in its own document later, or making it a choice.# I will change this to pushing the information in its own document later, or making it a choice.

#Decryption option follows

elif taskask == 'decrypt':
   
    text = raw_input('Decrypt the following text: ')
   
    key = raw_input('Use the following key: ') #Note to future, until non int key bug is fixed, put an if statement here to precent them from doing so. 
   
    decrypt = ''.join(chr(ord(y)^ord(z)) for y,z in izip(text, cycle(key))) # refrence double hash comments to see what this is doing
   
    print 'Decrypted text follows: '
   
    print decrypt # I will change this to pushing the information in its own document later, or making it a choice. The key will be seperate.

#Decryption option follows

else:
   
    print 'That is not an opperation this program can run at this time. Please type encrypt or decrypt.'

# I will use libraries in the future for more input options from the user! Such options could be credits, purpose, how to win life etc....