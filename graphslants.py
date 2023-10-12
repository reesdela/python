import matplotlib.pyplot as plt

x1 = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
y1 = [3, 4, 5, 6, 7, 8, 9, 10, 11]

x2 = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
y2 = [-3, -4, -5, -6, -7, -8, -9, -10, -11]

plt.subplot(1, 2, 1)
plt.plot(x1,y1)

plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.title('slants upward from left to right (positive slope). As x increases y increases.')

plt.subplot(1, 2, 2 )
plt.plot(x2, y2)
plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.title('slants downward from left to right (negative slope). As x increases y decreases.')
plt.show()