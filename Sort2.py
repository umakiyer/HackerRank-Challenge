# Sort different method
arr=[1,2,3,1,1]
sortarr=[0]*99
for i in range(99):
    sortarr[i] = 0
for i in range(len(arr)):
    sortarr[arr[i]] = sortarr[arr[i]]+1 
for i in range(99):
    print(sortarr[i])  