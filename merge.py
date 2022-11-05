# merging a sorted list consisting of K elements witha sorted list consisting of L elements takes (K+L) milliseconds(ms)
# the time required to erge more than 2 lists into one final list depends on the order in which the lists are merged.
# for example, if we have 3 lists, A, B, and C, and we merge them in the order A+B, then B+C, then A+B+C, the total time required to merge all 3 lists is 2*(K+L)+3*(L+M) ms.
# if we merge them in the order A+B, then A+B+C, then B+C, the total time required to merge all 3 lists is 2*(K+L)+3*(K+M) ms.
# if we merge them in the order A+B+C, then A+B, then B+C, the total time required to merge all 3 lists is 3*(K+L)+2*(K+M) ms.
# given a non-empty zero-indexed array A consisting of N integers, returns the minimum time required to merge all the elements into a single sorted list.
# For example , consider the following three lists:
# lis P consisting of 100 elements
# list Q consisting of 250 elements
# list R consisting of 1000 elements
# They can be mergerd in the following ways:
# first merge P& Q, then merge the result with R
# merge P with Q :350 ms; result with R: 1350 ms; total time: 1700 ms
# first merge P& R, then merge the result with Q
# merge P with R: 1100 ms; result with Q: 1350 ms; total time: 2450 ms
# first merge Q& R, then merge the result with P
# merge Q with R: 1250 ms; result with P: 1350 ms; total time: 2600 ms
# write a function:
# def solution(A)
# that, given an array of length N describing the lengths of N lists. returns the shortest time r( measured in milliseconds) required to merge all the lists into a single sorted list.
# for example, given A=[100,250,1000], the function should return 1700, as explained above.
# Write an efficient algorithm for the following assumptions:
# N is an integer within the range [0..10,000];
# each element of array A is an integer within the range [1..1000];
# For example A[0]=100, A[1]=250, A[2]=1000
# the function should return 1700, as explained above.
# Write an efficient algorithm for the following assumptions:
# N is an integer within the range [0..10,000];
# each element of array A is an integer within the range [1..1000];
# def solution(A):
#     # write your code in Python 3.6
#     # given an array A of N integers, returns the minimum time required to merge all the elements into a single sorted list.
#     # for example, given A=[100,250,1000], the function should return 1700, as explained above.
#     # Write an efficient algorithm for the following assumptions: 
def solution(A):
    # write your code in Python 3.6
    # given an array A of N integers, returns the minimum time required to merge all the elements into a single sorted list.
    # for example, given A=[100,250,1000], the function should return 1700, as explained above.
    # Write an efficient algorithm for the following assumptions:
    # N is an integer within the range [0..10,000];
    # each element of array A is an integer within the range [1..1000];
    # sort the array
    A.sort()
    # find the minimum time required to merge all the elements into a single sorted list
    # if the length of the array is 1, return 0
    if len(A) == 1:
        return 0
    # if the length of the array is 2, return the sum of the elements
    elif len(A) == 2:
        return A[0] + A[1]
    # if the length of the array is greater than 2, return the sum of the first two elements plus the sum of the first three elements plus the sum of the first four elements and so on
    else:
        sum = 0
        prev_sum = 0
        for i in range(len(A)):
            prev_sum=sum
            sum += A[i] 
            print (sum+prev_sum)
        return sum
    pass
A=[100,250,1000]
solution(A)
# print(solution(A))