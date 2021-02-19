from microbit import *
import radio

radio.config(group=12)
radio.on()

while True:
    message = radio.receive()
    if message:
        if message.split(":")[0] == "DISPLAY_TEMP":
            display.scroll(message.split(":")[1])
        elif message == "SEND_TEMP":
            radio.send("DISPLAY_TEMP:" + str(temperature()))
    if button_a.was_pressed():
        radio.send("DISPLAY_TEMP:" + str(temperature()))
    if button_b.is_pressed():
        radio.send("SEND_TEMP")