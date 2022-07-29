# Runner up score
n=5
arr=[2,3,5,8,5]
arr.sort()
first=arr[-1]
for i in range(n-1,-1,-1):
    if arr[i]!=arr[i-1]:
        second=arr[i-1]
        break
    else:
        continue
print (second)