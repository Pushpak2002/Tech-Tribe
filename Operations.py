import pyttsx3
import openai
import pyaudio
import wave
import time
import pyttsx3  #python text to speech
import speech_recognition as sr
import speech_recognition as sr
from datetime import date
# This stack is to keep the track of the functions of the car
class StringStack:
    def __init__(self):
        self._items = []

    def push(self, item):
        print(item)
        if isinstance(item, str):  # Ensure item is a string for safety
            self._items.append(item)

    def pop(self):
        if not self.is_empty():
            return self._items.pop()
        else:
            raise IndexError("Stack is empty")
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        print( self._items[-1])

    def is_empty(self):
        return len(self._items) == 0

    def __str__(self):
        return f"StringStack: {self._items}"
#----------------------------------------------------------------------------

def speak(text):
    speaker = pyttsx3.init()
    speaker.setProperty('rate', 150)
    speaker.say(text)
    speaker.runAndWait()


def del_stack(stack, element):
    """Deletes the first occurrence of the specified element from the stack."""
    temp_stack = []
    while stack:
        popped = stack.pop()
        if popped != element:
            temp_stack.append(popped)
    while temp_stack:
        stack.append(temp_stack.pop())

# to search on pins
def search(self, element):
        for item in reversed(self.items):
            if item == element:
                return True
        return False

# Car Movement
def Movement(string,stack):
    print(stack)
    words1 = ["back","backward"]
    words2 = ["front","forward","up","upward"]
    if "right" in string: 
        print("turning right")
        speak("turning right")
        stack.push("turning right")
        #processors.insert(0,"turning right")
    elif "left" in string:
        print("turning left")
        speak("turning left")
        stack.push("turning left")
    elif any(word in string for word in words1):#for headlight
        print("moving backward")
        speak("moving backward")
        stack.push("going back")
    elif any(word in string for word in words2):#for headlight
        print("moving forward")
        speak("moving forward")
        stack.push("going forward")
        
# Car headligh
def light(string,stack):
    print(stack)
    if "on" in string:
        print("headlight is turned On")
        speak("headlight is turned On")
        stack.push("headlight is on")
    elif  "off" in string:
        print("headlight is turned Off")

# Car indicator
def indicator(string,stack):
    word1 = ["off","close"]
    word2 = ["right","left"]
    if not any(word in string for word in word2 ):

        if "on" in string:
            speak("which indicator do you want to turned on")
            str = input("which indicator do you want to turned on")
            string = string+str

    if any(word in string for word in word1 ):
        if "left" in string:
            print("left indicator Off")
            speak("left indicator Off")
            #stack.push("left indicator")
        elif "right" in string:
            print("right indicator Off")
            speak("right indicator Off")
            #stack.push("right indicator")
        print("Indicator is turned Off")
    elif  "on" in string:
        if "left" in string:
            print("turned on left indicator") #dont forgot to turn off right indicator
            speak("turned on left indicator")  
            stack.push("left indicator")
        elif "right" in string:
            print("turned on right indicator")#dont forgot to turn off left indicator
            speak("turned on right indicator")
            stack.push("right indicator")
                
# Car door
def door(string,stack):
    word1 = ["off","close"]
    word2 = ["right","left"]
    if not any(word in string for word in word2 ):
        if "open" in string:
            speak("which door do you want to turned on")
            str = input("which door do you want to turned on : ")
            string = string+str

    if any(word in string for word in word1 ):
        if "left" in string:
            print("left door Off")
            speak("left door Off")
            #stack.push("left door")
        elif "right" in string:
            print("right door Off")
            #stack.push("right door")
            print("door is turned Off")
            speak("door is turned Off")
    elif  "open" in string:
        if "left" in string:
            print("turned on left door")
            speak("turned on left door")
            stack.push("left door")
        elif "right" in string:
            print("turned on right door")
            speak("turned on right door")
            stack.push("right door")
    #else
        #here write a code to turn off indicator pin

# Car wiper
def wiper(string,stack):
    print(stack)
    if "on" in string:
        print("wiper is turned On")
        speak("wiper is turned on")
        stack.push("wiper is on")
        # print("stack is : ")
        # stack.peek()
    elif  "off" in string:
        print("wiper is turned Off")
        speak("wiper is turned Off")
        del_stack(stack,"wiper is on")


def check_word_in_string(string,stack):
    words = ["turn off", "turned off", "turn of", "turned of" , "of", "off"]
    words1 = ["move", "go", "come"]
    words2 = ["light","headlight"]
    matching_words = [word for word in words1 if word == string]
    if matching_words:
        #print(stack.pop()) #here we get the pin number then write a code to turn of this pin
        print("temp")
    else:
        if any(word in string for word in words1): #for car movement
            Movement(string,stack)
        elif any(word in string for word in words2):#for headlight
            light(string,stack)
        elif "indicator" in string:
            indicator(string,stack)
        elif "door" in string:
            door(string,stack)
        elif "wiper" in string:
            wiper(string,stack)
        


# Main
# speak("Hello I'm your assistant here to help u. Please give me command to proceed")
from time import sleep
r = sr.Recognizer()
mic = sr.Microphone()
while True:
    try:
        print("turn on....")
        with mic as source:
            audio = r.listen(source)
        words = r.recognize_google(audio)
        if "Jarvis" in words:
            speak("Hello sir, How can i help you")
            CHUNK = 1024  # Number of frames per audio chunk
            FORMAT = pyaudio.paInt16  # Audio format (16-bit integer)
            CHANNELS = 1  # Number of channels (mono)
            RATE = 44100  # Sampling rate (samples per second)
            RECORD_SECONDS = 5  # Duration of recording

            # Create an instance of PyAudio
            p = pyaudio.PyAudio()

            # Open a stream to record audio from the microphone
            stream = p.open(format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            input=True,
                            frames_per_buffer=CHUNK)

            print("* Recording audio...")

            frames = []

            # Record audio for the specified duration
            for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                data = stream.read(CHUNK)
                frames.append(data)

            print("* Finished recording")

            # Stop the stream and close it
            stream.stop_stream()
            stream.close()

            # Terminate the PyAudio instance
            p.terminate()

            # Save the recorded audio to a WAV file
            wf = wave.open("recorded.wav", "wb")
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
            wf.close()

            print("* Audio saved to recorded_audio.wav")

        #------------------------------------------------------------------
            openai.organization = "org-iVuvSLiObMLmVJOihyNu2vqq"

            openai.api_key= "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"

            audio_file = open(r"C:\\Users\\Pushpak\\Desktop\\Car\\recorded.wav","rb")
            transcript = openai.Audio.translate("whisper-1",audio_file)
            string = transcript['text']
            print(string)
            
            string = string.lower()
            stack = StringStack()
            check_word_in_string(string,stack)
            print("----------------------------------------")
            print("stack elements")
            print("----------------------------------------")
            print(stack)
            print("----------------------------------------")
            print("----------------------------------------")
            time.sleep(1)
        else:
            print("could not recognize")
    except:
        continue