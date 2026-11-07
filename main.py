import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 101)
x_0 = 0.0
v_0 = 2.0
dt = 0.1
x = x_0
v = v_0
a = 1.0
position = [x_0]
velocity = [v_0]

def dynamics(v,a,x):
    dxdt = v
    dvdt = a
    return dxdt, dvdt

for i in range(100):
    dxdt, dvdt = dynamics(v, a, x)
    x = x + dxdt * dt
    v = v + dvdt * dt
    position.append(x)
    velocity.append(v)

print(f"Position: {x:.2f} m, Velocity: {v:.2f} m/s")
print(len(position), len(velocity))

plt.plot(t, position)
plt.xlabel('Time (s)')
plt.ylabel('Distance (m)')
plt.title('Motion of an Object at Constant Acceleration')
plt.grid()
plt.show()
