import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
import time

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Create a function to listen to the user's voice and return the text
def listen():
    with sr.Microphone() as microphone:
        recognizer.adjust_for_ambient_noise(microphone)
        audio = recognizer.listen(microphone)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
    except sr.RequestError:
        print("Sorry, there was an error with the speech recognizer.")

# Create a function to speak the text to the user
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Create a function to open a web page in the user's browser
def open_webpage(url):
    webbrowser.open(url)

# Create a function to execute a command on the user's computer
def execute_command(command):
    os.system(command)

# Start the main loop
while True:
    # Listen to the user's voice
    text = listen()

    # If the user says "exit" or "stop", stop the program
    if text in ["exit", "stop"]:
        break

    # If the user says "time", tell them the time
    if text == "time":
        speak(time.strftime("%H:%M:%S"))

    # If the user says "search Wikipedia", search Wikipedia for the given query
    if text.startswith("search Wikipedia"):
        query = text.replace("search Wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak(results)

    # If the user says "open a web page", open the given web page
    if text.startswith("open a web page"):
        url = text.replace("open a web page", "")
        open_webpage(url)

    # If the user says "execute a command", execute the given command
    if text.startswith("execute a command"):
        command = text.replace("execute a command", "")
        execute_command(command)

    # If the user says anything else, try to understand what they're asking and respond accordingly
    else:
        speak("I'm not sure what you mean. Can you please rephrase your question?")
