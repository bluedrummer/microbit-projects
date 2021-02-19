from microbit import *
from random import randint
import music
while True:
    if accelerometer.was_gesture('shake'):
        if randint(0,1)==1:
            display.show(Image.YES)
            music.play(["F4"])
            display.scroll('Mr Bean has chosen you!')

        else:
            display.show(Image.NO)
            music.play(["G3"])
            display.scroll('Mr Bean has left you with the sharks')

    if button_a.was_pressed():
        display.clear()
