import random
from gtts import gTTS
from gtts.tokenizer.pre_processors import abbreviations, end_of_line
from pygame import mixer
import speech_recognition as sr
import os
import time
import webbrowser
import sys
import pyjokes
from pyChatGPT import ChatGPT


GREETINGS = ["hello", "jarvis", "wake up", "are you there", "time to work", "hey",
             "ok jarvis", "you there"]

GREETINGS_RES = ["always there for you sir", "i am ready sir",
                 "your wish my command", "how can i help you sir?", "i am online and ready sir"]


# Speaking Method 
def speak(text_to_speak):
    tts = gTTS(text_to_speak, slow=False, lang_check=True, lang="en", tld='us',pre_processor_funcs = [abbreviations, end_of_line]) 
    tts.save('audio.mp3')
    mixer.init()
    mixer.music.load("audio.mp3")
    mixer.music.set_volume(20)
    mixer.music.play()
    while mixer.music.get_busy():
        pass 

def greeting():
    speak("Hello Sir. How Can I Help You Today ? ")

# Listening Method
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        return "None"
    return query


def WakeUp():
    speak("Starting all systems applications")
    speak("All systems have been activated")
    speak("Now I am online")
    while True:
        
        myvoice = listen().lower()
        if myvoice in GREETINGS:
            speak(random.choice(GREETINGS_RES))
        if "time" in myvoice and "what" in myvoice:
            speak("The time is " + time.strftime("%I:%M %p") + " right now")
        if "date" in myvoice and "what" in myvoice:
            speak("The date is " + time.strftime("%d/%m/%Y") + " right now")
        if "shutdown speech recognition" in myvoice:
            speak("shutting down speech recognition")
            time.sleep(1)
            speak("Goodbye Sir")
            break
        if "thank you" in myvoice:
            speak("You are welcome Sir")
        if "how are you" in myvoice:
            speak("I am fine Sir. Thank you for asking")
        if "what is your name" in myvoice:
            speak("My name is Jarvis Sir")
        if "who made you" in myvoice:
            speak("I was made by Mr. Abdallah Hussam")
        if "search" in myvoice:
            speak("Searching" + myvoice.replace("search", ""))
            webbrowser.open("https://www.google.com/search?q=" + myvoice.replace("search for", ""))
            continue
        if 'tell me about' in myvoice:
                topic = myvoice.split(' ')[-1]
                if topic:
                    wiki_res = obj.tell_me(topic)
                    print(wiki_res)
                    speak(wiki_res)
                else:
                    speak(
                        "Sorry sir. I couldn't load your query from my database. Please try again")
        if "joke" in myvoice:
               joke = pyjokes.get_joke()
               print(joke)
               speak(joke)
        if "take screenshot" in myvoice or "take a screenshot" in myvoice or "capture the screen" in myvoice:
              speak("Alright sir, taking the screenshot")
              os.system("coreshot -f")
    
    
from pychatgpt import Chat
import time
from pychatgpt import OpenAI

