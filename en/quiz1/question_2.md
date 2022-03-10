
--- question ---

---
legend: Question 2 of 3
---

This is the code for a four note piano:

--- code ---
---
language: python
line_numbers: false
---

from picozero import Speaker, Button

speaker = Speaker(5)
button1 = Button(18)
button2 = Button(19)
button3 = Button(20)
button4 = Button(21)

def play_c():
    speaker.play('c4', 1)
    
def play_d():
    speaker.play('d4', 1)
    
def play_e():
    speaker.play('e4', 1)
    
def play_f():
    speaker.play('f4', 1)

button1.when_pressed = play_c
button2.when_pressed = play_d
button3.when_pressed = play_e
button4.when_pressed = play_f

--- /code ---

Which note will play when the button connected to pin 20 is pressed?

--- choices ---

- ( ) 

  --- feedback ---

  --- /feedback ---

- ( ) 

  --- feedback ---

  --- /feedback ---

- ( ) 

  --- feedback ---

  --- /feedback ---

- ( ) 

  --- feedback ---

  --- /feedback ---

--- /choices ---

--- /question ---
