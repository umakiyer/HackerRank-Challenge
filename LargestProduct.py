# Largest product in an array
inputArray=[-23,4,-3,8,-12]
lenarr=len(inputArray)
large=-1000000
for i in range(lenarr-1):
    product=inputArray[i]*inputArray[i+1]
    if product > large :
        large=product
print(large)