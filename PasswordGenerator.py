# importing libraries needed to generate random input

import random 
from string import digits, punctuation, ascii_letters


# setting variables for password length, symbols included in password, ...

length = 18
symbols = ascii_letters + digits + punctuation
secure = random.SystemRandom()


# choosing random symbol length times 

password = "".join(secure.choice(symbols) 
            for i in range(length)
            )


# printing out result

print(password)
