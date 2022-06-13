
--- question ---

---
legend: Question 2 of 3
---

This is the code for a three note piano:

--- code ---
---
language: python
line_numbers: false
---
from picozero import Speaker, Button

speaker = Speaker(5) button1 = Button(18) button2 = Button(19) button3 = Button(20)

def play_c(): speaker.play('c4', 1)

def play_d(): speaker.play('d4', 1)

def play_e(): speaker.play('e4', 1)

button1.when_pressed = play_c button2.when_pressed = play_d button3.when_pressed = play_e

--- /code ---

Which note will play when the button connected to pin GP20 is pressed?

--- choices ---

- ( ) 'd4'

  --- feedback ---

  That's not it. Looks carefully at which button is connected to GP20 and what happens when it is pressed.

  --- /feedback ---

- (x) 'e4'

  --- feedback ---

  Yes, that's correct. `button3` uses GP20 and `when_pressed` it calls the `play_e` function which plays the `e4` note.

  --- /feedback ---

- ( ) 'c4'

  --- feedback ---

That's not it. Looks carefully at which button is connected to GP20 and what happens when it is pressed.

  --- /feedback ---

--- /choices ---

--- /question ---
