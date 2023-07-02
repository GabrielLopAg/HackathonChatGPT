# !pip install SpeechRecognition
# !pip install pipwin
# !pipwin install PyAudio

import speech_recognition as sr


def extract_text_from_voice():
  speech_recognition = sr.Recognizer()
  with sr.Microphone() as source:
    audio = speech_recognition.listen(source, phrase_time_limit=2)
    audio_text = ""

    try:
      audio_text = speech_recognition.recognize_google(audio)
      print(audio_text)
    except Exception as e:
      print(f"Exception: {str(e)}")

    return audio_text