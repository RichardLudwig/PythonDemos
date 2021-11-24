# Imports
import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer() # Assign speech recognition function to r variable

def record_audio(ask=False): # Audio recording function
  with sr.Microphone() as source: 
    if ask: # If ask is true
      player_speak(ask) # run player_speak function
    audio = r.listen(source) # Assign audio input to audio variable
    voice_data = "" # Initialize voice_data with empty String
    try:
      voice_data = r.recognize_google(audio) # Recognize and assign audio to voice_data variable
    except sr.UnknownValueError: # Catch unknown value errors
      player_speak("Please try again.")
    except sr.RequestError: # Catch request errors
      player_speak("Service down.")
    return voice_data # Return value associated with voice_data

def player_speak(audio_string): # Output audio function
  tts = gTTS(text=audio_string, lang="en") # Transform audio to text, set language to English
  r = random.randint(1, 10000000) # Generate random integer between 1 and 1 million
  audio_file = "audio-" + str(r) + ".mp3" # Save audio as temp mp3 file
  tts.save(audio_file) # Save audio file in text to speech format
  playsound.playsound(audio_file) # Output audio file as speech
  print(audio_string) # Print audio file as text
  os.remove(audio_file) # Delete/remove audio file to reduce file clutter

print()
print("Options") # Program Options
print("1. Time")
print("2. Search")
print("3. Location")
print("4. Video Channel")
print("5. Information")
print("6. Lyrics")
print()

def respond(voice_data): # Output response function based on user speech
  if "time" in voice_data: # If "time" requested by user
    time = "The time is " + ctime() # Assign time to variable
    player_speak(time) # Output time audio
  if "search" in voice_data: # If "search" requested by user
    search = record_audio("State search parameters:") # Request search parameters from user
    url = "https://google.com/search?q=" + search # Assign search parameters to url
    webbrowser.get().open(url) # Open browser with search terms
    player_speak("Search results for " + search) # Output search audio
  if "location" in voice_data: # If "location" requested by user
    location = record_audio("State location parameters:") # Request search parameters
    url = "https://google.com/maps/place/" + location + "/&amp" # Assign search parameters to url
    webbrowser.get().open(url) # Open browser with search terms
    player_speak("Search results for " + location) # Output search audio
  if "video" in voice_data: # If "video" requested by user
    channel = record_audio("State channel name:") # Request search parameters
    url = "https://www.youtube.com/c/" + channel # Assign search parameters to url
    webbrowser.get().open(url) # Open browser with search terms
    player_speak("Youtube results for " + channel) # Output search audio
  if "information" in voice_data: # If "information" requested by user
    info = record_audio("State search parameters:") # Request search parameters
    url = "https://en.wikipedia.org/wiki/" + info # Assign search parameters to url
    webbrowser.get().open(url) # Open browser with search terms
    player_speak("Wikipedia results for " + info) # Output search audio
  if "lyrics" in voice_data: # If "lyrics" requested by user
    lyrics = record_audio("State search parameters:") # Request search parameters
    url = "https://www.lyrics.com/lyrics/" + lyrics # Assign search parameters to url
    webbrowser.get().open(url) # Open browser with search terms
    player_speak("Lyrics.com results for " + lyrics) # Output search audio
  if "weather" in voice_data: # If "weather" requested by user
    weather = record_audio("State search parameters:") # Request search parameters
    # Only uses single term search locations
    url = "https://www.weather-forecast.com/locations/" + weather # Assign search parameters to url
    webbrowser.get().open(url) # Open browser with search terms
    player_speak("Weather-Forecast.com results for " + weather) # Output search audio
  if "exit" in voice_data: # If "exit" requested by user
    player_speak("Exiting now...") # Output exit audio
    exit() # Exit program

time.sleep(1) # Program sleeps until user speaks

while 1: # Program sleeps until it hears a valid response
  voice_data = record_audio() # Start recording audio
  respond(voice_data) # Run respond function to output audio answer to user request