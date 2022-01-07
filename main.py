import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command=command.lower()
            if 'hey buddy' in command:
                command = command.replace('hey buddy', '')
                print(command)



    except:
        pass
    return command

def run_buddy():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('current time is ' + time)
        print('Time is ' + time)

    elif 'search' or 'what' in command:
        info = command.replace('search', '')
        talk(('Some results are ' + info))
        pywhatkit.search(info)

    else:
        talk('Please say the command again')
while True:
    run_buddy()