import numpy as np
import matplotlib.pyplot as plt

duration = 10
x_0 = 0.0
v_0 = 2.0
F = 10.0
b = 0.5
m = 1.0
dt_values = [0.2, 0.1, 0.05, 0.01]
errors = []
dt = 0.05

def dynamics(v, F, m, b):
    """Compute the derivatives of position and velocity."""
    dxdt = v
    dvdt = (F - b * v) / m
    return dxdt, dvdt

#print(dynamics(4, 10, 2, 0))
#print(dynamics(4, 10, 2, 1))


def simulate(x_0, v_0, F, m, b, dt, duration):    
    """Simulate 1D motion using the forward Euler method."""
    x = x_0
    v = v_0
    steps = int(round(duration / dt))
    t = np.linspace(0, duration, steps + 1)
    position = [x_0]
    velocity = [v_0]
    # Integrate the equations of motion using forward Euler.
    for i in range(steps):
        dxdt, dvdt = dynamics(v, F, m, b)
        x = x + dxdt * dt
        v = v + dvdt * dt
        position.append(x)
        velocity.append(v)
        
    return(t, position, velocity)

t, position, velocity = simulate(
    x_0, v_0, F, m, b, dt, duration
)

#plt.plot(t, analytical_position, label="Analytical")
plt.plot(t, velocity, label="Velocity")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.grid()
plt.legend()
plt.show()