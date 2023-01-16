#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
# Input Format
# The first line contains . The second line contains an array   of  integers each separated by a space.
# Constraints
# 2 <= n <= 10
# -100 <= A[i] <= 100
# Output Format
# Print the runner-up score.
# Sample Input 0
# 5
# 2 3 6 6 5
# Sample Output 0
# 5
# Explanation 0
# Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up score.
n=int(input())
arr = map(int, input().split())
arr=list(arr)
arr.sort()
arr.reverse()
for i in range(0,n):
    if arr[i]>arr[i+1]:
        print(arr[i+1])
        break


