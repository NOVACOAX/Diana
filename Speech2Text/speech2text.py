import speech_recognition as sr
from playsound import playsound
import threading

# * Check the microphone index
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name));

def play_sound_async(file_path):
    threading.Thread(target=playsound, args=(file_path,), daemon=True).start()

def transcribe_speech():
  # * obtain audio from the microphone
  r = sr.Recognizer()
  with sr.Microphone() as source:
      r.adjust_for_ambient_noise(source);
      r.dynamic_energy_threshold = True;
      r.pause_threshold = 1.5;
      # * Play the first sound
      play_sound_async('assets/sounds/ding.mp3');
      print("Say something!");
      audio = r.listen(source)

  # * Play the second sound
  play_sound_async('assets/sounds/hotel-bell-ding.mp3');

  # * recognize speech using whisper
  try:
      text = r.recognize_whisper(audio, language="english");
      print("Whisper thinks you said: " + text);
  except sr.UnknownValueError:
      print("Whisper could not understand audio");
  except sr.RequestError as e:
      print("Could not request results from Whisper");

  return text;