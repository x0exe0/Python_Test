import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# SETUP SINYAL
fs = 100000
dt = 1/fs
t = np.linspace(0, 0.005, int(fs * 0.005), endpoint=False)
f_sinyal = 1000
amplitudo = 1

# Sinyal bersih
x_clean = amplitudo * signal.square(2 * np.pi * f_sinyal * t)

# Tambah noise -3 dB
snr_db = -3
p_signal = np.mean(x_clean**2)
p_noise = p_signal / (10**(snr_db / 10))
noise = np.random.normal(0, np.sqrt(p_noise), len(x_clean))
x_noisy = x_clean + noise

# DEFINISI MODEL 4 STATE
# Model 2 sistem orde-2 paralel
A = np.array([
    [1, dt, 0,  0],
    [0, 1,  0,  0],
    [0, 0,  1, dt],
    [0, 0,  0,  1]
])

# Hanya ukur state pertama
C = np.array([[1, 0, 0, 0]])

Q = 1e-4 * np.eye(4)
R = np.array([[0.1]])

# KALMAN FILTER
def kalman_filter_4state(z):

    n = len(z)

    x_hat = np.zeros((4,1))      # Estimasi state
    P = np.eye(4)                # Covariance awal

    x_est_history = []

    for k in range(n):

        # === Prediction ===
        x_pred = A @ x_hat
        P_pred = A @ P @ A.T + Q

        # === Update ===
        y = np.array([[z[k]]])
        K = P_pred @ C.T @ np.linalg.inv(C @ P_pred @ C.T + R)

        x_hat = x_pred + K @ (y - C @ x_pred)
        P = (np.eye(4) - K @ C) @ P_pred

        x_est_history.append(x_hat.flatten())

    return np.array(x_est_history)

# Jalankan filter
x_est = kalman_filter_4state(x_noisy)

# ======================================
# 4. FFT ANALISIS
# ======================================

n_fft = 1024
freq = np.fft.fftfreq(n_fft, 1/fs)[:n_fft//2]

mag_noisy = np.abs(np.fft.fft(x_noisy, n_fft)[:n_fft//2])
mag_kalman = np.abs(np.fft.fft(x_est[:,0], n_fft)[:n_fft//2])

# ======================================
# 5. PLOT
# ======================================

plt.figure(figsize=(12,10))

# Time domain
plt.subplot(2,1,1)
plt.plot(t, x_noisy, color='red', alpha=0.3, label='Noisy (-3dB)')
plt.plot(t, x_est[:,0], color='green', label='Kalman', linewidth=2)
plt.plot(t, x_clean, 'k--', alpha=0.7, label='Original')
plt.title("Kalman Filter - Time Domain")
plt.legend()
plt.grid(True)

# Frequency domain
plt.subplot(2,1,2)
plt.semilogy(freq, mag_noisy, color='red', alpha=0.3, label='FFT Noisy')
plt.semilogy(freq, mag_kalman, color='green', label='FFT Kalman')
plt.title("FFT 1024 Point")
plt.xlim(0, 5000)
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show() 