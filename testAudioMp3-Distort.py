from pydub import AudioSegment
import simpleaudio as sa
import numpy as np

# Load the MP3 file
audio = AudioSegment.from_mp3("test.mp3")

# Convert the audio to numpy array for processing
samples = np.array(audio.get_array_of_samples())

# Normalize the audio samples to the range -1 to 1
max_val = np.max(np.abs(samples))
normalized_samples = samples / max_val

# Apply hard clipping to create a distortion effect
threshold = 0.1  # Adjust this value to control the distortion level これが小さいほど音割れが大きくなる
clipped_samples = np.clip(normalized_samples, -threshold, threshold)

# Re-normalize the clipped samples back to the 16-bit range
distorted_samples = (clipped_samples * max_val).astype(np.int16)

# Convert back to raw audio data
distorted_audio = distorted_samples.tobytes()

# Play the distorted audio
play_obj = sa.play_buffer(distorted_audio, num_channels=audio.channels, bytes_per_sample=audio.sample_width, sample_rate=audio.frame_rate)

# Wait for the playback to finish
play_obj.wait_done()
