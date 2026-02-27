import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# ------------------------------
# Parameter sistem
# ωn = 5 rad/s
# ζ = 0.7
# ------------------------------
a1 = -9       # = -ωn^2
a2 = -3       # = -2ζωn
b1 = 2        # gain elevator

def elevator_input(t):
    return 0.1   

def pitch_dynamics(t, x):
    theta = x[0]
    q = x[1]
    delta_e = elevator_input(t)
    
    dtheta_dt = q
    dq_dt = a1*theta + a2*q + b1*delta_e
    
    return [dtheta_dt, dq_dt]

x0 = [0, 0] #kondisi awal
t_span = (0, 10) #simulasinya berapa detik
t_eval = np.linspace(0, 10, 1000) 


sol = solve_ivp(pitch_dynamics, t_span, x0, t_eval=t_eval)
theta = sol.y[0]
q = sol.y[1]

# Plot 1: Theta vs Time
plt.figure()
plt.plot(sol.t, theta)
plt.xlabel("Time (s)")
plt.ylabel("Pitch Angle θ (rad)")
plt.title("Theta vs Time")
plt.savefig("1.png")
plt.grid()
plt.show()

# ------------------------------
# Plot 2: dTheta/dt vs Time (q)
# ------------------------------
plt.figure()
plt.plot(sol.t, q)
plt.xlabel("Time (s)")
plt.ylabel("dθ/dt = q (rad/s)")
plt.title("Pitch Rate vs Time")
plt.savefig("2.png")
plt.grid()
plt.show()

# ------------------------------
# Plot 3: Phase Plot (q vs θ)
# ------------------------------
plt.figure()
plt.plot(theta, q)
plt.xlabel("Theta (rad)")
plt.ylabel("Pitch Rate q (rad/s)")
plt.title("Phase Plot (q vs Theta)")
plt.savefig("3.png")
plt.grid()
plt.show()