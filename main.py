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
from processor.TextProcessor import TextProcessor
num = 1


if __name__ == "__main__":
    # assistant_speaks("What's your name, Human?")
    name = 'My name is sandra. Am a hustler'
    # name = get_audio()
    AssistantSpeak().assistant_speaks("Hello," + name + '.')
    while (1):
        AssistantSpeak().assistant_speaks('What can i do for you?')
        text = AssistantSpeak.get_audio().lower()
        if text == 0:
            continue
        # assistant_speaks(text)
        if "exit" in str(text) or "bye" in str(text) or "go " in str(text) or "sleep" in str(text):
            AssistantSpeak().assistant_speaks("Ok, bye")
            break
        TextProcessor().process_text(input=text)
