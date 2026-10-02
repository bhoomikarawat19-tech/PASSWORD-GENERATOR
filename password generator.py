import random 
import string 
length=int(input("length of the password: "))

chars=(string.ascii_letters
        +string.digits
        +string.punctuation)
password="".join(random.choice(chars)
for i in range(length)
)
print("password: \n")
print (password)