# Manually set the token
OpenAI.Auth(email_address="20201701631@cis.asu.edu.eg", password="Abdullah_2002").save_access_token(access_token="eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..Onf2_SmyhYb3GoV6.DmcJGiR5HbFKhCjTMDZ7UIGzk_5eDLo7U0DQwI5c0wO1KyOZjf9h4jAXpcQvBlqDy1tT8Ub3ccpptv0cz0t3qikz7XY5MNTW9sgbtZf-jq__jsjClvxzgLDUb3YyzV8rGSnB3YsV7AHeHF2EUdQgx8q3dH79OZynBoDHXd-NcapPwAdBAyUW54RCgUvWTW__lW3k0xnHNxLCiEegI1d4BxwlV2kDm4TQlTSA_otDhVhcMKfolduaYfdjKRI9OXT3wPvi8SQIxmqhwQn7vb5QCPd51hm05RzxpWYr_X6LNVd0KBoATfxvSaSsld6Y1KNr-mX4r4ZzhsqI8i4uZU6BXlD04uC3aqmj0zomYopZReu36QrN5n8iSZEL2VkXjDh_BCn8jfb-iJU5lHQ13PaFT0oWGmMIW406E4RK8P_Dz0aRwbt5tIhDuL1OcbwiJ434aC2UodR_J_g2I7crzKvSrU3md_ftgVOX5cRu-GKiQJtnS__xaGMmIJprS82V6goHoIfZRRCioyf6WasHddwQxQSiaal_CNKMmJrYoklxp5eE-oJ11r50CNr8dSeaJYDI6N7rLJwecJ3gNy9oNouXdKlGkDWzgdExRJMKJmype7nYj1Saa4HJiWR9ChL2QClDMEY2ZvIhQvlN8l-aq-u8Wk2p1GKoxqHJmDrhPcVQTZ0VVe8nrX0pJraL_EdwXSr2h2PNHJ_IZPyvZK_2x6m4I00gS8YTt9LMZ6-1iYal-c8shuL_O7Fu3PKtus_wSAeBrqkxflEU9gJdFicODzyvDw3ccTTl04wXxOGyY4fhP8km5mL26WsyAwI_vKa-y1Yrb_2y-wwXRHvUh1ybckVur2gk7WED9aaelVAzSFZiDcbw-CEPYurzvN4RTjVuvg3uO3btdK2X4VqUtovPBxQA8U8nPtaUVStQ-uvnN57htXMjzjKMMeUI7ddzcSvv35t3ulKNsS9kptxDvQVcZT6u4SAv7GN25sWYg123mjoWr93OXbR5LHeHWM4IRz0vL8D_39GvphhbAHZj30w_lKMqI5kokN_G6s5vcnjFIRc20aEWSIQFgrx77jofH1UuikZT2LsVJmQ1We90j9o_3JpSikn6ReEiCxseaK9YoqwOQ9hIWCaY5li_YuUZy14YPWaCQPhLnQxwsZ-wQR66L9AQa4ytAoh0y9-gXiltOjsFMKl6gYLx6Pa7vLfUXKLIVDw8zQ82VcBUMufhAbbbo24REpPwTMdD0_Dyz5H7Ee4MoS8f48qHUp6bYU258F4IvD6vtab_sTMRousP2f_ZsC_lqNxkxK3lxN2S3yGmLVXeO837mjYtDX7603wD22-VQI96oa3dESJq-_U8r3fTACURdov0ECD4Vk-mS8ppIKvi62pX-R10lYJLnnjxoF7fOs2kBtfCCXSgVn7gMKvMLAfvz3PyVZeAKXNFufXofqa7-lvjGePURSxhFdtdKZsILqYpYTTUXovZTb2bTHyUUstgFyLPJZa-x4d_wgVjCO2kPyAz9-vvYkM_O0HRYLQ4MBErtWto_Q-Hi8Cdhpvbmz3yszF9L2Mm9cPwhDoYRY_Ws0jx1BICrpgm55YX9sYs4moFGeUDfqQ8ZktS7EUug7k7doxhb4rMK4U0dmJQDwMuuj_uRy3bHO4yTTWoRnA2FgXacIbbJNo1p_6nLl0inc40fYPQmd965KsT_AgnHbDRvRXZzu7sU8nTqp-fulLltQxFoB1WUHhuHJNxER9Qx1xkuuKsbEBkYU1IPYnhHD86ukTizT99QwOAc0tZF-UPyn7ty2T7Wl_ztLljDuYptJrC0JbSlphRE3erxicz2By6l4Jw0yQkp9N3-RpQTQnBe6YQpLm-CIM4omulUuNtdHKYkDNYb2M9QddaCNizI2DHH3yPQJtUKAa-3GuswWBPpzyv9hzKZwiEeiCtsB-bAD9OPRusx8ZjbnU57JZcJDPzaTmDIDh29LBJphdj80_sfMZD7ldaNU8p1U_1kWuUO69TqhSs_aNfAYwq_RcXQQE_ye6xeOO9V5anJNcSfz5KbfRrzgfv7uMAB6jpBXen_l7eiKfkRspaw1r62QdSGP7Iwwb54ECAvAtJGNLl4mf_Go_rtd9AHAHkpGOYb7EhoNL5P9XjUfpaVCewOefO5nJU9r9wgs2cTM3l96DKBR2yI-vYEjJrHG0MGpYdcp99y1c_NcyaCZDNkJAyMYjOzHLJpxOEoOV6ZXppOgFIBBnhxexJj_6kighsR3pHghavxQqWhZAxng6Dt_HJ1Mq-AocH1VkVb0tHg-YhpzwuTSWJxwv-Z270vSQXWX0R6ARpA1LK1EgLOuhkSG9d7CjhdE8NnC4nhRh6_mByfS1yEpBsiIDBom3AzlQtZhdxufr-4rA9lfX7tLjaHboEWeUegzq0ravkYiJ_zAHzWd6GRI1UVJMPfN8DOO2q1EMzOM50GhCr4N8s6ovTgTSsu8TvGGJvT8Z7YEFe1hfaNEA4E8BkC-2VruNSVqFLloAaZJ9OX5ekRyxywNUCAdrZifgs7eFcwvReYQre0PlF2Qv0np5KBFXVlOue4UK-odumQsDa8ElFNbX9chGjwj8DViOhGWjl_P-k71eaRvAflqGBkto1oArCFZodW45ccAcNADr8D3FyUfL3wWEcj7pG34jM5ZoIFUbzLirDykTMMAbVr5NUWm2C1U0hxKHYwwWunwLQIGn0bYf_ptJzzpOpmbw.MGu_-Y7pKPkv9edDJLbgHg", expiry=time.time() + 3600)

# Get the token, expiry
#access_token, expiry = OpenAI.get_access_token()

# Check if the token is valid
#is_expired = OpenAI.token_expired() # Returns True or False

myvoice = listen().lower()

# Create a Chat object
chat = Chat(email="20201701631@cis.asu.edu.eg", password="Abdullah_2002", 
            conversation_id="Parent Conversation ID", 
            previous_convo_id="Previous Conversation ID")

answer, parent_conversation_id, conversation_id = chat.ask(myvoice)

speak(answer)

# Or change the conversation id later

