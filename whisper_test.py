
import whisper

import wave
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# Open the wave file for reading
audio_file = 'audio.wav'
with wave.open(audio_file, 'rb') as wave_file:
    # Print some information about the wave file
    print(f"Number of channels: {wave_file.getnchannels()}")
    print(f"Sample width: {wave_file.getsampwidth()}")
    print(f"Frame rate: {wave_file.getframerate()}")
    print(f"Number of frames: {wave_file.getnframes()}")

    # Read all the audio data from the wave file
    audio_data = wave_file.readframes(wave_file.getnframes())

    # Print the audio data as text
    # print(audio_data.decode('utf-8'))
    
model = whisper.load_model("base")
result = model.transcribe(audio_file)
print(result["text"])