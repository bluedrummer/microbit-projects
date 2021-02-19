from microbit import *
import radio

radio.config(group=11)
radio.on()
count=0
while True:
    message = radio.receive()
    if message:
        display.scroll(str(message))
        count = int(message)
    if button_a.was_pressed()
        display.clear()
        count += 1
        radio.send(str(count))