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
    
    

session_token = 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..TniBNyWhgnFyR7x5._AukFmbVq6_0MMIZwMPHylhKMvHex1tmQ43OJIaG0EDk7jhaf_HH5tcCEAJSq_A1h_SZeGTc1k38_KP4NXITau8O8hIgxDulX2RjN4gBUMRy9zLBP5JA7WF5jB6zITZCAEHHZMFK1bHy2qhulufhzi8Ragsws8rPR9_Am8ADAGUSomUYDBdcGPNvVgo_GeErbfqFIaH3rWQqa4BfM2sGygyYVXtkoFS43fydYTScu7_byrz_ze9xw0Xs1mONc9KladIT6s4YAGOgnmjdduipkdQp_AYshOSlZdwbIVtWqwNXn0t-xRY6C2-rwRi2IOe0iAmX_QWBZJX6ltxxgaAr9BkOvKu4Lv-f1f-iNMxHEcrSwjZJe2iPTKuyjTqFZA2Gy--o-1cwsoWEOINGjuGnr-HelH7N05xIXS6PG6BjZHQwp5IvqnATJdGsTIRwTMo4fAjvyypP1hKN5dZQOdfSj70AJWmQ-4F5leOSahR3PdMhIA46WaGMdZ8zcXusS-YQCdOYfENhVkvfhPSnUruYc3sramBC1qU78Loh4USyKn1AALbv1iMRyxOZNxjZlM_9o6JJQ1t4fOOalYgb44hby2V1A5N6IYm3XhxZhXThlHAe9FahzBG6zyHYo2tcG4jmljKcUof2N6ApnzksUREqTLCn_c-s11V23knOspdIqThMpeDPupVVFNkNWi7Jm_XILiDDTzE0Eh3hOGO-HuRtlb7w2swzWXpKoZNsu4DVWFQNB6ftLI37w06Y8NiiwCbdB_qMnFycWVmOk6Fk30R_0gN5btud8zRJo8HW7dMBnbdW-QaaYCknmBgVYYHRUa9evVC4GGqFmUYqX18mRT17hjfOdorKugxTlcJgpdsazNV8aqFV3dqHu0zbdGT7b0n8SSoKOJKYbE3YKEsQaaUPHbBGj9h2fEoNllAPj_agcebCQ12ouBpK91aSBUHP2AEyKQCWDvFQooBMle4haJ7PyTN5YATSbF3WDYWLEQu9LadJzDdl1Got9n25FG5daLmYAC4t74P_-8jTJ0GO4tkO454WG4r3EqHydnCDT-fInda7GmrQWisJvqkWt_J2cCMooKUKm1sfY2me19sgkoliggpt6lKtLNwUKOUy3QZerNzt3T-S_Z0tVLgklYvxcgYl7quWLUiZgtIWpAyjVs3fIUcPKCwXZWYTFtNn1iWSovbaG30PDzCrifDgecDOYlSJRIBLm2Wamx-MzP24_Pei4tIapt-E2EKzNiEYt6IAQYn4y_rm-A9GbK_DVyPKbf4CMAObmNOE-qu4Htg_1XaZmIHjZXbKY58yrpc-GkFL5atv39xPnlM4oAlIkG4dHjqVeRwZWyicxv7BrHuG4AxI58AyC8lIkOlJUFhP-oe_7jmL-cXT-aeb9ElITIFv4kamP_jIQD4Vgdzop_dJKa2Jw8HpG6RseLG4RS1ufJSDeBGDD0CDUtuc7InCUCTWhW0s8_afBxbI8pn-tnW6tGov0jEYwrX9Ed9Xn1wICgmWn1ZlfVHuFGRqWFeuVcyBzem_m6DW5IQni6cz2v-nAe6c2Tb2TWLO_Yas2KJDDNAg-Cx2U_BKy31CWYV89dGVfeAvALPMy36FOgqtQXot93yTWDwKZfk02mtiuj_wp7taf-P5MwCvZGs3ndb5N-i6svZ0nWVbxrc3L-fzICfZN_TGaHAVlmn5053wf6VqVo5SyO9n_1OXfiU89wypml-1DqjwG98sJ8wZoGLZ1qjdHj2JhfYtdq-q5tlg9WV22LwyS6VgyoQFQnt7PTD4ob71lBbIdeDCXeeWo2cPHuOaJAXeeGRAsI1D4cGW25Ja0DGV_YgZKJogOKLKIj6BdzOedMzgudDhew1sxk4T3DbP0dHrZjXK6lsSr14SJrsRExERq-zgPLWsX_zQmq2AEV_Ht01BIJuu4g-xT86Phy9pvorBJF0rh_YNnk8B-0Zl4t7aa67E85_NDswxkfq9XFTb2PtH5Vk0SKUPPRZfKT3FwJIDb5fRjZl5ucs1Ey2ZV3TWeUZgGAYDTUrnV-RR6Qh5AdvsWuM6R3l9plgfx1MABm__83-papuVFDUTz-SYKROjhGqBXR6PgQnqNcXwTBcHBUB73csfyMFaXzRST5GF7fWo-RAlrVIdr6fxL2i82jYpzbytnlrQXMHOSWjyGMFL4TGZUBI7jCN5BNx6qi5otfNAiRJOLxsL_wqefNhZLEI7fEKxRSf-vEWfiIGWBQyYD02G0MFgqCMDXFRCIzusvEd-HWjHF-2FJV3goTitQcBV2oTKSBsT-NYPBDfpNRYr5A3jYZsEvphEYfnceKsQvm_bCNmtWIFMpb3XwMttF5nM4FIa-5wqa0qOzN-7cN0U6TyfCfe1ofAgbwUWfCFnJp2df4vINqWLwQbV0hTlNwiIPmv3Vy4TbtZxVLlv37vF9CGVW-d6jGa7HJ8nNiaxb9lweI10PJeSide7-ydiKJabZK6GXdK6CJsYaDZ60J-0TxUzp3828iGr0vTXQZaKvNH1EdPG1JRWNELXho9x0ffK50ovdfP-41f4DQvenPTC-ihr4DFEU8YhL8RCAnsvwJFKrWKM3BbAXnBy7vqELsDsoyceZQWdodTgMBAR6cLPom5Ic79wA5hxcfSB3io9l8rDxmn7TZy4tnZ8hT3hG8iIzf_gjdx_CVp7jU6w0XZYST3hAMc3WqfkOXV0lKSnhHkBPYj47CHDddYhvyk.yOMbXFBBG-1LkUOwJmZAZg'
api = ChatGPT(session_token)  # auth with session token
api = ChatGPT(session_token, conversation_id='1')  # specify conversation id
#api = ChatGPT(session_token, proxy='https://proxy.example.com:8080')  # specify proxy
#api = ChatGPT(session_token, chrome_args=['--window-size=1920,768'])  # specify chrome args
api = ChatGPT(session_token, moderation=False)  # disable moderation
api = ChatGPT(session_token, verbose=True)  # verbose mode (print debug messages)


# auth with openai login (captcha solving using speech-to-text engine)

api = ChatGPT(auth_type='openai',  email='20201701631@cis.asu.edu.eg', password='Abdullah_2002')

# auth with openai login (manual captcha solving)

#api = ChatGPT(
#    auth_type='openai', captcha_solver=None,
#    email='20201701631@cis.asu.edu.eg', password='Abdullah_2002'
#)

# auth with openai login (2captcha for captcha solving)

#api = ChatGPT(
#    auth_type='openai', captcha_solver='2captcha', solver_apikey='abc',
#    email='20201701631@cis.asu.edu.eg', password='Abdullah_2002'
#)

# reuse cookies generated by successful login before login,
# if `login_cookies_path` does not exist, it will process logining  with `auth_type`, and save cookies to `login_cookies_path`
# only works when `auth_type` is `openai` or `google`

#api = ChatGPT(auth_type='openai', email='20201701631@cis.asu.edu.eg', password='Abdullah_2002',
#    login_cookies_path='your_cookies_path',
#)


myvoice = listen().lower()
resp = api.send_message(myvoice)
speak(resp['message'])


api.reset_conversation()  # reset the conversation
api.clear_conversations()  # clear all conversations
api.refresh_chat_page()  # refresh the chat page




