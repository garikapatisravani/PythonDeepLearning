# Delete at least 2 characters, reverse the resultant string and print it.

# Converts the string to list
input = list(str(input("Enter a string: ")))

from random import randint
if len(input)>2:
    # Randomly delete two characters from list
    del input[randint(0,len(input)-1)]
    del input[randint(0,len(input)-1)]
    # reverse the list
    a=input[::-1]
    #converts list to string
    print("".join(a))
else:
    print("Length of the string should be greater than 2")