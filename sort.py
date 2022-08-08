# sort an array of numbers
# # sort array functions such that it returen a list of sorted numbers
# # sort array functions such that it returen a list of sorted numbers
array=[3,2,5,3,1] 
def sort(array):
    sortarr=[0]*99
    for i in range(99):
        sortarr[i] = 0
    for i in range(len(array)):
        sortarr[array[i]] = sortarr[array[i]]+1 
    for i in range(len(array)):
        print(sortarr[i])  
    return sortarr

sorted=sort(array)
print(sorted)