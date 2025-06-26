import speech_recognition as sr

#pip install SpeechRecognition
#pip install pyaudio

# Initialize recognizer
recognizer = sr.Recognizer()

# Use microphone as the audio source
with sr.Microphone() as source:
    print("Please speak something...")
    recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
    try:
        # Capture audio from the microphone
        audio = recognizer.listen(source)
        print("Recognizing...")
        # Convert speech to text
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
