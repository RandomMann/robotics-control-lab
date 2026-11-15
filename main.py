import numpy as np
import matplotlib.pyplot as plt

duration = 10
x_0 = 0.0
v_0 = 2.0
a = 1.0
dt_values = [0.2, 0.1, 0.05, 0.01]
errors = []


def dynamics(v,a):
    """Compute the derivatives of position and velocity."""
    dxdt = v
    dvdt = a
    return dxdt, dvdt

def simulate(x_0, v_0, a, dt, duration):
    """Simulate 1D motion using the forward Euler method."""
    x = x_0
    v = v_0
    steps = int(round(duration / dt))
    t = np.linspace(0, duration, steps + 1)
    position = [x_0]
    velocity = [v_0]
    # Integrate the equations of motion using forward Euler.
    for i in range(steps):
        dxdt, dvdt = dynamics(v, a)
        x = x + dxdt * dt
        v = v + dvdt * dt
        position.append(x)
        velocity.append(v)
        
    return(t, position, velocity)


# Evaluate the final position error for different time steps.
for dt in dt_values:
    t, position, velocity = simulate(x_0, v_0, a, dt, duration)
    analytical_position = x_0 + v_0 * t + 0.5 * a * t**2
    error = abs(analytical_position[-1] - position[-1])
    errors.append(error)
    print(f"dt = {dt}, final position = {position[-1]:.2f}")
    print(f"error = {error}")

# Estimate the convergence order from two time-step sizes.
order = np.log(errors[0] / errors[1]) / np.log(dt_values[0] / dt_values[1])
print(order)

#plt.plot(t, analytical_position, label="Analytical")
plt.plot(dt_values, errors, marker="o", label="Euler error")
plt.xlabel('Time step dt (s)')
plt.ylabel('Final position error (m)')
plt.title('Euler Error Convergence')
plt.grid()
plt.legend(loc="upper left")
plt.show()
