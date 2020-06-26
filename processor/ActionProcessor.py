from selenium import webdriver  # to control browser operations
import subprocess
import re
from .AiProcessor import AssistantSpeak


class ActionProcessor:
    @staticmethod
    def search_web(input):
        driver = webdriver.Firefox()
        driver.implicitly_wait(1)
        driver.maximize_window()
        if 'youtube' in input.lower():
            AssistantSpeak().assistant_speaks("Opening in youtube")
            indx = input.lower().split().index('youtube')
            query = input.split()[indx + 1:]
            driver.get("http://www.youtube.com/results?search_query=" + '+'.join(query))
            return

        elif 'wikipedia' in input.lower():
            AssistantSpeak().assistant_speaks("Opening Wikipedia")
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

    @staticmethod
    def open_application(input):
        reg_ex = re.search('launch (.*)', input)
        if reg_ex:
            appname = reg_ex.group(1)
            appname1 = appname + ".app"
            subprocess.Popen(["open", "-n", "/Applications/" + appname1], stdout=subprocess.PIPE)
            AssistantSpeak().assistant_speaks('I have launched the desired application')
            return
