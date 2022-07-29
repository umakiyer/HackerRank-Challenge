#ZigZag Sequence: Sort the given array in zigzag fashion.
#https://www.hackerrank.com/challenges/zig-zag-sequence/problem
a=[2,8,9,3,1,7,4,6,5,13,15]
a.sort()
print(a)
b=[0]*len(a)
mid=len(a)//2
last=len(a)-1
print(mid,len(a))
b[mid]=a[last]
for i in range(0,mid):
   b[i]=a[i]
   b[mid+i+1]=a[len(a)-i-2]
print(b)
