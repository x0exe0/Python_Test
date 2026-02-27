import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parameter sistem
a1 = -9       # gain nonlinear (mirip -ωn^2)
a2 = -3       # damping
b1 = 2        # gain elevator

def elevator_input(t):
    return 0.1

def pitch_dynamics_nonlinear(t, x):
    theta = x[0]
    q = x[1]
    delta_e = elevator_input(t)

    dtheta_dt = q
    dq_dt = a1 * np.sin(theta) + a2 * q + b1 * delta_e

    return [dtheta_dt, dq_dt]

# kondisi awal
x0 = [0.2, 0]  # misal awalnya 0.2 rad (~11 deg)
t_span = (0, 10)
t_eval = np.linspace(0, 10, 1000)

sol = solve_ivp(pitch_dynamics_nonlinear, t_span, x0, t_eval=t_eval)

theta = sol.y[0]
q = sol.y[1]

# Plot theta vs time
plt.figure()
plt.plot(sol.t, theta)
plt.xlabel("Time (s)")
plt.ylabel("Pitch Angle θ (rad)")
plt.title("Nonlinear Theta vs Time")
plt.grid()
plt.show()

# Plot phase
plt.figure()
plt.plot(theta, q)
plt.xlabel("Theta (rad)")
plt.ylabel("Pitch Rate q (rad/s)")
plt.title("Nonlinear Phase Plot")
plt.grid()
plt.show()