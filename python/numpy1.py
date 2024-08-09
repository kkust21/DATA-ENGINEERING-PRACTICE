import random

import numpy as np

"""
arr1=np.array([[1,2,3],[4,5,6]])
print(arr1)
print(arr1.shape)
print(arr1.size)
rowvector = arr1[np.newaxis,:]
print("array",rowvector)
print(rowvector.shape)
colvector=arr1[:,np.newaxis]
print("arry", colvector)
print(colvector.shape)
"""
"""
arr2 = np.array([[1, 2, 3, ],
                 [6, 7, 8],
                 [10, 23, 4]])
#print(arr2[:2, :2])
#print(arr2[1:,2:])
"""
curve_center = 80
grades = np.array([56, 34, 89, 12])
average = grades.mean();
print(average)
change = curve_center - average
print(change)


def curves(grades):
    new_grades = grades + change
    return np.clip(new_grades, grades, 100)


curves(40)
"""
"""
temp = np.array([3, 4, 5, 6, 7, 8, 9, 7]).reshape(2, 2, 2)
print(temp)

print(np.swapaxes(temp, 2, 1))

bat_avg = np.array([
    [50, 30, 70],
    [20, 50, 60],
    [100, 70, 2]
])
print("size of array", bat_avg.shape)
print("Max Avg", bat_avg.max())
print("max avg col:", bat_avg.max(axis=0))
print("min avg row:", bat_avg.min(axis=1))

print(np.linspace(10, 40, 5, dtype=int))

num = np.arange(32).reshape(2, 4, 4)
print(num)

nums = np.arange(40).reshape(2, 5, 4)
print(nums)

numb = np.linspace(10, 40, 8, dtype=int).reshape(2, 2, 2)
print("num array:", numb)
mask = numb % 5 == 0  #vectoried boolen computerization
print("mark array:", mask)

#filtering
print("all the values divisible by 5 ", numb[mask])
print("number divisible by 8", numb[numb % 8 == 0])

print("num array:", numb)
trans = numb.T
print("transpose od number", trans)

number = [2, 3, 45, 6]

print("Horizontal Sorting", np.sort(number, axis=0))
#print("vertical Sorting", np.sort(number,axis=1))

a = np.array([[4, 8]])
b = np.array([[3, 5]])

concat = np.concatenate((b, a))
print(concat)

#identity matrix

im = np.eye(4)
print(im)

temparr = np.array([
                 [3,2,3,6,7],
                  [3,6,2,0,1]])
temp = temparr.astype('float')
tempe = temparr.astype('bool')
print(tempe)


























