'''
#import matplotlib
#matplotlib.use('Agg')
#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt


x=[12,14,18,25,30]
c=['r','b','m','y','g']
plt.pie(x,colors=c)
plt.show()
#plt.savefig('fig1')
'''

import matplotlib.pyplot as plt
x = [10,20,30,40,50]
y = [100,200,300,400,500]
plt.plot(x,y)   #Plot functionality will plot the values of x against y.
plt.show()     #show functionality will display the plotted graph in a native window.

