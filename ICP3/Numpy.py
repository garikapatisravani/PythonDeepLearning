import random  # imports random module
import numpy as np # imports numpy module

# Random vector of size 20 having only Integers in the range 1-20.
a = np.random.randint(1, 20, size=20)

# Reshapes the array to 4 by 5
b = a.reshape(4, 5)
print(b)

# Replaces the max in each row by 0
c = np.where(b == np.max(b, axis=1).reshape(-1, 1), 0,b)
print(c)