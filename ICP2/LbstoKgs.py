# Author : Sravani Garikapati
#program reads weights (lbs.) of N students into a list and convert these weights to kilograms
# creating an empty list
lbs = []
kgs = []

# Ask user to enter no of students
n = int(input("Enter number of students : "))

# iterating till the range
# Using for loop
for i in range(n):
    ele = int(input("Enter the weight in lbs: "))
    lbs.append(ele)  # adding the element
    kgs.append(lbs[i]*0.453592)
print("Weight in kgs using for loop: ",kgs)

# Using list comprehension
li = [ i*0.453592 for i in lbs ]
print("Weight in kgs using list comprehension: ",li)