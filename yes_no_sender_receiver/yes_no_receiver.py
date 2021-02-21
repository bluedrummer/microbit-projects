from microbit import *
import radio
import speech
radio.on()
radio.config(group=9)
while True:
    message = radio.receive()
    if message:
        if message == "YES":
            speech.say("yes")
            display.clear()
        if message == "NO":
            speech.say("no")
            display.clear()

























































































































