### IMPORTANT !!!!

### For right now your key has to be numerical, some really wierd things will happen if you ignore this.
### I saw a computer set on fire once. I can't proove that a non numeric key generation started it,
### But I am pretty sure they have to be connected. Seriously, dont do it. 

## Ignore the emptytripple hashtags, those are for personal reminders of where I am activley working

# itertools lets me xor non intigers which is needed. 
from itertools import cycle, izip

# Program greting

print 'Welcome to GeoCryptr! '
###
def initial():
###
    taskask = raw_input('encrpyt or decrypt?')

    print taskask

    #Nitty Gritty
    #Encryption option follows

    if taskask == 'encrypt'.lower() : 
    
        text = raw_input('Encrypt the following text: ')
    
        key = raw_input('Use the following key: ')
    
        encrypt = ''.join(chr(ord(a)^ord(b)) for a,b in izip(text, cycle(key))) 
    
        print'Encrypted text follows: ' 
    
        print encrypt # I will change this to pushing the information in its own document later, or making it a choice.# I will change this to pushing the information in its own document later, or making it a choice.

    #Decryption option follows

    elif taskask == 'decrypt'.lower():
   
        text = raw_input('Decrypt the following text: ')
   
        key = raw_input('Use the following key: ') #Note to future, until non int key bug is fixed, put an if statement here to precent them from doing so. 
   
        decrypt = ''.join(chr(ord(y)^ord(z)) for y,z in izip(text, cycle(key))) # refrence double hash comments to see what this is doing
   
        print 'Decrypted text follows: '
   
        print decrypt # I will change this to pushing the information in its own document later, or making it a choice. The key will be seperate.

    # People who dont follow directions will get this

    else:
   
        print 'That is not an opperation this program can run at this time. Please type encrypt or decrypt.'

###
def goagain():
    return raw_input("Do you have another task for geocryptr?").lower() == "yes"
### 
###
while True:
    initial()
    if not goagain(): break
###
###
print 'Thank you for using geocryptr! Have a good day.'
###

# I will use libraries in the future for more input options from the user! Such options could be credits, purpose, how to win life etc....
