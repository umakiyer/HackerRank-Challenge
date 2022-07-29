#zigzag where a[0] >a[1] <a[2]
def solution(numbers):
    result=[0]*(len(numbers)-2)
    for i in range(len(numbers)-2):
        j=i+1
        k=j+1
        if numbers[i]<numbers[j] and numbers[j]>numbers[k]:
            print(numbers[i],numbers[j],numbers[k])
            result[i]=1
        elif numbers[i]>numbers[j] and numbers[j]<numbers[k]:
            print(numbers[i],numbers[j],numbers[k])
            result[i]=1
    return result

zigzag=solution([6,4,7,2,3])
print(zigzag)

