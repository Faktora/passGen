import random
import string
import sys
import os

Letters = string.ascii_letters
Numbers = string.digits
Punctuation = string.punctuation
Length = int(sys.argv[1])


def passwordGeneration(size):
    printable = f'{Letters}{Numbers}{Punctuation}'
    
    printable = list(printable)
    random.shuffle(printable)
    
    random_password = random.choices(printable, k=size)
    random_password = ''.join(random_password)
    
    return random_password


print(passwordGeneration(Length))
os.system('pause')
