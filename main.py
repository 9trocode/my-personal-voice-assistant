import speech_recognition as sr  # importing speech recognition package from google api
# from pygame import mixer
import playsound  # to play saved mp3 file
from gtts import gTTS  # google text to speech
import os  # to save/open files
import wolframalpha  # to calculate strings into formula, its a website which provides api, 100 times per day
from selenium import webdriver  # to control browser operations
from selenium.webdriver.common.keys import Keys
from io import BytesIO
from io import StringIO
import subprocess
import re
import requests
from time import strftime

num = 1


def assistant_speaks(output):
    """speaks audio passed as argument"""
    print(output)
    for line in output.splitlines():
        os.system("say " + output)


def get_audio():
    r = sr.Recognizer()
    audio = ''
    with sr.Microphone() as source:
        print("Speak...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    print("Stop.")
    try:
        text = r.recognize_google(audio, language='en-NG')
        print("You : ", text)
        return text
    except:
        assistant_speaks("Could not get that, Please try again!")
        command = get_audio();
        return command


def search_web(input):
    driver = webdriver.Firefox()
    driver.implicitly_wait(1)
    driver.maximize_window()
    if 'youtube' in input.lower():
        assistant_speaks("Opening in youtube")
        indx = input.lower().split().index('youtube')
        query = input.split()[indx + 1:]
        driver.get("http://www.youtube.com/results?search_query=" + '+'.join(query))
        return

    elif 'wikipedia' in input.lower():
        assistant_speaks("Opening Wikipedia")
        indx = input.lower().split().index('wikipedia')
        query = input.split()[indx + 1:]
        driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query))
        return
    else:
        if 'google' in input:
            indx = input.lower().split().index('google')
            query = input.split()[indx + 1:]
            driver.get("https://www.google.com/search?q=" + '+'.join(query))
        elif 'search' in input:
            indx = input.lower().split().index('google')
            query = input.split()[indx + 1:]
            driver.get("https://www.google.com/search?q=" + '+'.join(query))
        else:
            driver.get("https://www.google.com/search?q=" + '+'.join(input.split()))
        return


def open_application(input):
    reg_ex = re.search('launch (.*)', input)
    if reg_ex:
        appname = reg_ex.group(1)
        appname1 = appname + ".app"
        subprocess.Popen(["open", "-n", "/Applications/" + appname1], stdout=subprocess.PIPE)
        assistant_speaks('I have launched the desired application')
        return


def process_text(input):
    try:
        if "who are you" in input or "define yourself" in input:
            speak = 'Hello, I am Chiamaka. Your personal Assistant. I am here to make your life easier. You can command me to perform various tasks such as calculating sums or opening applications etcetra'
            assistant_speaks(speak)
            return
        elif "who made you" in input or "created you" in input:
            speak = "I have been created by Nitrocode Alex."
            assistant_speaks(speak)
            return
        elif "how are you" in input:
            speak = "Am doing great and you ?"
            assistant_speaks(speak)
            return
        elif "good morning" in input or "morning" in  input:
            speak = "Good Morning, how are you doing today"
            assistant_speaks(speak)
            return
        elif "Am fine" in input or "fine" in input:
            speak = "Good to know that you are fine"
            assistant_speaks(speak)
            return
        elif "crazy" in input:
            speak = """Well, there are 2 mental asylums in India."""
            assistant_speaks(speak)
            return
        elif "calculate" in input.lower():
            app_id = "E46YXW-T5LG6RT7K7"
            client = wolframalpha.Client(app_id)

            indx = input.lower().split().index('calculate')
            query = input.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            assistant_speaks("The answer is " + answer)
            return
        elif 'open' in input:
            open_application(input.lower())
            return
        elif 'search' in input or 'play' in input:
            search_web(input.lower())
            return
        elif 'hello' in input:
            day_time = int(strftime('%H'))
            if day_time < 12:
                assistant_speaks('Hello Sir. Good morning')
            elif 12 <= day_time < 18:
                assistant_speaks('Hello Sir. Good afternoon')
            else:
                assistant_speaks('Hello Sir. Good evening')
        elif 'joke' in input:
            res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept": "application/json"})
            if res.status_code == requests.codes.ok:
                assistant_speaks(str(res.json()['joke']))
            else:
                assistant_speaks('oops!I ran out of jokes')
        else:
            assistant_speaks("I can search the web for you, Do you want to continue?")
            ans = get_audio()
            if 'yes' in str(ans) or 'yeah' in str(ans):
                search_web(input)
            else:
                return
    except Exception as e:
        print(e)
        assistant_speaks("I don't understand, I can search the web for you, Do you want to continue?")
        ans = get_audio()
        if 'yes' in str(ans) or 'yeah' in str(ans):
            search_web(input)


if __name__ == "__main__":
    # assistant_speaks("What's your name, Human?")
    name = 'I am NitroCode, am here to make your life easier'
    # name = get_audio()
    assistant_speaks("Hello," + name + '.')
    while (1):
        assistant_speaks("What can i do for you?")
        text = get_audio().lower()
        if text == 0:
            continue
        # assistant_speaks(text)
        if "exit" in str(text) or "bye" in str(text) or "go " in str(text) or "sleep" in str(text):
            assistant_speaks("Ok bye, " + name + '.')
            break
        process_text(text)
