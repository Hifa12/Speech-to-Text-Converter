import sounddevice as sd
import speech_recognition as sr
import wavio
import soundfile as sf
from playsound import playsound
import os
from time import sleep

#Define function for recording voice
def record_voice():
    key = input("Press enter to begin recording")
    if key == '':
        #Record voice into an array
        seconds = 15
        f = 44100
        print("Now recording")
        voice_recording = sd.rec(int(seconds * f), samplerate=f, channels=1)
        sleep(8)
        print("Recording will stop in...")
        sleep(2)
        for i in range(5, 0, -1):
            print(i)
            sleep(1)
        sd.wait()
        print("Stopped Recording.")
        #Save voice recording as .wav file
        wavio.write("voicerecording.wav", voice_recording, f, sampwidth=2)
        #Play voice recording
        print("Playing your recording...")
        playsound("voicerecording.wav")
    else:
        quit()

#Allow user to record themselves and give option to recieve transcript or re-record
while True:
    record_voice()
    key2 = input("Press enter to record yourself again, enter t to get a transcript of your recording, enter q to exit: ")
    if key2 == "t":
        break
    if key2 == "q":
        quit()
    os.remove("voicerecording.wav")

#Retrieve transcript of recording
print("Retrieving your transcript...")
#Listen to the .wav file containg voice recording
with sr.AudioFile("voicerecording.wav") as source:
    l_recording = sr.Recognizer().listen(source)
# Use Google recognizer for speech to text conversion
    try:
        transcript = sr.Recognizer().recognize_google(l_recording)
        print("Transcript:",transcript)
    except:#In case Google is unable to recognize
        print("Unable to retrieve transcript.")

#Delete voice recording
os.remove("voicerecording.wav")
