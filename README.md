# Speech-to-Text-Converter
## This is a Python console application where the user can record a short voice recording and receive a transcript of their recording.
### Description
This project was created for speech to text conversion. This has several potential uses, including securing a written record of verbal speech and increasing accessibility for the hard of of hearing. I created this project to strengthen my Python programming skills, including working with audio recording, playback and speech to text conversion in Python.
### Technologies
* Python
* Libraries used:
  * sounddevice
  * SpeechRecognition 3.9.0
  * wavio
  * soundfile
  * playsound
  * os
  * time
  * PyAudio
### Instructions
* To run this project, download the ZIP file and run the Python script in the console.
```
cd path    #path to local folder where the python script was dowloaded.
python3 speech-to-text.py
```
* Upon running the script, a prompt will be shown in the console, follow the prompt to begin recording.
* Once the recording is complete it will be played back automatically, after which you will have the option to record again, obtain a trancript of the recording, or exit the application.
* If you choose to obtain a trancript, your transcript will be displayed in the console.
* It is possible that the application may not be able to convert your recording to text, in which case you can run the script again.
### Credits
* For speech to text recognition, Google Speech Recognition used: https://pypi.org/project/SpeechRecognition/
