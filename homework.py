import numpy as np
array1=np.arange(1,21)
#first 5
print(array1[:5])
#last 5
print(array1[15:])
#3rd ones
print(array1[:20:3])
#reverse order
print(array1[::-1])
#All values <8
print(array1[array1<8])
#All values >=10
print(array1[array1 >=10])
#All odd values
print(array1[::2])
