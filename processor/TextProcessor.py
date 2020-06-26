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
from processor.AiProcessor import AssistantSpeak
from .ActionProcessor import ActionProcessor
num = 1


class TextProcessor:
    @staticmethod
    def process_text(input):
        try:
            if "who are you" in input or "define yourself" in input or "what's your name" in input:
                speak = 'Hello, I am Chiamaka. Your personal Assistant. I am here to make your life easier. You can command me to perform various tasks such as calculating sums or opening applications etcetra'
                AssistantSpeak().assistant_speaks(speak)
                return
            elif "who made you" in input or "created you" in input:
                speak = "I have been created by Nitrocode Alex."
                AssistantSpeak().assistant_speaks(speak)
                return
            elif "how are you" in input:
                speak = "Am doing great. and you ?"
                AssistantSpeak().assistant_speaks(speak)
                return
            elif "good morning" in input or "morning" in input:
                speak = "Good Morning, how are you doing today"
                AssistantSpeak().assistant_speaks(speak)
                return
            elif "Am fine" in input or "fine" in input:
                speak = "Good to know that you are fine"
                AssistantSpeak().assistant_speaks(speak)
                return
            elif "crazy" in input:
                speak = """Well, there are 2 mental asylums in India."""
                AssistantSpeak().assistant_speaks(speak)
                return
            elif "calculate" in input.lower():
                app_id = "E46YXW-T5LG6RT7K7"
                client = wolframalpha.Client(app_id)

                indx = input.lower().split().index('calculate')
                query = input.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                AssistantSpeak.assistant_speaks("The answer is " + answer)
                return
            elif 'open' in input:
                ActionProcessor().open_application(input.lower())
                return
            elif 'search' in input or 'play' in input:
                ActionProcessor().search_web(input.lower())
                return
            elif 'hello' in input:
                day_time = int(strftime('%H'))
                if day_time < 12:
                    AssistantSpeak.assistant_speaks('Hello Sir. Good morning')
                elif 12 <= day_time < 18:
                    AssistantSpeak.assistant_speaks('Hello Sir. Good afternoon')
                else:
                    AssistantSpeak.assistant_speaks('Hello Sir. Good evening')
            elif 'joke' in input:
                res = requests.get(
                    'https://icanhazdadjoke.com/',
                    headers={"Accept": "application/json"})
                if res.status_code == requests.codes.ok:
                    AssistantSpeak.assistant_speaks(str(res.json()['joke']))
                else:
                    AssistantSpeak.assistant_speaks('oops!I ran out of jokes')
            else:
                AssistantSpeak.assistant_speaks("I can search the web for you, Do you want to continue?")
                ans = AssistantSpeak.get_audio()
                if 'yes' in str(ans) or 'yeah' in str(ans):
                    ActionProcessor().search_web(input)
                else:
                    return
        except Exception as e:
            print(e)
            AssistantSpeak.assistant_speaks("I don't understand, I can search the web for you, Do you want to continue?")
            ans = AssistantSpeak.get_audio()
            if 'yes' in str(ans) or 'yeah' in str(ans):
                ActionProcessor().search_web(input)
