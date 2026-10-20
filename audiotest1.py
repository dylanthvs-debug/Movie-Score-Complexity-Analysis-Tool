# Python 3 Audio Sample Testing
# This program makes use of the librosa and music21 Libraries to 
# taken in a wav file input and do simple analysis and processing waveform

#import the librosa library for the program to use:
import librosa

# Assign the variables y and sr to data loaded from the audio file:
# y loads the audio file itself
# sr extracts the sampling rate for the audio file
y, sr = librosa.load("single-piano-note-a4_100bpm_C_major.wav", sr=None)

# Print the sampling rate that was extracted using the librosa load function:
print("Sample rate:", sr)

# Calculate the duration of the audio file:
# Formula: Duration (seconds) = (Total samples)/(Sample Rate)
# Use the len() functio to return the amount of samples taken from y

# Duration variable and formula applied:
duration = (len(y))/(sr)

# Print duration in seconds:
print("Duration:", duration, "seconds")

# Make use of built-in librosa duration function:
duration_librosa = librosa.get_duration(y=y, sr=sr)

# Print librosa duration function output:
print("librosa duration: ", duration_librosa, "seconds")

# Deterimining the frequency of the note:
# Create a variable named "frequencies" that creates an array of
# the detected frequencies and harmonics of the piano note "A4".
frequencies = librosa.yin(y=y, fmin=200, fmax=1000, sr=sr)

# Output the array of frequencies detected by the librosa.yin() function
print(frequencies)

# The following output was given by the program:
# [ 888.99762902  893.4602208   895.10822404 ... 1002.27272727 1002.27272727
# 1002.27272727]
# The fundamental freqeuncy of A4 is 440 Hz
# The first harmonic was given as 889 Hz, which is close to A5, an octave higher than A4

# Frequency Analysis:
# Experiment to Plot the Waveform:
# Import the matplot library and call it plt (for easier function calls)
import matplotlib.pyplot as plt

# Create figure 1:
plt.figure(1)

# Use librosa's visualisation module to plot the waveform against time:
librosa.display.waveshow(y, sr=sr)

# Give the plot a title:
plt.title("Complete Audio Waveform - Piano A4")

# Labelling both axes:
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")

# The function was shown to have an instant inital attack, followed by a rapid decay,
# then the note was sustained for the majority of the audio duration, and then it decayed
# once more and eventually approached zero (silence).

# Audio Slicing - attempt to produce a portion of the time domain plot of the waveform
# to conduct analysis and visualise the harmonics.
# xlim limits the plot between two selected x-variables:
plt.figure(2)
librosa.display.waveshow(y, sr=sr)
plt.xlim(0, 1)
plt.title("First Second of Audio - Piano A4")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.show()

# Analysing the frequency spectrum:
# Creating an audio slice:
# Analyse audio slice between 0.1 and 0.4 seconds:

# Using Index = Sampling Rate x Time 
# we can determine the samples for a given time range

# Indexing the start and end of the audio sample using an integer array:

# Starting index as an integer:
start = int(0.1*sr)
# End index as an integer:
end = int(0.4*sr)

# Slicing audio file using start and ending indexes:
y_segment = y[start:end]

# Audio slice information:
# Number of samples in y_segment:
y_seg_num = len(y_segment)
print("Number of Samples in audio slice:", y_seg_num)

# Duration of y_segment:
y_seg_dur = librosa.get_duration(y=y_segment, sr=sr)
print("Duration of audio slice:", y_seg_dur)

# Analysis of Waveform with fast fourier transform:
# Using NumPy library:
import numpy as np

# Fast Fourier Transform function:
# np calls the library
# fft is for fast fourier transforms
# rfft is designed for real-valued input signals (non-negative frequency components)
fft_result = np.fft.rfft(y_segment)

# Calculating magnitudes of the FFT Harmonics:
# np.abs() calculates absolute value of each element.
seg_mag = np.abs(fft_result)

print("FFT output:", fft_result)
print("Magnitudes:", seg_mag)
print("Number of FFT bins:", len(seg_mag))

# Converting FFT bins into frequencies:
# represented using deltaf = sr/N
# where N is the number of samples, and deltaf is separation frequency between FFT bins
# Calculate the frequency associate with each bin:
# d = 1/sr is the period between samples, derived from T = 1/f
# rfftfreq arguments are number of samples in segment, and time (s) between samples
seg_freqs = np.fft.rfftfreq(len(y_segment), d=1/sr)

# Printing Harmonic frequencies for the note A4:
print("Frequency at bin 132:", seg_freqs[132], "Hz")
print("Frequency at bin 132:", seg_freqs[264], "Hz")
print("Frequency at bin 132:", seg_freqs[396], "Hz")

# Plotting the frequency spectrum:
# Plot spectrum using magnitude as y-axis and frequency as x-axis:
plt.figure(3)
plt.plot(seg_freqs, seg_mag)
plt.title("Frequency Spectrum between 0.1 and 0,4 seconds")
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.xlim(0,2000)
plt.show()

# Analysis using Spectrogram:
# Using the Short Time Fourier Transform to analyse overlapping windows without loss
stft_result = librosa.stft(y)

# Spectrogram requires results in decibels (dB)
# Obtaining absolute values of results:
stft_mag = np.abs(stft_result)
# Using librosa amp to dB function:
stft_db = librosa.amplitude_to_db(stft_mag, ref=np.max)

# Plotting spectrogram:
plt.figure(4)

# Formatting data required by spectrogram for plot:
librosa.display.specshow(stft_db, sr=sr, x_axis="time", y_axis="linear")

plt.title("Spectrogram of A4")
plt.xlabel("Time (s)")
plt.ylabel("Frequency (Hz)")
plt.ylim(0, 2000)

# Colour bar configuration:
plt.colorbar(format="%+2.0f dB")

plt.show()