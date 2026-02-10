# Morse Code Decoder 🔊

## What is Morse Code?

Morse code turns letters and numbers into a pattern of **dots** (short signals) and **dashes** (long signals).

For example:
- **S** = dot dot dot
- **O** = dash dash dash
- **SOS** = dot dot dot, dash dash dash, dot dot dot

It was invented in the 1830s for the telegraph — one of the first ways to send messages over long distances using electricity. It's still used today in emergency signaling and radio communication.

Here's the full alphabet:

| Letter | Code | Letter | Code |
|--------|------|--------|------|
| A | dot-dash | N | dash-dot |
| B | dash-dot-dot-dot | O | dash-dash-dash |
| C | dash-dot-dash-dot | P | dot-dash-dash-dot |
| D | dash-dot-dot | Q | dash-dash-dot-dash |
| E | dot | R | dot-dash-dot |
| F | dot-dot-dash-dot | S | dot-dot-dot |
| G | dash-dash-dot | T | dash |
| H | dot-dot-dot-dot | U | dot-dot-dash |
| I | dot-dot | V | dot-dot-dot-dash |
| J | dot-dash-dash-dash | W | dot-dash-dash |
| K | dash-dot-dash | X | dash-dot-dot-dash |
| L | dot-dash-dot-dot | Y | dash-dot-dash-dash |
| M | dash-dash | Z | dash-dash-dot-dot |

## How the Program Works

- **Button A** → record a dot
- **Button B** → record a dash
- **Touch the logo** → decode the current letter
- **Shake** → scroll the full message

You type one letter at a time. Press the buttons to enter dots and dashes, then touch the logo to decode it. The program builds up a string like `'dot-dash-dot'` and looks it up in the dictionary to find the letter.

## Your Tasks

Start with the starter code in `main.py`. Complete the tasks in order — each one builds on the last.

---

### Task 1: Record Dots and Dashes

Make Button A and Button B build up `current_symbol`.

- If `current_symbol` is empty, set it to `'dot'` or `'dash'`
- If it already has something, add `'-dot'` or `'-dash'` to the end

**Example:** pressing A, B, A should give `'dot-dash-dot'`

**Test it:** press some buttons, then touch the logo. Check the serial console — it should print your symbol string.

---

### Task 2: Decode the Symbol

When the logo is touched and `current_symbol` is not empty:

1. Look up `current_symbol` in `morse_dict`
2. If it's found, that's your letter. If not, use `'?'`
3. Add the letter to the `message` list
4. Reset `current_symbol` back to `''`

**Test it:** enter dot-dot-dot (S), touch the logo, then check the serial console.

<details>
<summary>Q: What happens if you hold the symbol instead of just pressing it?</summary>

**Answer**: You might notice that it's added a bunch of question marks to your message!

This is because the `while` loop immediate runs again and tries to add the now empty `current_symbol` to the message.

You might notice this even happens when you mean to tap the symbol quickly but are not quick enough!

Consider adding a short `sleep()` to let the user take their finger off the symbol without adding question marks to their message. 
</details>

---

### Task 3: Add Display and Sound

Go back and add feedback to each interaction:

**Button A (dot):**
```python
display.show(Image('00000:'
                   '00000:'
                   '36963:'
                   '00000:'
                   '00000'))
music.pitch(200)
sleep(100)
music.stop()
```

**Button B (dash):**
```python
display.show(Image('00300:'
                   '03630:'
                   '36963:'
                   '03630:'
                   '00300'))
music.pitch(300)
sleep(300)
music.stop()
```

**Logo touched (after decoding):**
```python
display.show(letter)
music.pitch(500)
sleep(100)
music.stop()
```

---

### Task 4: Shake to Show Message

When the micro:bit is shaken, scroll the full decoded message across the display.

**Hints:**
- `accelerometer.was_gesture('shake')`
- `''.join(message)` turns a list like `['S', 'O', 'S']` into `'SOS'`
- This should go at the top of the loop, before the other checks

---

## Challenge

Try sending a message to a friend! Have them decode it by hand using the table above, then check it against your micro:bit's decoded message.
