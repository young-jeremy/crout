import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Use the microphone as the source
with sr.Microphone() as source:
    print("Adjusting for ambient noise... Please wait.")
    recognizer.adjust_for_ambient_noise(source)
    print("Listening for speech... Please speak now.")
    audio = recognizer.listen(source)

try:
    # Recognize speech using Google Web Speech API
    print("Recognizing... Please wait.")
    text = recognizer.recognize_google(audio)
    print(f"You said: {text}")
except sr.UnknownValueError:
    print("Sorry, I could not understand the audio.")
except sr.RequestError:
    print("Sorry, the service is unavailable.")
