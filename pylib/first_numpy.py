import numpy as np 
# Creating an array using np.array() method 
arr = np.array([10, 20, 30, 40, 50]) 
# Printing 
print(arr)

# more than one dimensions 
import numpy as np 
a = np.array([[1, 2], [3, 4], [5,6],[8,7],[9,10]]) 
print(a)

import numpy as np  
a = np.array([1, 2, 3, 4, 5], ndmin = -2) 
# Printing 
print(a)

import numpy as np  
a = np.array([1, 2, 3, 4, 5], dtype = complex) 
# Printing 
print(a)

import numpy as np
a = np.arange(0,60,5)
a = a.reshape(3,4)
print('Original array is:')
print(a)
print('\n')
print('Modified array is:')
for x in np.nditer(a):
   print(x)

import numpy as np
a = np.arange(0,60,5)
a = a.reshape(3,4)
print('Original array is:')
print(a)
print('\n')
print('Transpose of the original array is:')
b = a.T
print(b)
print('\n')
print('Modified array is:')
for x in np.nditer(b):
   print(x)
