from microbit import *

def turn_on(position):
    if position == 1:
        return "90000:00000:00000:00000:00000"
    elif position == 2:
        return "09000:00000:00000:00000:00000"
    elif position == 3:
        return "00900:00000:00000:00000:00000"
    elif position == 4:
        return "00090:00000:00000:00000:00000"
    elif position == 5:
        return "00009:00000:00000:00000:00000"
    elif position == 6:
        return "00000:90000:00000:00000:00000"
    elif position == 7:
        return "00000:09000:00000:00000:00000"
    elif position == 8:
        return "00000:00900:00000:00000:00000"
    elif position == 9:
        return "00000:00090:00000:00000:00000"
    elif position == 10:
        return "00000:00009:00000:00000:00000"
    elif position == 11:
        return "00000:00000:90000:00000:00000"
    elif position == 12:
        return "00000:00000:09000:00000:00000"
    elif position == 13:
        return "00000:00000:00900:00000:00000"
    elif position == 14:
        return "00000:00000:00090:00000:00000"
    elif position == 15:
        return "00000:00000:00009:00000:00000"
    elif position == 16:
        return "00000:00000:00000:90000:00000"
    elif position == 17:
        return "00000:00000:00000:09000:00000"
    elif position == 18:
        return "00000:00000:00000:00900:00000"
    elif position == 19:
        return "00000:00000:00000:00090:00000"
    elif position == 20:
        return "00000:00000:00000:00009:00000"
    elif position == 21:
        return "00000:00000:00000:00000:90000"
    elif position == 22:
        return "00000:00000:00000:00000:09000"
    elif position == 23:
        return "00000:00000:00000:00000:00900"
    elif position == 24:
        return "00000:00000:00000:00000:00090"
    elif position == 25:
        return "00000:00000:00000:00000:00009"
current_position = 13
display.show(Image(turn_on(current_position)))
while True:
    if button_a.was_pressed():
        if current_position != 1:
            current_position -= 1
            display.show(Image(turn_on(current_position)))
    if button_b.was_pressed():
        if current_position != 25:
            current_position += 1
            display.show(Image(turn_on(current_position)))


