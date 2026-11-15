# Cart Control Lab

A personal learning project focused on numerical simulation, dynamical systems, and control algorithms using Python.

## Project Goals

- Build a foundation in Python programming and numerical simulation.
- Understand dynamical system modeling and numerical integration.
- Progress toward PID, LQR, and Model Predictive Control (MPC).

## Current Implementation

- 1D motion with constant acceleration.
- Numerical integration using the Forward Euler method.
- Comparison with analytical solutions.
- Time-step sensitivity analysis.
- Numerical estimation of convergence order.

## Mathematical Model

The current system assumes constant acceleration:

\[
\dot{x} = v
\]

\[
\dot{v} = a
\]

The Forward Euler method approximates the system as:

\[
x_{k+1} = x_k + v_k \Delta t
\]

\[
v_{k+1} = v_k + a \Delta t
\]

## Results

Decreasing the integration time step reduces the numerical error. The current experiment demonstrates first-order convergence of the Forward Euler method.

## Requirements

- Python 3
- NumPy
- Matplotlib

## How to Run

Install dependencies:

```bash
pip install numpy matplotlib
```

Run the Python simulation script.

## Next Steps

- Introduce force, mass, and friction into the system model.
- Implement basic feedback control (PID).
- Explore state-space control and LQR.
- Implement a basic Model Predictive Controller.