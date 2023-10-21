
sum = 0
subtractor = 0 # for subtracting the sum of the common multiplies of 3 and 5

counter = 1

# 1000/3 is 333.33 repeating. 333 * 3 = 999
while(counter < 334):
    sum = sum + (3 * counter)
    # 1000/5 is 200
    if(counter < 200):
        sum = sum + (5 * counter)
    # 1000/15 is 66.66. 15 * 66 = 990.
    if(counter < 67):
        subtractor = subtractor + (15 * counter)
    counter += 1
sum = sum - subtractor
print(sum)