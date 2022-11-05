#there is a road consisting of N segments, numbered from 0 to N-1, represented by a string S.
#Segment S[K] of the road may contain pothole, denoted by a single uppercase letter'X
# or it may be a good segment, denoted by a single dot'.'.
# for example , string ".X..XX" represents a road with 5 segments:
# segment 0: good segment
# segment 1: pothole
# segment 2: good segment
# segment 3: good segment
# segment 4: pothole
# segment 5: pothole
# the goal is to compute the minimum number of patches that need to be applied to the road so that all segments of the road are good.
# a patch is a contiguous segment of the road that is covered with a single layer of asphalt.
# for example, the road above could be repaired with two patches: one covering segments 1,2,3 and the other covering segment 4,5.
# write a function:
# def solution(S)
# that, given a string S representing the road, returns the minimum number of patches that need to be applied to the road
#  so that all segments of the road are good.
# for example, given S = ".X..XX", the function should return 2.
# given S = "....", the function should return 0.
# given S = "XXXX", the function should return 1.
# given S = ".X.X....X", the function should return 3.
# assume that:
# N is an integer within the range [3..100,000]

# string S consists only of the characters'.'and'X'.
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
        patches = potholes // good_segments + 1
    return patches

S=".X..XX"
print(solution(S))