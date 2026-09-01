import numpy as np

array1=np.array([1,2,3,4,5,6,7,8])
print(array1)

print(array1[0])

#slicing operator(last number always excluded)
print(array1[0:5])

#you can also do just :5 to mean from the start to the extra number that gets excluded
print(array1[:5])

#even though there are only 8 elements and the array starts with 0, since the last number isnt included i can make a pseudo-limit
print(array1[5:8])

#i can do 5: to mean 1st number to the end
print(array1[5:])

#**concept of array slicing:[start:end:count by]
print(array1[0:8:2])

#to reverse an array, put ::-1
print(array1[::-1])

#multi-dimensional array
array2=np.array([[1,2,3],[4,5,6],[7,8,9]])
#to access a specific value in a multidimensional array, i have to do print(array name[mini array index value][value in mini array])
print(array2[1][1])
print(array2[2][0])
print(array2[0][2])
#to cutout the rest of the square, i do the same

print(array2[0:2, 0:2])
#when using the np.arange function to stack numbers to the excluded end, i shouldnt use square brackets
array3=np.arange(1,50).reshape(7,7)
print(array3)
print(array3[2:5, 2:5])

k=np.array([1,2,3,4,5,6,7,8,9,10])
evenArray=k[k%2 ==0]
print(evenArray)

oddArray=k[k%2 != 0]
print(oddArray)

print(k[k==5])
print(k[k==500])
print(k[k <5])

a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9,10])
#when printing arrays added by each other, identical index values are added together
#but the arrays have to be the same size to work!
print(a+b)
print(a-b)
print(a/b)
print(a*b)


def linearEquation(x):
    y=(2*x)+3
    print(y)

linearEquation(5)

