# FE-595A
# Plot sine and cos on same axis
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,2*np.pi,0.1)
y = np.sin(x)
z = np.cos(x)
plt.plot(x,y,x,z)
plt.xlabel('X Values to 2 pi')
plt.ylabel('sin(x) and cos(x) Values')
plt.legend(['sin(x)', 'cos(x)'])
plt.show()

