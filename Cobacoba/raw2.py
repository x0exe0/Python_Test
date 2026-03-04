import numpy as np
import matplotlib.pyplot as plt

# ===============================
# 1. PARAMETER SISTEM
# ===============================

dt = 0.1

A = np.array([[1, dt],
              [0, 1]])

B = np.array([[0],
              [dt]])

C = np.array([[1, 0]])  # hanya ukur posisi

# ===============================
# 2. NOISE COVARIANCE
# ===============================

Q = np.array([[0.01, 0],
              [0, 0.01]])

R = np.array([[0.1]])

# ===============================
# 3. LQR CONTROLLER
# ===============================

Q_lqr = np.array([[10, 0],
                  [0, 1]])

R_lqr = np.array([[1]])

# Solve Riccati equation manually (iteratif sederhana)
P = Q_lqr
for _ in range(100):
    P = A.T @ P @ A - A.T @ P @ B @ \
        np.linalg.inv(R_lqr + B.T @ P @ B) @ \
        B.T @ P @ A + Q_lqr

K_lqr = np.linalg.inv(R_lqr + B.T @ P @ B) @ B.T @ P @ A

# ===============================
# 4. INISIALISASI
# ===============================

x_true = np.array([[5],
                   [0]])

x_hat = np.array([[0],
                  [0]])

P_k = np.eye(2)

N = 100

x_history = []
xhat_history = []

# ===============================
# 5. SIMULASI LOOP
# ===============================

for k in range(N):

    # ---- CONTROLLER ----
    u = -K_lqr @ x_hat

    # ---- SISTEM SEBENARNYA ----
    w = np.random.multivariate_normal([0,0], Q).reshape(2,1)
    v = np.random.normal(0, np.sqrt(R)).reshape(1,1)

    x_true = A @ x_true + B @ u + w
    y = C @ x_true + v

    # ---- KALMAN FILTER ----
    # Prediction
    x_pred = A @ x_hat + B @ u
    P_pred = A @ P_k @ A.T + Q

    # Kalman Gain
    K_k = P_pred @ C.T @ np.linalg.inv(C @ P_pred @ C.T + R)

    # Update
    x_hat = x_pred + K_k @ (y - C @ x_pred)
    P_k = (np.eye(2) - K_k @ C) @ P_pred

    x_history.append(x_true.flatten())
    xhat_history.append(x_hat.flatten())

# ===============================
# 6. PLOT
# ===============================

x_history = np.array(x_history)
xhat_history = np.array(xhat_history)

plt.plot(x_history[:,0], label="True Position")
plt.plot(xhat_history[:,0], '--', label="Estimated Position")
plt.legend()
plt.show()