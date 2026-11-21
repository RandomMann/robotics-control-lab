import numpy as np
import matplotlib.pyplot as plt

duration = 10
x_0 = 0.0
v_0 = 2.0
b = 0.5
m = 1.0
dt = 0.05
x_ref = 10
tolerance = 0.02 * abs(x_ref)
Kp = 2.0
Kd_values = [0.2, 1.0, 3.0]

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
    A = np.array([
    [0, 1],
    [0, -b / m]
 ])

    B = np.array([
    [0],
    [1 / m]
 ])

    position = [x_0]
    velocity = [v_0]
    steps = int(round(duration / dt))
    t = np.linspace(0, duration, steps + 1)

    state = np.array([
    [x_0],
    [v_0]
 ])

 # Integrate the equations of motion using forward Euler.
    for i in range(steps):
        x = state[0, 0]
        v = state[1, 0]
        F = controller(x, x_ref, Kp, v, Kd)
        dxdt, dvdt = dynamics(v, F, m, b)
        state_dot = A @ state + B * F
        state = state + dt * state_dot
        position.append(state[0,0])
        velocity.append(state[1,0])
        
    return(t, position, velocity)

for Kd in Kd_values:
    t, position, velocity = simulate(
    x_0=x_0,
    v_0=v_0,
    x_ref=x_ref,
    m=m,
    b=b,
    dt=dt,
    duration=duration,
    Kp=Kp,
    Kd=Kd
)
    plt.plot(t, position, label=f"Kd = {Kd}")

    steady_state_error = abs(x_ref - position[-1])
    print(f"Final Position Error = {steady_state_error:.8f} m")

    # Calculate the open-loop velocity time constant (s)
    tao = m / b

    # Calculate percentage overshoot relative to the target position.
    Mp = max(0, (max(position) - x_ref) / x_ref * 100)

    last_outside = None
    for i in range(len(position)):
        error = abs(position[i] - x_ref)

        if error > tolerance:
            last_outside = i

    if last_outside is None:
        settling_time = 0.0
    elif last_outside == len(position) - 1:
        settling_time = None
    else:
        settling_time = t[last_outside + 1]

    print(f"Kd = {Kd}, Mp = {Mp:.2f} %")
    if settling_time is None:
        print("Settling Time is not detected")
    else:
        print(f"Settling Time is {settling_time:.2f} s")

plt.axhline(y=x_ref, linestyle="--", label="Reference")
plt.xlabel("Time (s)")
plt.ylabel("positions (m)")
plt.legend()
plt.grid()
plt.show()