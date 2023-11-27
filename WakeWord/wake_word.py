import os
import pvporcupine
import struct
import pyaudio
from dotenv import dotenv_values

config = {**dotenv_values(".env.secret")}

def listen_for_wake_word():
    # initialize Porcupine with your custom wake word
    handle = pvporcupine.create(
        access_key=config['PICOVOICE_ACCESS_KEY'],
        keywords=['Diana'],
        keyword_paths=['WakeWord/Diana_en_mac_v2_2_0.ppn'])

    # initialize PyAudio and open an input stream
    pa = pyaudio.PyAudio()
    audio_stream = pa.open(
        rate=handle.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=handle.frame_length)

    print("Listening for wake word...")

    while True:
        # read audio data from stream
        pcm = audio_stream.read(handle.frame_length, exception_on_overflow=False)
        pcm = struct.unpack_from("h" * handle.frame_length, pcm)

        # check for wake word
        keyword_index = handle.process(pcm)
        if keyword_index >= 0:
            print("Wake word detected!")
            break

    # cleanup
    audio_stream.close()
    pa.terminate()
    handle.delete()

    return True
