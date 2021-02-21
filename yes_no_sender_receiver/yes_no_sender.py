from microbit import *
import radio
import speech
radio.on()
radio.config(group=9)
while True:
    if button_a.was_pressed:
        radio.send("YES")
    if button_b.was_pressed():
        radio.send("NO")