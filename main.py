import numpy as np
import matplotlib.pyplot as plt

dt = 0.05
steps = int(round(10 / dt))
t = np.linspace(0, 10, steps + 1)
x_0 = 0.0
v_0 = 2.0
x = x_0
v = v_0
a = 1.0
position = [x_0]
velocity = [v_0]

def dynamics(v,a):
    dxdt = v
    dvdt = a
    return dxdt, dvdt

for i in range(steps):
    dxdt, dvdt = dynamics(v, a)
    x = x + dxdt * dt
    v = v + dvdt * dt
    position.append(x)
    velocity.append(v)

analytical_position = x_0 + v_0 * t + 0.5 * a * t**2
analytical_velocity = v_0 + a * t

error = abs(analytical_position - position)

#print(f"Position: {x:.2f} m, Velocity: {v:.2f} m/s")
print(error[-1])
print(max(error))

plt.plot(t, position, label="Euler")
plt.plot(t, analytical_position, label="Analytical")
plt.xlabel('Time (s)')
plt.ylabel('Distance (m)')
plt.title('Motion of an Object at Constant Acceleration')
plt.grid()
plt.legend(loc="upper left")
plt.show()
