import numpy as np
import matplotlib.pyplot as plt

duration = 10
last_outside = None
x_0 = 0.0
v_0 = 2.0
F = 10.0
b_values = [0.2, 0.5, 1.0]
m = 1.0
dt = 0.05
x_ref = 10
tolerance = 0.02 * abs(x_ref)
Kp = 2.0
Kd = 1


def dynamics(v, F, m, b):
    """Compute the derivatives of position and velocity."""
    dxdt = v
    dvdt = (F - b * v) / m
    return dxdt, dvdt

def controller(x, x_ref, Kp, v, Kd):
    F = Kp * (x_ref - x) - Kd * v
    return F

def simulate(x_0, v_0, x_ref, m, b, dt, duration, Kp, Kd):    
    """Simulate 1D motion using the forward Euler method."""
    x = x_0
    v = v_0
    steps = int(round(duration / dt))
    t = np.linspace(0, duration, steps + 1)
    position = [x_0]
    velocity = [v_0]
    # Integrate the equations of motion using forward Euler.
    for i in range(steps):
        F = controller(x, x_ref, Kp, v, Kd)
        dxdt, dvdt = dynamics(v, F, m, b)
        x = x + dxdt * dt
        v = v + dvdt * dt
        position.append(x)
        velocity.append(v)
        
    return(t, position, velocity)



for b in b_values:
    t, position, velocity = simulate(
    x_0=x_0,
    v_0=v_0,
    x_ref=x_ref,
    m=m,
    b=b,
    dt=dt,
    duration=duration,
    Kp=Kp,
    Kd=Kd,
)
    plt.plot(t, position, label=f"b = {b}")
    tao = m / b
    Mp = max(0, (max(position) - x_ref) / x_ref * 100)
    for i in range(len(position)):
        error = abs(position[i] - x_ref)

        if error > tolerance:
            last_outside = i
            settling_time = t[last_outside + 1]
    
    print(f"b = {b}, tao = {tao:.2f} s, Mp = {Mp:.2f} %")
    print(f"Settling Time is {settling_time:.2f} s")

plt.xlabel("Time (s)")
plt.ylabel("positions (m)")
plt.legend()
plt.grid()
plt.show()