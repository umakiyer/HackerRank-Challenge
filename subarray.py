# function to find a subarray which adds up to a given number
# store the start and end index of the subarray
def subarray(arr,n,s):
    # initialize start and end index
    start = 0
    end = 0
    # initialize sum
    sum = 0
    # loop through the array
    for i in range(n):
        # add the current element to the sum
        sum += arr[i]
        # if the sum is greater than the given sum
        if sum > s:
            # subtract the current element from the sum
            sum -= arr[start]
            # increment the start index
            start += 1
        # if the sum is equal to the given sum
        elif sum == s:
            # set the end index to the current index
            end = i
            # break the loop
            break
    # if the sum is not greater than the given sum
    if sum < s:
        # return -1
        return -1
    # return the start and end index
    return start,end

arr=[1,2,3,7,5]
n=5
s=15
print(subarray(arr,n,s))

 
