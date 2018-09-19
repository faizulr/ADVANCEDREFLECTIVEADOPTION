import string
from random import *
characters = string.ascii_letters + string.punctuation  + string.digits
pswd =  "".join(choice(characters) for x in range(randint(6, 14)))
print pswd
