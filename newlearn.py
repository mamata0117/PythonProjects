# we can use sqrt() or **0.5 or math.sqrt() to calculate the square root in python
print('The square root of 5 is',5**0.5)
import math
print('The square root of 6 is',math.sqrt(6))
from math import sqrt
print('The square root of 7 is',sqrt(7))
#mutable and immutable data types in python
# some mutable data types in python are list, set, dictionary,etc. mutable data types can be modified after they are created.
mylist=[1,2,3]
print('Original list:',mylist)
mylist.append(4)
print('Modified list:',mylist)
mytuple=(1,2,3)
print('Original tuple:',mytuple)
# mytuple.append(4) will give an error because tuples are immutable and cannot be modified after they are created.
# some immutable data types in python are int, float, string, tuple,etc.
# () is used to create a tuple, [] is used to create a list and {} is used to create a dictionary in python.