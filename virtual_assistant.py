import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


# hear the microphone and return the audio as text
def transform_audio_into_text():
    # store recogniser in variable
    r = sr.Recognizer()

    # set microphone
    with sr.Microphone() as source:

        # waiting time
        r.pause_threshold = 0.8

        # report that recording has begun
        print("You can now speak")

        # save what u hear as audio
        audio = r.listen(source)

        try:
            # search google
            request = r.recognize_google(audio, language='en-gb')

            # test in text
            print('You: ' + request)

            # return request
            return request

        # In case it doesn't understand the audio
        except sr.UnknownValueError:

            # show proof that your didn't understand the audio
            print("Oops! I didn't understand the audio")

            # return error
            return 'I am still waiting'

        # In case the request cannot be resolved
        except sr.RequestError:

            # show that your request not good
            print("Oops! there is no service")

            # return audio
            return 'I am still waiting'

        # In case any other error
        except:

            # show that your request not good
            print("Oops! something went wrong")

            # return audio
            return 'I am still waiting'


# voice options
girl = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
boy = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'


# The assistant can speak
def speak(message):
    # start engine
    engine = pyttsx3.init()

    # say message
    engine.setProperty('voice', girl)
    engine.say(message)

    # waiting
    engine.runAndWait()


# Day
def ask_day():
    # Date
    date = datetime.date.today()
    print(f'The date is {date.day}/{date.month}/{date.year}')
    # Print day name
    day = date.weekday()
    day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thurday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
    speak(f'Today is {day_dict[day]} and todays date is {date}')


# Time
def ask_time():
    # Time
    time = datetime.datetime.now()
    print(f'The time is {time.hour} hours and {time.minute} minutes')
    speak(f'The time is {time.hour} hours and {time.minute} minutes')


# Greetings
def initial_greetings():
    print("Hello, I am Qadir's assistant Dumb Erum. How can i help you today!")
    speak("Hello, I am Qadir's assistant Dumb Erum. How can i help you today!")


# Assistant
def my_assistant():
    initial_greetings()

    # starting loop
    go_on = True
    while go_on:
        statments = transform_audio_into_text().lower()

        if 'open youtube' in statments:
            speak('Ok boss, Opening Youtube')
            webbrowser.open('www.youtube.com')
            continue
        elif 'open google' in statments:
            speak('Ok boss, Opening Google')
            webbrowser.open('www.google.com')
            continue
        elif 'what day is today' in statments:
            ask_day()
            continue
        elif 'what time is now' in statments:
            ask_time()
            continue
        elif 'search the wikipedia' in statments:
            speak("Ok boss! I am looking for it")
            statments = statments.replace('search the wikipedia about','')
            answer= wikipedia.summary(statments,sentences= 1)
            speak(f'This is what i found on wikipedia! {answer}')
            continue
        elif 'search the internet about' in statments:
            speak('Ok boss! Searching the internet')
            statments = statments.replace('search the internet about','')
            pywhatkit.search(statments)
            continue
        elif 'joke' in statments:
            jokes = pyjokes.get_joke('en')
            print(jokes)
            speak(jokes)
        elif 'play' in statments:
            speak('Ok boss!, I will play it for you')
            pywhatkit.playonyt(statments)
        elif 'goodbye hazel' in statments:
            speak('good bye boss! Call me whenever you need me.')
            break
my_assistant()
