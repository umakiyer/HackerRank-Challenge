# tiny concatenation of two strings & find number of tiny string less than 'k'
def solution(a,b,k):
    soln=0
    for i in range(len(a)):
        tiny=str(a[i])+str(b[len(b)-1-i])
        print (tiny)
        if int(tiny) < k :
             soln=soln+1
    return soln
    
a=[1,2,3,4,5]
b=[1,2,3,4,5]
k=50
print(solution(a,b,k))