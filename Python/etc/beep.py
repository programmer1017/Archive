from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

from pygame import mixer  # Load the popular external library
import keyboard
print('Press q to play, w to exit.')

def main():
    mixer.init()
    mixer.music.load('e:\\NASA_tone.mp3')
    mixer.music.play()

while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            main() #then play a mp3 file
        if keyboard.is_pressed('w'):
            break
    except:
        main()
