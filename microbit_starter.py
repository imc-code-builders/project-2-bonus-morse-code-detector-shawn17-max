from microbit import *
import music

# Morse code dictionary
morse_dict = {
    'dot-dash': 'A', 'dash-dot-dot-dot': 'B', 'dash-dot-dash-dot': 'C',
    'dash-dot-dot': 'D', 'dot': 'E', 'dot-dot-dash-dot': 'F',
    'dash-dash-dot': 'G', 'dot-dot-dot-dot': 'H', 'dot-dot': 'I',
    'dot-dash-dash-dash': 'J', 'dash-dot-dash': 'K', 'dot-dash-dot-dot': 'L',
    'dash-dash': 'M', 'dash-dot': 'N', 'dash-dash-dash': 'O',
    'dot-dash-dash-dot': 'P', 'dash-dash-dot-dash': 'Q', 'dot-dash-dot': 'R',
    'dot-dot-dot': 'S', 'dash': 'T', 'dot-dot-dash': 'U',
    'dot-dot-dot-dash': 'V', 'dot-dash-dash': 'W', 'dash-dot-dot-dash': 'X',
    'dash-dot-dash-dash': 'Y', 'dash-dash-dot-dot': 'Z',
    'dot-dash-dash-dash-dash': '1', 'dot-dot-dash-dash-dash': '2',
    'dot-dot-dot-dash-dash': '3', 'dot-dot-dot-dot-dash': '4',
    'dot-dot-dot-dot-dot': '5', 'dash-dot-dot-dot-dot': '6',
    'dash-dash-dot-dot-dot': '7', 'dash-dash-dash-dot-dot': '8',
    'dash-dash-dash-dash-dot': '9', 'dash-dash-dash-dash-dash': '0'
}

current_symbol = ''
message = []

while True:
    # Clear screen to make it responsive
    display.clear()

    # TASK 4: Shake to scroll the full message
    if accelerometer.was_gesture('shake'):
        if message:
            display.scroll("".join(message))
        else:
            display.show("?")
        message = [] # Clear message after scrolling
        current_symbol = ''

    # TASK 2: Decode current_symbol when logo is touched
    elif pin_logo.is_touched():
        if current_symbol in morse_dict:
            letter = morse_dict[current_symbol]
            message.append(letter)
            display.show(letter)
            music.pitch(880, 100) # Higher tone for decoded letter
            sleep(500)
        else:
            display.show(Image.NO) # Show X if invalid
            sleep(500)
        current_symbol = '' # Reset symbol after decoding

    # TASK 1: Record dots and dashes (Button A = dot, Button B = dash)
    # TASK 3: Add display and sound
    elif button_a.was_pressed():
        if current_symbol == '':
            current_symbol = 'dot'
        else:
            current_symbol += '-dot'
        display.show('.')
        music.pitch(440, 100) # Dit sound
        sleep(200)

    elif button_b.was_pressed():
        if current_symbol == '':
            current_symbol = 'dash'
        else:
            current_symbol += '-dash'
        display.show('-')
        music.pitch(440, 300) # Dah sound
        sleep(200)
