import speech_recognition as sr
import pyttsx3

def speak(text):
    """
    Convert text to speech.
    :param text: Text to be spoken
    """
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"User said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        print("Sorry, my speech service is down.")
        return ""

def main():
    speak("Hello, how can I assist you today?")
    while True:
        command = recognize_speech().lower()

        if "hello" in command:
            speak("Hello! How can I help you?")
        elif "who are you" in command:
            speak("I am your voice assistant.")
        elif "how are you" in command:
            speak("I am fine and what about you.")
        elif "exit" in command:
            speak("Goodbye!")
            break
        else:
            speak("I am sorry, I did not understand that. Please try again.")

if __name__ == "__main__":
    main()
