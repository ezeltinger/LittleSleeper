import sounddevice as sd
import numpy as np
import time

duration = 5
sd.default.samplerate = 44100
def callback(indata, frames, time, status):
    if status:
        print(status)
    # print(indata)
    max_audio = np.abs(indata).max()
    # print(f"Max audio in is {max_audio}")

print(sd.query_devices())

with sd.InputStream(dtype='int32', callback=callback):
    sd.sleep(int(duration * 1000))