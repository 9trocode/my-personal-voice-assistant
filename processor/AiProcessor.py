import os  # to save/open files
import speech_recognition as sr  # importing speech recognition package from google api


class AssistantSpeak:

    @staticmethod
    def assistant_speaks(output):
        """speaks audio passed as argument"""
        print(output)
        for line in output.splitlines():
            os.system('say ' + output)

    @staticmethod
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
            AssistantSpeak.assistant_speaks('Could not get that, please try again')
            command = AssistantSpeak.get_audio()
            return command
