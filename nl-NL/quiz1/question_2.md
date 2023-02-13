
--- question ---

---
legend: Vraag 2 van 3
---

Dit is de code voor een piano met drie noten:

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

Welke noot wordt afgespeeld wanneer de knop die is aangesloten op pen GP20 wordt ingedrukt?

--- choices ---

- ( ) 'd4'

  --- feedback ---

  Dat klopt niet. Look carefully at which button is connected to GP20 and what happens when it is pressed.

  --- /feedback ---

- (x) 'e4'

  --- feedback ---

  Ja dat is goed. `knop3` gebruikt GP20 en `wanneer_ingedrukt` roept de `play_e` functie op die de `e4` noot afspeelt.

  --- /feedback ---

- () 'c4'

  --- feedback ---

Dat klopt niet. Look carefully at which button is connected to GP20 and what happens when it is pressed.

  --- /feedback ---

--- /choices ---

--- /question ---
