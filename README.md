# Cart Control Lab

A Python-based learning project exploring numerical simulation, dynamical systems, and feedback control, with the long-term goal of implementing Model Predictive Control (MPC).

The project follows a step-by-step approach, starting with simple one-dimensional motion and gradually introducing physical dynamics, feedback controllers, and optimization-based control.

## 1. Project Goals

- Develop practical Python programming skills.
- Understand mathematical modeling of dynamical systems.
- Implement and evaluate numerical integration methods.
- Design and compare feedback control algorithms.
- Progress toward LQR and Model Predictive Control (MPC).

## 2. Current Features

- One-dimensional cart simulation.
- Forward Euler numerical integration.
- Comparison with analytical solutions for constant-acceleration motion.
- Time-step sensitivity and convergence-order analysis.
- Force-based dynamics with mass and viscous friction.
- Proportional (P) and proportional-derivative (PD) position control.
- Visualization of position and velocity responses.
- Comparison of system behavior under different friction coefficients.

## 3. Mathematical Models

### 3.1 Constant-Acceleration Model

The initial model assumes constant acceleration:

\[
\dot{x}=v
\]

\[
\dot{v}=a
\]

The corresponding analytical solutions are:

\[
x(t)=x_0+v_0t+\frac{1}{2}at^2
\]

\[
v(t)=v_0+at
\]

This model was used to verify the numerical integration algorithm.

### 3.2 Force-Based Dynamics

The model was extended to include cart mass, applied force, and viscous friction:

\[
\dot{x}=v
\]

\[
\dot{v}=\frac{F-bv}{m}
\]

where:

- \(x\): Cart position (m)
- \(v\): Cart velocity (m/s)
- \(F\): Applied force (N)
- \(m\): Cart mass (kg)
- \(b\): Viscous friction coefficient (N·s/m)

This model allows the cart's acceleration to change dynamically according to its current velocity and applied force.

## 4. Numerical Integration

The system is simulated using the Forward Euler method:

\[
x_{k+1}=x_k+\dot{x}_k\Delta t
\]

\[
v_{k+1}=v_k+\dot{v}_k\Delta t
\]

where \(\Delta t\) is the integration time step.

### Error and Convergence Analysis

The constant-acceleration model was used to compare Euler integration with the analytical solution.

For a simulation duration of 10 seconds, initial velocity of 2 m/s, and acceleration of 1 m/s²:

| Time Step (s) | Final Position Error (m) |
|---|---|
| 0.20 | 1.00 |
| 0.10 | 0.50 |
| 0.05 | 0.25 |
| 0.01 | 0.05 |

The results demonstrate first-order convergence: halving the time step approximately halves the numerical error.

## 5. Feedback Control

### 5.1 Proportional Control (P)

The proportional controller computes the control force using the position error:

\[
F=K_p(x_{\mathrm{ref}}-x)
\]

where \(x_{\mathrm{ref}}\) is the target position and \(K_p\) is the proportional gain.

The simulations show that P control can cause the cart to overshoot and oscillate around the target because of its inertia.

### 5.2 Proportional-Derivative Control (PD)

Velocity feedback is introduced to provide additional damping:

\[
F=K_p(x_{\mathrm{ref}}-x)-K_dv
\]

where \(K_d\) is the derivative gain.

For a constant position reference, the velocity feedback term helps reduce oscillations and improve the system's transient response.

Setting \(K_d=0\) recovers the original P controller.

## 6. Simulation Architecture

The implementation separates the physical model, controller, and numerical simulation:

- `dynamics()`: Computes position and velocity derivatives.
- `controller()`: Calculates the control force based on position and velocity feedback.
- `simulate()`: Integrates the system dynamics using Forward Euler.
- Plotting and analysis: Visualizes system responses and compares parameters.

This modular structure will support future controller implementations.

## 7. Requirements

- Python 3
- NumPy
- Matplotlib

Install the required libraries:

```bash
python -m pip install numpy matplotlib
```

## 8. How to Run

Run the main simulation script from the project directory:

```bash
python main.py
```

The program runs the configured simulation and displays the resulting plots.

Simulation parameters, including mass, friction coefficient, control gains, and integration time step, can currently be modified directly in `main.py`.

## 9. Current Observations

- Smaller integration time steps improve the numerical accuracy of the Forward Euler method.
- Greater viscous friction reduces the steady-state velocity under a constant applied force.
- Friction also influences damping and transient response.
- P position control may produce oscillations around the target.
- PD control introduces velocity feedback to improve damping.

## 10. Development Roadmap

- [x] Implement constant-acceleration motion.
- [x] Implement Forward Euler integration.
- [x] Compare numerical and analytical solutions.
- [x] Analyze time-step sensitivity and convergence order.
- [x] Extend the model with mass, force, and viscous friction.
- [x] Implement P position control.
- [x] Implement the PD control law.
- [ ] Compare P and PD performance for different derivative gains.
- [ ] Evaluate overshoot, settling time, and steady-state error.
- [ ] Introduce control force and velocity constraints.
- [ ] Implement state-space modeling and LQR.
- [ ] Implement a basic Model Predictive Controller (MPC).
- [ ] Compare controller performance and computational cost.
- [ ] Explore 3D visualization and future ROS 2 integration.

## 11. Project Status

**Work in progress — currently developing and evaluating classical feedback control.**

This project is intended as a progressive learning and experimentation platform rather than a production-ready control system.