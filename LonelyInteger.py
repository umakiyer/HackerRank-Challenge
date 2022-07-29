#Given an array of integers, where all elements but one occur twice, find the unique element.
arr=[1,2,3,7,3,2,1]
unique=0
for i  in range(0,len(arr)):
    count=0
    for j in range(0, len(arr)):
        if arr[i]==arr[j]:
            count=count+1
    if count == 1 :
        unique = arr[i]
print(unique)

