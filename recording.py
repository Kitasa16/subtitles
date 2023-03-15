import pyaudio
import wave
import keyboard


    

# Set up the PyAudio input stream
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100





def record():
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    # Record audio while the user is holding down the "f" key
    print("Press 'f' to start recording...")
    keyboard.wait("f")
    frames = []
    while True:
        if keyboard.is_pressed('f'):
            data = stream.read(CHUNK)
            frames.append(data)
        else:
            break

    # Stop the stream and close the PyAudio instance
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save the recorded audio to a WAV file
    WAVE_OUTPUT_FILENAME = "audio.wav"
    with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
    print("Audio recording complete.")

while True:
    record()
    if keyboard.is_pressed('s'):
        print("recording session over")
        break


