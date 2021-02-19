from microbit import *
import radio

radio.config(group=10)
radio.on()

while True:
    message = radio.receive()
    if message:
        display.show(Image.DUCK)
    if button_a.was_pressed():
        display.clear()
        radio.send('duck')