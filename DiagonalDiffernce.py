# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
arr= [[1,2,4],[1,2,3],[1,2,3]]
lenarr=len(arr)
rev=0
sum1=0
sum2=0
sum=0
for i in range(lenarr):
    rev=lenarr-i-1
    sum1=sum1+arr[i][i]
    sum2=sum2+arr[rev][i]
sum=abs(sum1-sum2)
print(sum)