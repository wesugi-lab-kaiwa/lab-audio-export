import numpy as np
import sounddevice as sd

# Parameters
duration = 20  # seconds
sample_rate = 44100  # Hz
carrier_freq = 40000  # Hz
modulator_freq = 880  # Hz

# Time array
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Generate carrier and modulator signals
carrier = np.sin(2 * np.pi * carrier_freq * t)
modulator = np.sin(2 * np.pi * modulator_freq * t)

# Modulated signal
modulated_signal = carrier * modulator

# Output the signal
sd.play(modulated_signal, sample_rate)
sd.wait()