#there is a road consisting of N segments, numbered from 0 to N-1, represented by a string S.
#Segment S[K] of the road may contain pothole, denoted by a single uppercase letter'X
# or it may be a good segment, denoted by a single dot'.'.
# for example , string ".X..XX" represents a road with 5 segments:
# the road fixing machine can patch over three consecutive segments at once with asphalt and repaid all the potholes in those segments.
# for example, the road above could be repaired with two patches: one covering segments 1,2,3 and the other covering segment 4,5.
# write a function:
# def solution(S)
# that, given a string S representing the road, returns the minimum number of patches that need to be applied to the road so that all segments of the road are good.

# for example, given S = ".X..XX", the function should return 2.The road fixing machine could patch , for example, segments 0-2 and 2-4
# given S = "....", the function should return 0.
# given S = "X.XXXXX.X", the function should return 3. the road fixing machine could patch, for example, segment 0-2 ,3-5 and 6-8.
# given S = "XX.XXX..", the function should return 2. The road fixing machine could patch , for example, segments 0-2 and 3-5.
# given S="XXXX",your function should return 2, The road fixing machine could patch segments 0-2 and 1-3
# assume that:
# N is an integer within the range [3..100,000]
# string S consists only of the characters'.' and/or 'X'.
# complexity:
# expected worst-case time complexity is O(N)
# expected worst-case space complexity is O(1) (not counting the storage required for input arguments)
def solution(S):
    # write your code in Python 3.6
    # find the number of patches
    patches = 0
    # find the number of potholes
    potholes = 0
    # find the number of good segments
    good_segments = 0
    # find the number of segments
    segments = len(S)
    # find the number of potholes
    for i in range(segments):
        if S[i] == 'X':
            potholes += 1
    # find the number of good segments
    good_segments = segments - potholes
    # find the number of patches
    if good_segments == 0:
        patches = 1
    else:
        patches = (potholes // good_segments) + 1
    return patches
S="XXXX"
print(solution(S))