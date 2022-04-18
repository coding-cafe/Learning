# Markers
# You can use the keyword argument marker to emphasize each point with a specified marker:

# Example
# Mark each point with a circle, star etc.

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, marker = 'o') 
plt.plot(ypoints, marker = '*') 


plt.show()