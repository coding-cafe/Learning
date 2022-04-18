# Most of the Matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias:

# Draw a line in a diagram from position (0,0) to position (6,250):
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 4])
ypoints = np.array([0, 200])

plt.plot(xpoints, ypoints)
plt.show()
