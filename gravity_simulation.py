import numpy as np
import matplotlib.pyplot as plt

# Two-body gravitational simulation
# Starting point — June 2026 build

G = 6.674e-11  # gravitational constant

# masses in kg
m1 = 1.989e30  # star (solar mass)
m2 = 5.972e24  # planet (earth mass)

# initial positions in metres
r1 = np.array([0.0, 0.0])
r2 = np.array([1.496e11, 0.0])  # 1 AU

# initial velocities in m/s
v1 = np.array([0.0, 0.0])
v2 = np.array([0.0, 29780.0])  # earth orbital velocity

# to be built: euler integration, then Runge-Kutta
# goal: simulate stable orbit and visualise
