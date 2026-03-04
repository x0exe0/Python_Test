import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

#parameter sinyal
fs = 100000
dt = 1/fs
t = np.linspace(0, 0.005, int(fs * 0.005), endpoint=False)
f_sinyal = 1000
amplitudo = 1

x_clean = amplitudo * signal.square(2 * np.pi * f_sinyal * t)

snr_db = -3
p_signal = np.mean(x_clean**2)
p_noise = p_signal / (10**(snr_db / 10))
noise = np.random.normal(0, np.sqrt(p_noise), len(x_clean))
x_noisy = x_clean + noise


#state space 2 dof

m = 1
c = 0.8
k = 2

I = 0.5
c_theta = 0.6
k_theta = 4
b = 1.5

Ac = np.array([
    [0, 1, 0, 0],
    [-k/m, -c/m, 0, 0],
    [0, 0, 0, 1],
    [0, 0, -k_theta/I, -c_theta/I]
])

Bc = np.array([
    [0],
    [0],
    [0],
    [b/I]
])

# Diskretisasi 
Ad = np.eye(4) + Ac * dt
Bd = Bc * dt

# Hanya ukur state pertama
C = np.array([[1, 0, 0, 0]])

Q = 1e-4 * np.eye(4)
R = np.array([[0.1]])

# algoritma kalman filter
def kalman_filter_4state(z):

    n = len(z)
    x_hat = np.zeros((4,1))      # initial state
    P = np.eye(4)                # initial covariance
    x_est_history = []

    for k in range(n):

        # INPUT (anggap elevator = 0)
        u = np.array([[0]])

        # PREDIKSI
        x_pred = Ad @ x_hat + Bd @ u
        P_pred = Ad @ P @ Ad.T + Q

        # UPDATE
        y = np.array([[z[k]]])

        S = C @ P_pred @ C.T + R
        K = P_pred @ C.T @ np.linalg.inv(S)

        x_hat = x_pred + K @ (y - C @ x_pred)
        P = (np.eye(4) - K @ C) @ P_pred

        x_est_history.append(x_hat.flatten())

    return np.array(x_est_history)


x_est = kalman_filter_4state(x_noisy)

# FFT analisis
n_fft = 1024
freq = np.fft.fftfreq(n_fft, 1/fs)[:n_fft//2]

mag_noisy = np.abs(np.fft.fft(x_noisy, n_fft)[:n_fft//2])
mag_kalman = np.abs(np.fft.fft(x_est[:,0], n_fft)[:n_fft//2])

# Plot
plt.subplot(2,1,1)
plt.plot(t, x_noisy, color='red', alpha=0.3, label='Noisy (-3dB)')
plt.plot(t, x_est[:,0], color='green', label='Kalman 4-State', linewidth=2)
plt.plot(t, x_clean, 'k--', alpha=0.7, label='Original')
plt.title("Kalman Filter 4 State - Time Domain")
plt.legend()
plt.grid(True)

plt.subplot(2,1,2)
plt.semilogy(freq, mag_noisy, color='red', alpha=0.3, label='FFT Noisy')
plt.semilogy(freq, mag_kalman, color='green', label='FFT Kalman 4-State')
plt.title("FFT 1024 Point")
plt.xlim(0, 5000)
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()