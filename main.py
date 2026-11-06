import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 100)
v = 2.0

x = v * t

plt.plot(t, x)
plt.xlabel('Time (s)')
plt.ylabel('Distance (m)')
plt.title('Motion of an Object at Constant Velocity')
plt.grid()
plt.show()
