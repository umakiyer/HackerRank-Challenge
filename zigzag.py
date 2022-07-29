#zigzag
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

zigzag=solution([1,2,3,4])
print(zigzag)

