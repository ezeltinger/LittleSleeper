import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import time


print("Imported Libraries")
freq = 32000
duration = 5
sd.default.samplerate = freq
sd.default.device = 'HD Pro Webcam C920: USB Audio (hw:1,0)'
recording = np.array([[], []], dtype='int32')
def callback(indata, frames, time, status):
    if status:
        print(status)
    np.append(recording, indata)
    # write("recording0.wav", freq, indata)
    # print(indata)
    # max_audio = np.abs(indata).max()
    # print(f"Max audio in is {max_audio}")

# print(sd.query_devices())

# with sd.InputStream(channels=2, dtype='int32', callback=callback):
#     sd.sleep(int(duration * 1000))

recording = sd.rec(int(duration * freq), channels=2)
sd.wait()

write("recording0.wav", freq, recording)

