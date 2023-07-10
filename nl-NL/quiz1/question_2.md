
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

luidspreker = Speaker(5)
knop1 = Button(18)
knop2 = Button(19)
knop3 = Button(20)

def play_c():
    luidspreker.play('c4', 1)
    
def play_d():
    luidspreker.play('d4', 1)
    
def play_e():
    luidspreker.play('e4', 1)
    
knop1.when_pressed = play_c
knop2.when_pressed = play_d
knop3.when_pressed = play_e

--- /code ---

Welke noot wordt afgespeeld wanneer de knop die is aangesloten op pen GP20 wordt ingedrukt?

--- choices ---

- ( ) 'd4'

  --- feedback ---

  Dat klopt niet. Kijk goed welke knop is aangesloten op de GP20 en wat er gebeurt wanneer deze wordt ingedrukt.

  --- /feedback ---

- (x) 'e4'

  --- feedback ---

  Ja dat is goed. `knop3` gebruikt GP20 en `wanneer_ingedrukt` roept de `play_e` functie op die de `e4` noot afspeelt.

  --- /feedback ---

- () 'c4'

  --- feedback ---

Dat klopt niet. Kijk goed welke knop is aangesloten op de GP20 en wat er gebeurt wanneer deze wordt ingedrukt.

  --- /feedback ---

--- /choices ---

--- /question ---
