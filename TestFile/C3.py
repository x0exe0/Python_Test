import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# ------------------------------
# Parameter sistem
# ------------------------------

# Translasi
m = 1.0
c = 0.8
k = 2.0

# Rotasi
I = 0.5
c_theta = 0.15
k_theta = 2.0
b = 1.5

def elevator_input(t):
    return 0.3  # step elevator

def two_dof_dynamics(t, x):
    x_pos = x[0]
    x_vel = x[1]
    theta = x[2]
    q = x[3]
    
    delta_e = elevator_input(t)
    
    # Translasi
    dx1_dt = x_vel
    dx2_dt = (-c*x_vel - k*x_pos)/m
    
    # Rotasi
    dx3_dt = q
    dx4_dt = (-c_theta*q - k_theta*theta + b*delta_e)/I
    
    return [dx1_dt, dx2_dt, dx3_dt, dx4_dt]

# Kondisi awal
x0 = [0, 0, 0, 0]

t_span = (0, 10)
t_eval = np.linspace(0, 10, 1000)

sol = solve_ivp(two_dof_dynamics, t_span, x0, t_eval=t_eval)

x_pos = sol.y[0]
x_vel = sol.y[1]
theta = sol.y[2]
q = sol.y[3]

# ------------------------------
# Plot posisi translasi
# ------------------------------
plt.figure()
plt.plot(sol.t, x_pos)
plt.xlabel("Time (s)")
plt.ylabel("Position x (m)")
plt.title("Translational Position vs Time")
plt.grid()
plt.show()

# ------------------------------
# Plot sudut pitch
# ------------------------------
plt.figure()
plt.plot(sol.t, theta)
plt.xlabel("Time (s)")
plt.ylabel("Theta (rad)")
plt.title("Pitch Angle vs Time")
plt.grid()
plt.show()

# ------------------------------
# Phase plot pitch
# ------------------------------
plt.figure()
plt.plot(theta, q)
plt.xlabel("Theta (rad)")
plt.ylabel("Pitch Rate q (rad/s)")
plt.title("Phase Plot Pitch")
plt.grid()
plt.show()