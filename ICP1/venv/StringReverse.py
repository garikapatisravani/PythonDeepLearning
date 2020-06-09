string = list(str(input("Enter a string")))
from random import randint
print(len(string))
if len(string)>2:
    del string[randint(0,len(string)-1)]
    del string[randint(0,len(string)-1)]
    a=string[::-1]
    print("".join(a))
else:
    print ("Length of the string should be greater than 2")