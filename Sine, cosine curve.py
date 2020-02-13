#For this project, you will have a generate a sine vs cosine curve. 
#You will need to use the numpy library to access the sine and cosine functions. 
# You will also need to use the matplotlib library to draw the curve. 
# To make this more difficult, make the graph go from -360° to 360°, 
# with there being a 180° difference between each point on the x-axis.


import numpy as np
import matplotlib.pyplot as plt

#get value for x-ray:
deg = np.arange(-360,540,180)
#get sin value for y-ray:
sin_value = np.sin(deg)


plt.plot(deg, sin_value)
plt.title('sin wave')
plt.xlabel('degree')
plt.ylabel('sinvalue')
plt.grid(True, which ='both')
plt.axhline(y=0, color = 'k')
plt.show()

