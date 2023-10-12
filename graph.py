import matplotlib.pyplot as plt

x = [-3, -2, -1, 0, 1, 2, 3]
y = []
for num in x:
    y.append(num*num)


plt.plot(x,y)

plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.title('graph')

plt.show()