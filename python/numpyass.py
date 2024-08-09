import numpy as np

arr = np.arange(10).reshape(2,5)
print(arr)

print(np.max(arr))
#min max
maxele = np.max(arr,axis=1)
print(maxele)
#sorting
numb = np.array([
    [8,4,3],
    [7,5,6]])
print(numb)
sr=np.sort(numb,axis=1)# axis=0 for col sort
print(sr)
#
list =[
    np.array([3,2,8,9]),
    np.array([6,7,8,9]),
    np.array([6,9,9])
    ]

result=[]
for i in range((len(list))):
     result.append(np.mean(list[i]))
print("result",result)
#add row and col
arre=[
    ([3,2,8,9]),
    ([6,7,8,9])]

arra = np.array([3,2,8,9]),

revarray = np.flipud(arra)
print("revarray", revarray)

matrix1=[
    [3,4,5],
    [6,7,8],
    [2,3,9]
]
res=np.dot(matrix1,matrix1)
print(res)



























