from inflect import engine
import pyttsx3


def speak(audio):
	engine = pyttsx3.init()
	engine.setProperty('volume', 4)
	# getter method(gets the current value
	# of engine property)
	voices = engine.getProperty('voices')
	# setter method .[0]=male voice and
	# [1]=female voice in set Property. 
    #engine.setProperty('volume',1.0)
	engine.setProperty('voice', 'mb-en1')
	engine.setProperty('rate', 120)
	# Method for the speaking of the assistant
	engine.say(audio)
	# Blocks while processing all the currently
	# queued commands
	engine.runAndWait()

speak("Hello World ! , How are you ?")

