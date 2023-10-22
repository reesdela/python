prev = 1
curr = 1
nth = 3
sumOfEven = 0

while((prev + curr) < 4000000):
    temp = curr
    curr = prev + curr
    prev = temp
    nth += 1
    if(curr % 2 == 0):
        sumOfEven += curr
print(f'nth {nth} value: {curr}')
print(sumOfEven)