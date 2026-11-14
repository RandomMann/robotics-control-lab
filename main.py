import numpy as np
import matplotlib.pyplot as plt

duration = 10
dt = 0.05
x_0 = 0.0
v_0 = 2.0
a = 1.0

def dynamics(v,a):
    dxdt = v
    dvdt = a
    return dxdt, dvdt

def simulate(x_0, v_0, a, dt, duration):
    x = x_0
    v = v_0
    steps = int(round(duration / dt))
    t = np.linspace(0, duration, steps + 1)
    position = [x_0]
    velocity = [v_0]

    for i in range(steps):
        dxdt, dvdt = dynamics(v, a)
        x = x + dxdt * dt
        v = v + dvdt * dt
        position.append(x)
        velocity.append(v)
        
    return(t, position, velocity)

t, position, velocity = simulate(x_0, v_0, a, dt, duration)
t1, p1, v1 = simulate(0, 2, 1, 0.1, 10)
t2, p2, v2 = simulate(0, 2, 1, 0.05, 10)
analytical_position = x_0 + v_0 * t + 0.5 * a * t**2
analytical_velocity = v_0 + a * t
error = abs(analytical_position[-1] - position[-1])

print(error)
plt.plot(t1, p1, label="Euler1")
plt.plot(t2, p2, label="Euler2")
plt.plot(t, analytical_position, label="Analytical")
plt.xlabel('Time (s)')
plt.ylabel('Distance (m)')
plt.title('Motion of an Object at Constant Acceleration')
plt.grid()
plt.legend(loc="upper left")
plt.show()
