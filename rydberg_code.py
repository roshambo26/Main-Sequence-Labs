
import numpy as np

# Rydberg lab — red light data analysis

red_m = np.array([0, 1, 2, 3, 4, 5])

red_A = np.array([
    0, 0.05468698, 0.10704686,
    0.1602794, 0.21758438, 0.27081692
])

red_dsinA = np.array([
    0, 0.00000068325, 0.0000013355,
    0.0000019949, 0.0000026984, 0.000003344
])

# Grating spacing (80 lines/mm)
d = 1 / 80000

# Angular uncertainty: convert arcminutes to radians
sigA = np.sqrt(2.5) * np.pi / (180 * 60)

# Propagate uncertainty into d*sin(A)
sig = d * np.abs(np.cos(red_A)) * sigA

# Weighted linear fit, excluding zero order
fit, cov = np.polyfit(
    red_m[1:],
    red_dsinA[1:],
    1,
    w=1/sig[1:],
    cov='unscaled'
)

# Wavelength = gradient
wavelength = fit[0]
wavelength_unc = np.sqrt(cov[0, 0])

print(f"Wavelength = {wavelength * 1e9:.2f} nm")
print(f"Uncertainty = {wavelength_unc * 1e9:.2f} nm")
print(f"Intercept = {fit[1]:.3e} m")
