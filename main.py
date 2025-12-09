import speech_recognition as sr
import webbrowser
import pyttsx3

def speak(text):    
    ttsEngine = pyttsx3.init()  # will convert text to speech
    ttsEngine.setProperty("rate", 150)
    ttsEngine.setProperty("volume", 1.0)
    ttsEngine.say(text)
    ttsEngine.runAndWait()

def processCommand(c):
    ToDo = c.lower()
    if "open google" in ToDo:
        speak("Opening google")
        webbrowser.open("https://google.com")
    elif "open youtube" in ToDo:
        speak("Opening youtube")
        webbrowser.open("https://youtube.com")
    elif "open instagram" in ToDo:
        speak("Opening instagram")
        webbrowser.open("https://instagram.com")
    elif "open facebook" in ToDo:
        speak("Opening facebook")
        webbrowser.open("https://facebook.com")

if __name__ == "__main__":
    speak("initializing Jarvis....")
    while True:
        recognizer = sr.Recognizer() # will recognize the speech
        with sr.Microphone() as source:
            print("Listening....")
            try:
                # recognizer.adjust_for_ambient_noise(source) # Adjust for background noise
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
                word = recognizer.recognize_google(audio)   
                
                if "jarvis" in word.lower() or "hey jarvis" in word.lower() or "hello jarvis" in word.lower():
                    speak("Yaa?")
                    print("Jarvis Active!!!!") 
                    with sr.Microphone() as source:    
                        # recognizer.adjust_for_ambient_noise(source) 
                        doCommand = recognizer.listen(source)
                        cmdTextFormat = recognizer.recognize_google(doCommand)                        
                        processCommand(cmdTextFormat)

            except sr.WaitTimeoutError:
                print("Timeout: No speech detected.")
                continue # Continue to the next iteration of the loop

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")

            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
