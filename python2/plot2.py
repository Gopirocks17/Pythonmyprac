import matplotlib.pyplot as plt

days=[1,2,3,4,5]

sleeping=[7,8,6,10,7]
eating=[2,3,1,3,2]
working=[10,11,9,8,9]
playing=[5,2,4,3,1]

plt.plot([],[],color='c',label='Sleeping',linewidth=5)
plt.plot([],[],color='m',label='Eating',linewidth=5)
plt.plot([],[],color='b',label='Working',linewidth=5)
plt.plot([],[],color='r',label='Playing',linewidth=5)


plt.stackplot(days,sleeping,eating,working,playing,colors=['C','Y','b','r'])

plt.xlabel('X-label')
plt.xlabel('Y-label')

plt.legend()
plt.title('Sample stack plot')

plt.show()
