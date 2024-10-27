import numpy as np
import sounddevice as sd

# Parameters
frequency = 880  # Frequency in Hz
duration = 5  # Duration in seconds
sample_rate = 44100  # Sample rate in Hz

# Generate the audio signal
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
audio_signal = 0.5 * np.sin(2 * np.pi * frequency * t)

# Play the audio signal
sd.play(audio_signal, sample_rate)
sd.wait()  # Wait until the audio is finished playing

# Distort the audio signal by adding noise
noise = np.random.normal(0, 0.1, audio_signal.shape)
distorted_signal = audio_signal + noise
audio_signal = distorted_signal

# Play the audio signal
sd.play(audio_signal, sample_rate)
sd.wait()  # Wait until the audio is finished playing
