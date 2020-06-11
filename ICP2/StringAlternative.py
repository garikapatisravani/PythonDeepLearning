# Author : Sravani Garikapati
# program that returns every other char of a given string starting with first
# Ask user to enter a string
s = str(input("Enter a string: "))

# Use slicing to get every other character of string
def string_alternative(s):
  print(s[::2])

if __name__ == '__main__':
    string_alternative(s)
