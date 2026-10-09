import numpy as np

# python list
numbers = [10, 20, 30, 40]
print (numbers)

numbers = np.array([10,20,30, 40])
print (numbers)

#Accessing array elements
print (numbers [0])
print(numbers [2])
print (numbers [-1])

print(numbers + 5)
print (numbers * 2)
print (numbers / 10)

marks = np.array([85,90,78,92, 88])

print("Total:", np. sum(marks))
print("Average:", np.mean (marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))

marks = np. array([
[85,90,78],
[92, 88,95],
[76,80,84] ])

