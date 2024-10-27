from pydub import AudioSegment 
import simpleaudio as sa 
import numpy as np

# Load the MP3 file
audio = AudioSegment.from_mp3("test.mp3")

# Convert the audio to numpy array for processing
samples = np.array(audio.get_array_of_samples())

# Add white noise to create a rough effect
noise = np.random.normal(0, 250, samples.shape)  # Adjust the noise level
distorted_samples = samples + noise

# Clipping: limit the values to prevent overflow
distorted_samples = np.clip(distorted_samples, -32768, 32767)

# Convert back to raw audio data
distorted_audio = distorted_samples.astype(np.int16).tobytes()

# Play the distorted audio
play_obj = sa.play_buffer(distorted_audio, num_channels=audio.channels, bytes_per_sample=audio.sample_width, sample_rate=audio.frame_rate)

# Wait for the playback to finish
play_obj.wait_done()
