#Interesting Polygon from CodeSignal
n=5
area=0
for i in range(n*2):
    if i % 2 != 0:
        area=area+2*i
area=area-(2*n-1)
print(area)