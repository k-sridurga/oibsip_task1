import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    print("Voice Assistant:", text)  # Print the voice assistant's response
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-us')
        print(f"User said: {query}")
        return query.lower()
    except Exception as e:
        print(e)
        return ""

# Function to respond to user commands
def respond(query):
    if "hello" in query:
        speak("Hello! How can I assist you today?")
    elif "what's the time" in query:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    elif "what's the date" in query:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}")
    elif "search for" in query:
        search_query = query.replace("search for", "")
        url = f"https://www.google.com/search?q={search_query}"
        webbrowser.open(url)
    elif "exit" in query:  # Check for exit command
        speak("Ok, I'm leaving.")
        exit()  # Stop the program
    else:
        speak("I'm sorry, I didn't understand that.")

# Main loop for the voice assistant
def main():
    speak("Hello! I am your voice assistant.")
    while True:
        query = listen()
        if query:
            respond(query)

if __name__ == "__main__":
    main()
