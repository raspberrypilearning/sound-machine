
--- question ---

---
legend : Question 2 sur 3
---

Voici le code d'un piano à trois notes :

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

Quelle note sera jouée lorsque le bouton connecté à la broche GP20 est enfoncé ?

--- choices ---

- ( ) 'd4'

  --- feedback ---

  Ce n'est pas ça. Look carefully at which button is connected to GP20 and what happens when it is pressed.

  --- /feedback ---

- (x) 'e4'

  --- feedback ---

  Oui, c'est correct. `button3` utilise GP20 et `when_pressed` appelle la fonction `play_e` qui joue la note `e4`.

  --- /feedback ---

- ( ) 'c4'

  --- feedback ---

Ce n'est pas ça. Look carefully at which button is connected to GP20 and what happens when it is pressed.

  --- /feedback ---

--- /choices ---

--- /question ---
