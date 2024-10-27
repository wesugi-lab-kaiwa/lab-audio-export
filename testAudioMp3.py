
from pydub import AudioSegment
import simpleaudio as sa
import numpy as np

# Load the MP3 file
audio = AudioSegment.from_mp3("test.mp3")

# Convert the audio to a format that simpleaudio can play
audio = audio.set_channels(2).set_frame_rate(44100)
play_obj = sa.play_buffer(audio.raw_data, num_channels=2, bytes_per_sample=audio.sample_width, sample_rate=audio.frame_rate)

# Generate white noise
noise = np.random.normal(0, 1, len(audio.raw_data))

# Scale the noise to 5% of the original audio's volume
scaled_noise = (noise * 0.05 * np.iinfo(np.int16).max).astype(np.int16)

# Play noise
play_obj = sa.play_buffer(scaled_noise, num_channels=2, bytes_per_sample=2, sample_rate=audio.frame_rate)

# Wait for the playback to finish
play_obj.wait_done()
