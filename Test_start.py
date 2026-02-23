database_motor = {
            # Motor Tipe 1
            "T6PLUS": {
                "specs": {
                    "total_weight_g": 620,
                    "propeller_weight_g": 108,
                    "max_thrust_N": 11.5,
                    "max_voltage_V": 60.9,
                    "battery_cells": 14,
                    "current_cont_A": 30,
                    "current_max_A": 90,
                    "max_takeoff_weight_kg": 5.5,
                    "Weight_drone_g": 35128,

                },
                "regressions": {
                    "throttle_vs_power": [2767.107, 394.588, -417.513],    
                    "throttle_vs_ampere": [61.211, 7.454, -8.828],  
                    "throttle_vs_thrust": [-2125.045, 20766.587, -5761.246],     
                    "throttle_vs_efficiency": [-59.623, 74.107, 60.900],
                }
            },

            # Motor Tipe 2
            "T8": {
                "specs": {
                    "total_weight_g": 1140,
                    "propeller_weight_g": 220,
                    "max_thrust_N": 15.9,
                    "max_voltage_V": 60.9,
                    "battery_cells": 14,
                    "current_cont_A": 30,
                    "current_max_A": 120,
                    "max_takeoff_weight_kg": 6,
                    "Weight_drone_g": 37000,
                },
                "regressions": {
                    "throttle_vs_power": [4965.821, -2452.62, 424.660], 
                    "throttle_vs_ampere": [111.988, -57.644, 10.303],  
                    "throttle_vs_thrust": [4976.123, 13804.569, -3758.644],     
                    "throttle_vs_efficiency": [-66.727, 90.085, 51.130],
                    "rpm_vs_force": [4.816e-07, -5.700e-03, 20.771] 
                }
            },

            # Motor Tipe 3
            "T10": {
                "specs": {
                     "total_weight_g": 1429,
                    "propeller_weight_g": 267.3,
                    "max_thrust_N": 17.4,
                    "max_voltage_V": 60.9,
                    "battery_cells": 14,
                    "current_cont_A": 80,
                    "current_max_A": 150,
                    "max_takeoff_weight_kg": 6,
                    "Weight_drone_g": 40938,
                },
                "regressions": {
                    "throttle_vs_power": [4185.561, 1015.866, -989.4], 
                    "throttle_vs_ampere": [80.939, 15.880, -17.716],  
                    "throttle_vs_thrust": [-11334.464, 42684.595, -12976.96205],     
                    "throttle_vs_efficiency": [-96.857, 109.603, 48.284],

                }
            },

            # Motor Tipe 4
            "T15": {
                "specs": {
                    "total_weight_g": 1568,
                    "propeller_weight_g": 308,
                    "max_thrust_N": 22.3,
                    "max_voltage_V": 60.9,
                    "battery_cells": 14,
                    "current_cont_A": 80,
                    "current_max_A": 150,
                    "max_takeoff_weight_kg": 9,
                    "Weight_drone_g": 37005
                },
                "regressions": {
                    "throttle_vs_power": [14907.132, -11524.349, 2557.599], 
                    "throttle_vs_ampere": [286.637, -224.776, 60.337],  
                    "throttle_vs_thrust": [21537.850, 7782.832, -3561.223],     
                    "throttle_vs_efficiency": [-112.569, 155.252, 28.367],
                }
            },

            # Motor Tipe 5
            "T20": {
                "specs": {
                     "total_weight_g": 1890,
                    "propeller_weight_g": 442.5,
                    "max_thrust_N": 32.5,
                    "max_voltage_V": 80.1,
                    "battery_cells": 14,
                    "current_cont_A": 70,
                    "current_max_A": 150,
                    "prop_diameter_in*prop_pitch_in":134112,
                    "max_takeoff_weight_KG": 15,
                    "Weight_drone_g": 37008,
                },
                "regressions": {
                    "throttle_vs_power": [9307.082, -2708.706, 144.442], 
                    "throttle_vs_ampere": [183.454, -60.442, 5.130],  
                    "throttle_vs_thrust": [2118.956, 42513.175, -11000],     
                    "throttle_vs_efficiency": [-36.250, 40.675, 73.793],   
                }
            },

            "T20_18S": {
                "specs": {
                     "total_weight_g": 1943,
                    "propeller_weight_g": 442.5,
                    "max_thrust_N": 32.5,
                    "max_voltage_V": 80.1,
                    "battery_cells": 14,
                    "current_cont_A": 70,
                    "current_max_A": 150,
                    "prop_diameter_in*prop_pitch_in":134112,
                    "max_takeoff_weight_KG": 15,
                    "Weight_drone_g": 37008,
                },
                "regressions": {
                    "throttle_vs_power": [8534.338885, 527.4294159, -1226.239715], 
                    "throttle_vs_ampere": [127.7697285, 2.745209989, -16.53645492],  
                    "throttle_vs_thrust": [-6143.93047, 60242.65035, -17422.67845],     
                    "throttle_vs_efficiency": [-61.45707895, 65.46045448, 69.16932337],
                }
            },

            #Tipe Motor 6
            "T30": {
                "specs": {
                    "total_weight_g": 2370,
                    "propeller_weight_g": 418.3,
                    "max_thrust_N": 36.6,
                    "max_voltage_V": 80.1,
                    "battery_cells": 14,
                    "current_cont_A": 100,
                    "current_max_A": 230,
                    "prop_diameter_in*prop_pitch_in":152908.2,
                    "max_takeoff_weight_KG": 15,
                    "Weight_drone_g": 37010,
                },
                "regressions": {
                    "throttle_vs_power": [-1068.501, 10757.986, -3764.740], 
                    "throttle_vs_ampere": [105.467, 108.217, -51.657],  
                    "throttle_vs_thrust": [-47118.532, 97974.080, -25210.207],     
                    "throttle_vs_efficiency": [-60210, 54.997, 72.873],    
                }
            },

            "T30_18S": {
                "specs": {
                    "total_weight_g": 2400,
                    "propeller_weight_g": 418.3,
                    "max_thrust_N": 36.6,
                    "max_voltage_V": 80.1,
                    "battery_cells": 14,
                    "current_cont_A": 100,
                    "current_max_A": 230,
                    "prop_diameter_in*prop_pitch_in":152908.2,
                    "max_takeoff_weight_KG": 15,
                    "Weight_drone_g" : 37011,
                },
                "regressions": {
                    "throttle_vs_power": [4110.045249, 5061.969748, -1776.183232], 
                    "throttle_vs_ampere": [62.18164189, 70.4710084, -25.13970911],  
                    "throttle_vs_thrust": [-12821.47253, 64769.22571, -14154.21119],     
                    "throttle_vs_efficiency": [-41.37685844, 42.53277311, 77.49967356],     
                }
            },

            #Tipe Motor 7
            "T40": {
                "specs": {
                    "total_weight_g": 3700,
                    "propeller_weight_g": 603.4,
                    "max_thrust_N": 42.8,
                    "max_voltage_V": 80.1,
                    "battery_cells": 14,
                    "current_cont_A": 100,
                    "current_max_A": 230,
                    "prop_diameter_in*prop_pitch_in":231610,
                    "max_takeoff_weight_KG": 22,
                    "Weight_drone_g": 37020,
                },
                "regressions": {
                    "throttle_vs_power": [3413.436, 10068.977, -4081.265], 
                    "throttle_vs_ampere": [76.686, 177.883, -74.424],  
                    "throttle_vs_thrust": [-32576.808, 103505.685, -27612.365],     
                    "throttle_vs_efficiency": [-20.761, 4.440, 86.830],   
                }
            },

            "T40_18S": {
                "specs": {
                    "total_weight_g": 2700,
                    "propeller_weight_g": 603.4,
                    "max_thrust_N": 42.8,
                    "max_voltage_V": 80.1,
                    "battery_cells": 14,
                    "current_cont_A": 100,
                    "current_max_A": 230,
                    "prop_diameter_in*prop_pitch_in":231610,
                    "max_takeoff_weight_KG": 22,
                    "Weight_drone_g": 37014,
                },
                "regressions": {
                    "throttle_vs_power": [2493.249674, 8840.522439, -3300.173172], 
                    "throttle_vs_ampere": [40.09324098, 124.1174338, -47.0354986],  
                    "throttle_vs_thrust": [-32120.20962, 99453.1299, -25625.81128],     
                    "throttle_vs_efficiency": [-33.18130578, 28.99287117, 81.91764931],    
                }
            },


            #Tipe Motor 8
            "T50": {
                "specs": {
                    "total_weight_g": 3700,
                    "propeller_weight_g": 763.4,
                    "max_thrust_N": 50.8,
                    "max_voltage_V": 80.1,
                    "battery_cells": 14,
                    "current_cont_A": 100,
                    "current_max_A": 230,
                    "prop_diameter_in*prop_pitch_in":279400,
                    "max_takeoff_weight_KG": 22,
                    "Weight_drone_g": 37020,
                },
                "regressions": {
                    "throttle_vs_power": [12211.820, 261.776, -1101.574], 
                    "throttle_vs_ampere": [255.339, -21.600, -14.205],  
                    "throttle_vs_thrust": [-10388.407, 88121.812, -21226.953],     
                    "throttle_vs_efficiency": [-50.627, 50.259, 76.353],    
                }
            },

        "T50_18S": {
                "specs": {
                    "total_weight_g": 3850,
                    "propeller_weight_g": 763.4,
                    "max_thrust_N": 50.8,
                    "max_voltage_V": 80.1,
                    "battery_cells": 14,
                    "current_cont_A": 100,
                    "current_max_A": 230,
                "prop_diameter_in*prop_pitch_in":279400,
                    "max_takeoff_weight_KG": 22,
                    "Weight_drone_g": 37020,
                },
                "regressions": {
                    "throttle_vs_power": [2725.431257, 13921.16749, -5285.733838], 
                    "throttle_vs_ampere": [47.99382476, 193.6635879, -74.92745834],  
                    "throttle_vs_thrust": [-48833.75538, 144130.0906, -38448.93119],     
                    "throttle_vs_efficiency": [-28.60237618, 16.4844024, 88.16320893],    
                }
            },
            #Tipe Motor 9
            "T50P_18S": {
                "specs": {
                    "total_weight_g": 4200,
                    "propeller_weight_g": 558,
                    "max_thrust_N": 50.8,
                    "max_voltage_V": 80.1,
                    "battery_cells": 14,
                    "current_cont_A": 100,
                    "current_max_A": 230,
                    "prop_diameter_in*prop_pitch_in":279400,
                    "max_takeoff_weight_KG": 22,
                    "Weight_drone_g": 37022,
                },
                "regressions": {
                    "throttle_vs_power": [13618.0668, -2243.028836, 271.2091273], 
                    "throttle_vs_ampere": [205.77754, -43.45051266, 6.697010076],  
                    "throttle_vs_thrust": [-19275.0366, 90488.75615, -17410.07992],     
                    "throttle_vs_efficiency": [-80.51244743, 82.7174232, 65.31542362],  
                }
            },

            #Tipe Motor 10
            "T60_18S": {
                "specs": {
                    "total_weight_g": 5050,
                    "propeller_weight_g": 567.5,
                    "max_thrust_N": 50.8,
                    "max_voltage_V": 80.1,
                    "battery_cells": 14,
                    "current_cont_A": 100,
                    "current_max_A": 230,
                    "prop_diameter_in*prop_pitch_in":279400,
                    "max_takeoff_weight_KG": 22,
                    "Weight_drone_g": 37027,
                },
                "regressions": {
                    "throttle_vs_power": [22791.76318, -5424.077605, -24.86479554], 
                    "throttle_vs_ampere": [352.8105765, -103.7395359, 5.939628191],  
                    "throttle_vs_thrust": [-12093.05861, 123534.4972, -31465.23446],     
                    "throttle_vs_efficiency": [-67.99260041, 80.18484876, 64.20546621],   
                }
            }
        }


