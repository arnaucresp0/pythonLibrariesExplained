import numpy as np
import matplotlib.pyplot as plt

# Signal parameters
fs = 1000              # Frequency(Hz)
t = np.linspace(0, 1, fs)

print(t)

# Orignal signal based on a sinusoidal signal with the values generated
signal = np.sin(2 * np.pi * 5 * t)

# Add some noise to the signal
noise = 0.4 * np.random.randn(len(t))
noisy_signal = signal + noise

# Filtre de noisy signal
window_size = 20
kernel = np.ones(window_size) / window_size
filtered_signal = np.convolve(noisy_signal, kernel, mode="same")

# Visualització
plt.figure(figsize=(10, 5))
plt.plot(t, noisy_signal, label="Noisy signal", alpha=0.6)
plt.plot(t, filtered_signal, label="Filtered signal", linewidth=2)
plt.plot(t, signal, label="Original signal", linestyle="--", alpha=0.8)

plt.xlabel("Time (s)")
plt.ylabel("Magnitude")
plt.title("Signal processing with NumPy")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()