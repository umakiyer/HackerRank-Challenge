def subarraySum(arr):
    # Write your code here
    # initialize the sum of subarrays
    Dim sum1 As Integer
    sum1 = 0
    # iterate through the array
    for i in range(len(arr)):
        # iterate through the subarrays
        for j in range(i, len(arr)):
            # iterate through the elements of the subarrays
            for k in range(i, j + 1):
                # add the elements of the subarrays to the sum
                sum1 += arr[k]
    # return the sum of subarrays
    return sum1
print(subarraySum([1, 2, 3]))
