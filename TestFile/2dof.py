import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parameter
g = 9.81      
L = 1.0       
c = 0.5       

def system(t, x):
    theta = x[0]
    omega = x[1]
    
    dtheta_dt = omega
    domega_dt = -(g/L)*theta - c*omega
    
    return [dtheta_dt, domega_dt]

t_span = (0, 10)
t_eval = np.linspace(0, 10, 1000)

# Kondisi awal
x0 = [0.5, 0]   # theta awal 0.5 rad, omega awal 0

# Solve
sol = solve_ivp(system, t_span, x0, t_eval=t_eval)

# Plot 1: Sudut terhadap waktu
plt.figure()
plt.plot(sol.t, sol.y[0])
plt.xlabel("Time (s)")
plt.ylabel("Theta (rad)")
plt.title("Sudut θ terhadap Waktu")
plt.show()

# Plot 2: Kecepatan sudut terhadap waktu
plt.figure()
plt.plot(sol.t, sol.y[1])
plt.xlabel("Time (s)")
plt.ylabel("Omega (rad/s)")
plt.title("Kecepatan Sudut ω terhadap Waktu")
plt.show()