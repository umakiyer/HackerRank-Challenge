# Boolean array
numbers = [8, 5, 6, 16, 5]
left = 1
right = 3
lennum = len(numbers)
result = [0]*lennum
t='true'
f='false'
lennum = len(numbers)
for i in range(lennum):
   
    x = numbers[i] % (i+1)
    y= numbers[i] / (i+1)
    
    if (x == 0) and (left <= y and right >= y):
        result[i]=t
       
    else:
         result[i]=f
print(result) 
