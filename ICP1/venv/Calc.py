# Take two numbers from user and perform arithmetic operations on them

# To ask the user to enter two numbers
x=int(input("Enter the fist number:"))
y=int(input("Enter the second number:"))

# Performing basic arithmetic operations(Addition, Subtraction, Multiplication, Division)
addition = x+y
subtraction = x-y
multiplication = x*y
division = x/y

# Printing the result
print("Sum of",x,"and",y, "is", addition)
print("Difference of",x,"and",y, "is", subtraction)
print("Product of",x,"and",y, "is", multiplication)
print("Division of",x,"and",y, "is", division)
