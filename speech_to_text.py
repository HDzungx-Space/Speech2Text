import speech_recognition as sr
import pyttsx3

# Initializing the recognizer
recognizer = sr.Recognizer()

# Function for text to speech conversion
def Text2Speech(command):
    # Initializing the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# create a recognizer object
r = sr.Recognizer()

# specify the path of the audio file
audio_file = "demo.wav"

# open the audio file using the recognizer object
with sr.AudioFile(audio_file) as source:
    # read the audio data from the file
    audio_data = r.record(source)

# convert the audio data to text
text = r.recognize_google(audio_data)
text = text.lower()

# Confirmation using text and audio
print(text)
Text2Speech(text)

# # Handling exceptions at the runtime
# try:

#     # using microphone as input source.
#     with sr.Microphone() as source2:

#         # Adjusting the energy threshold based on the surrounding noise level
#         print("Calibrating background noise...")
#         recognizer.adjust_for_ambient_noise(source2, duration=0.2)
#         print("Calibration successful. Prescribe!")

#         # listening user's input
#         audio2 = recognizer.listen(source2)

#         # Using Google Web Speech API to recognize audio
#         text = recognizer.recognize_google(audio2)
#         text = text.lower()

#         # Confirmation using text and audio
#         print(text)
#         Text2Speech(text)

# except sr.RequestError as e:
#     print("Could not request results; {0}".format(e))

# except sr.UnknownValueError:
#     print("unknown error occurred")

