#This actually works At the moment - this is the file you are looking for
#It takes chat messages, makes them into a buffer file, then plays the audio and automatically adds all chat messages into a queue to be converted then played as audio (means only 1 audio file will exist at a time for this and will be constantly written over, which is fine lol) 
#Needs Stream ID (aka the videoID of the stream) in order to pull the data it needs 


# print(f"version: {np.__version__}")


'''
---------WARNING: PERMISSIONS REQUIRED - WorkAround (just install this, its ez)---------
needed to not only install pydub, but for permissions to get thru you also needed "pip install simpleaudio"
otherwise it will throw an error with "Permissions denied"


'''

'''

OS Stats: (Hopefully this doesnt matter)
Edition	Windows 11 Pro
Version	23H2
Installed on	11/27/2022
OS build	22631.5472
Experience	Windows Feature Experience Pack 1000.22700.1106.0

Python: Ver. 3.10.11 (from Microsoft Store - probably not relavent)

Here are the library versions of each included library: 

* pytchat: verson 0.5.5
* gtts: verson 2.5.1
* pydub: verion 0.25.1
* simpleaudio: version 1.0.4 (the permissions one that works in the background, but not directly imported)
* os (UNKNOWN - doesnt have a __version__)
* time: (UNKNOWN - doesnt have a __version__)
* threading: : (UNKNOWN - doesnt have a __version__)


'''


import pytchat
from gtts import gTTS
import os
import time
import threading
import queue

import os
from pydub import AudioSegment
from pydub.playback import play

#was hard vibing
script_path = os.path.realpath(__file__)
program_directory = os.path.dirname(script_path)

# for playing audio file
song = AudioSegment.from_mp3(program_directory + "\\chat_message.mp3")

# Queue for chat messages to speak
speak_queue = queue.Queue()

# Function to convert text to speech and play it
def text_to_speech_worker():
    while True:
        text = speak_queue.get()
        try:
            #get the text, convert it to TTS, save as a file
            tts = gTTS(text)
            filename = "chat_message.mp3"
            tts.save(filename)

            #Say the message here 
            song = AudioSegment.from_mp3(program_directory + "\\chat_message.mp3")
            print('TTS Says: "' + str(text) + '"')
            play(song) #Not sure if the code STOPS while this is playing or NOT
            
            
            #time.sleep(5)  # Let the message play before the next one
        except Exception as e:
            print(f"TTS Error: {e}")
        speak_queue.task_done()

# Start the background TTS thread
threading.Thread(target=text_to_speech_worker, daemon=True).start()

# YouTube video ID (not chat ID)
video_id = "WhkpIFxW7Tg"

# Start fetching chat
chat = pytchat.create(video_id=video_id)
print("Listening to YouTube live chat...")

while chat.is_alive():
    try:
        for c in chat.get().sync_items():
            message = c.message
            author = c.author.name
            print("LiveChat: ")
            print(f"[{author}] {message}")
            #speak_queue.put(f"{author} said: {message}")
            speak_queue.put(f"{message}")
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(1)
