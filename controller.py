from WakeWord.wake_word import listen_for_wake_word
from Speech2Text.speech2text import transcribe_speech


# * Listen to for the wake-word
if listen_for_wake_word():

    # * Transcribe the audio in real-time
    text = transcribe_speech();
    print(text);