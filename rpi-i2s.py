import os
import subprocess

def play_audio(file_path):
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return

    try:
        # Use omxplayer to play the audio file
        subprocess.run(['omxplayer', '-o', 'alsa', file_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while trying to play the file: {e}")

# https://deviceplus.jp/raspberrypi/replacing-the-analogue-audio-output-on-raspberry-pi/

if __name__ == "__main__":
    audio_file = "test.mp4"
    play_audio(audio_file)