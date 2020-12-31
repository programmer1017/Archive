from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

from pygame import mixer  # Load the popular external library
import keyboard
print('Press q to play NASA quinadr tone, press a to play airplane seatbelt sound effect, press l to play airplane landing sound effect, and w to exit.')

def NASA():
    mixer.init()
    mixer.music.load('E:\\GithubRelease\\fastful\\Python\\etc\\NASA_tone.mp3')
    mixer.music.play()

def Airplane():
    mixer.init()
    mixer.music.load('E:\\GithubRelease\\fastful\Python\etc\\Airplane_dingdong_sound.mp3')
    mixer.music.play()

def airplane_landing():
    mixer.init()
    mixer.music.load('E:\\GithubRelease\\fastful\\python\\etc\\Airplane_landing.mp3')
    mixer.music.play()

while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            NASA() #then play a mp3 file
        if keyboard.is_pressed('w'):
            break
        if keyboard.is_pressed('a'):
            Airplane() #then play a mp3 file
        if keyboard.is_pressed('l'):
            airplane_landing()
    except:
        pass
