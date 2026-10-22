# Music Note Generator
# Program that generates a selected musical note from one of the 12 main musical notes

# Pure musical note is represented by:
# Asin(2*pi*f*t)
# Where a = amplitude, f = frequency, and t = time

# For the note A4, the fundamental frequency is 440 Hz

# Import NumPy
import numpy as np

# Signal Parameters:
amplitude = 1
frequency = 440
duration = 1
sr = 44100

# Time array:
# Index of the amount of samples for signal generation
t = np.arange(int(sr*duration))/sr

# Generate the sine wave:
signal = amplitude * np.sin(2 * np.pi * frequency * t)

# Printintg values for testing:
print("Number of samples: ", len(signal))
print("First 10 time values: ", t[:10])
print("First 10 amplitude values: ", signal[:10])

# Graphical representation of Generated Audio Sample:
import matplotlib.pyplot as plt

plt.figure(figsize=(10,4))
plt.plot(t, signal)

# Plot labels:
plt.title("Generated Waveform of A4")
plt.xlabel("Time, t")
plt.ylabel("Amplitude, A")
plt.grid(True)

# Zoomed in plot of the Graph to show the waveform:
plt.figure(2)
plt.plot(t, signal)
plt.title("Waveform of A4 between 0-0.01 seconds")
plt.xlim(0, 0.01)
plt.xlabel("Time, t")
plt.ylabel("Amplitude, A")
plt.grid(True)

plt.show()