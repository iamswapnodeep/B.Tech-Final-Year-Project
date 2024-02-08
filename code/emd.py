from load_data import * #import all the data variables from load_data
import numpy as np
import matplotlib.pyplot as plt
from PyEMD import EMD

# Generate a sample signal
np.random.seed(42)
t = np.linspace(0, 1, 1000, endpoint=False)
signal = np.sin(2 * np.pi * 5 * t) + np.random.normal(scale=0.3, size=len(t))

# Create an EMD object
emd = EMD()
# Perform Empirical Mode Decomposition
imfs = emd(signal)
# Plot the original signal and its IMFs
plt.figure(figsize=(10, 8))

plt.subplot(len(imfs) + 1, 1, 1)
plt.plot(t, signal, 'r')
plt.title('Original Signal')

for i, imf in enumerate(imfs):
    plt.subplot(len(imfs) + 1, 1, i + 2)
    plt.plot(t, imf, 'g')
    plt.title(f'IMF {i + 1}')

plt.tight_layout()
plt.show()