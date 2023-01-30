# Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/
# By: Osvaldo A. Ramirez
# 2019-10-28
# Language: Python3
# Tested on: Python 3.7.4
# Time to solve: 0:15:00
# Tags: arrays, subarray, sum, k, leetcode
# Resources:
# https://leetcode.com/problems/subarray-sum-equals-k/discuss/341399/Python-O(n)-solution-with-detailed-explanation
# subarraySum has the following parameters:
#     int nums[n]: an array of integers to process
# returns:
#     int: an integer repreenting the sum of all subarrays of the given array
#    
# Given an array of integers, find the the sum of all elemnts of the subarrays of that array
# array = [1, 2, 3]
# subarrays = [[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]
# sum of subarrays = 1 + 1 + 2 + 1 + 3 + 2 + 3 = 13
# optimize the code
# constraints:
#     1 <= n <= 2*10^5
#     1 <= nums[i] <= 1000, where 0 <= i < n
# the first line contains an integer n, the number of elements in the array
# the second line contains n space-separated integers nums[i], where 0 <= i < n
# allowed time limit is 10 seconds

def subarraySum(arr):
    # initialize variables
    # sum of all subarrays
    sum = 0
    # dictionary to store the sum of all subarrays
    # key: sum of subarray
    # value: number of times that sum of subarray has been found
    subarraySum = {}
    # sum of subarray
    subarraySum[0] = 1
    # sum of all elements of the array
    totalSum = 0
    # iterate through the array
    for i in range(len(arr)):
        # sum of all elements of the array
        totalSum += arr[i]
        # if the sum of all elements of the array minus the sum of the subarray is in the dictionary
        if totalSum - arr[i] in subarraySum:
            # add the number of times that sum of subarray has been found to the sum of all subarrays
            sum += subarraySum[totalSum - arr[i]]
        # if the sum of all elements of the array minus the sum of the subarray is not in the dictionary
        else:
            # add the sum of all elements of the array minus the sum of the subarray to the dictionary
            subarraySum[totalSum - arr[i]] = 0
        # add 1 to the number of times that sum of subarray has been found
        subarraySum[totalSum - arr[i]] += 1
    # return the sum of all subarrays
    return sum