import numpy as np
import matplotlib.pyplot as plt

n_motor = 6
u = np.linspace(0.05, 1, 1500)
g = 9.81

def poly(coef, u):
    a, b, c = coef
    return a*u**2 + b*u + c

def find_hover_throttle(coef_T, coef_P, T_hover):
    aT, bT, cT = coef_T
    aP, bP, cP = coef_P

    roots = np.roots([aT, bT, cT - T_hover])
    roots = roots[np.isreal(roots)].real
    roots = roots[(roots > 0) & (roots < 1)]

    valid = []
    for u in roots:
        T_u = aT*u**2 + bT*u + cT
        P_u = aP*u**2 + bP*u + cP

        if (T_u > 0) and (P_u > 0):
            valid.append(u)

    if len(valid) == 0:
        return None

    return min(valid)

for motor, data in database_motor.items():

    W_total_g = data["specs"]["Weight_drone_g"]  
    T_hover = W_total_g / n_motor                 

    coef_T = data["regressions"]["throttle_vs_thrust"]
    coef_P = data["regressions"]["throttle_vs_power"]

    T = poly(coef_T, u)        
    P = poly(coef_P, u)        

    T[T <= 0] = np.nan
    P[P <= 0] = np.nan


    mask = (~np.isnan(T)) & (~np.isnan(P)) & (T >= T_hover)
    if not mask.any():
        print(f"{motor} tidak feasible")
        continue

    u_f = u[mask]
    T_f = T[mask]
    P_f = P[mask]
    eta = T_f / P_f

    idx = np.argmax(eta) 
    u_opt = u_f[idx] 
    eta_max = eta[idx] 
    u_hover = find_hover_throttle(coef_T, coef_P, T_hover)

    if u_hover is None:
        print(f"{motor} hover thrust tidak tercapai")
        continue

    # ========================
    # PLOT (DUAL AXIS)
    # ========================
    fig, ax1 = plt.subplots(figsize=(9,5))
    ax2 = ax1.twinx()

    ax1.plot(u, T, label="Thrust [g]")
    ax1.plot(u, P, label="Power [W]")
    ax1.fill_between(
        u,
        0,
        T,
        where=mask,
        alpha=0.2,
        label="Feasible Region"
    )
    ax1.axvline(u_hover, linestyle="--", label="u_hover")
    ax1.axvline(u_opt, linestyle=":", label="u_opt")

    ax2.plot(u_f, eta, linestyle="-.", label="Efficiency [gf/W]")

    ax1.set_xlabel("Throttle")
    ax1.set_ylabel("Thrust / Power")
    ax2.set_ylabel("Efficiency")

    ax1.grid(True)
    fig.legend(loc="upper right")
    plt.title(f"{motor} – Optimal Operating Region")
    plt.show()

    print(f"{motor}")
    print(f"T_hover/motor = {T_hover:.2f} gf")
    print(f"u_hover       = {u_hover:.3f}")
    print(f"u_opt         = {u_opt:.3f}")
    print(f"η_max         = {eta_max:.5f} gf/W")
    print("-"*40)