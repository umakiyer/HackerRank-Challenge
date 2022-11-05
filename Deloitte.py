def solution(A):
    # write your code in Python 3.6
    # given an array a of n numbers, return the smallest positive integer( greated than 0) that does not occur in a
    # for example, given a = [1,3,6,4,1,2], the function should return 5
    # given a = [1,2,3], the function should return 4
    # given a = [-1,-3], the function should return 1
    # assume that:
    # n is an integer within the range [1..100,000]
    # each element of array a is an integer within the range [-1,000,000..1,000,000]
    # complexity:
    # expected worst-case time complexity is O(n)
    # expected worst-case space complexity is O(n) (not counting the storage required for input arguments)
    # sort the array
    A.sort()
    # find the smallest positive integer
    for i in range(len(A)):
        if A[i] > 0:
            break
    # if the smallest positive integer is not 1, return 1
    if A[i] != 1:    
        return 1    
    # if the smallest positive integer is 1, find the smallest positive integer that does not occur in a
    else:
        for j in range(i,len(A)):
            if A[j] != A[j-1] + 1:
                return A[j-1] + 1
        return A[-1] + 1
            
    # write your code in Python 3.6
    pass
