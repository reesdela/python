import matplotlib.pyplot as plt

x = [-3, -2, -1, 0, 1, 2, 3]
y = []
x1 = [-3, -2, -1, 0, 1, 8, 6]
y2 = []

for num in x:
    y.append(3*num + 2)

for num in x1:
    y2.append(3*num + 3)


plt.plot(x,y)
plt.plot(x1,y2)

plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.title('lines with same slope (3) are parellel')

plt.show()