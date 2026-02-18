from microbit import *
import music

# Corrected Morse code dictionary using . and - instead of 'dot' and 'dash'
morse_dict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    '-----': '0'
}

current_symbol = ''
message = []

while True:
    # Clear screen briefly to make input responsive
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
            current_symbol = '.'
        else:
            current_symbol += '.'
        display.show('.')
        music.pitch(440, 100) # Dit sound
        sleep(200)
        
    elif button_b.was_pressed():
        if current_symbol == '':
            current_symbol = '-'
        else:
            current_symbol += '-'
        display.show('-')
        music.pitch(440, 300) # Dah sound
        sleep(200)
