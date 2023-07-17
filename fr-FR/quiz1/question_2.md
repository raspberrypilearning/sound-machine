
--- question ---

---
legend: Question 2 sur 3
---

Voici le code d'un piano à trois notes :

--- code ---
---
language: python
line_numbers: false
---
from picozero import Speaker, Button

haut_parleur = Speaker(5)
bouton1 = Button(18)
bouton2 = Button(19)
bouton3 = Button(20)

def joue_c():
    haut_parleur.play('c4', 1)
    
def joue_d():
    haut_parleur.play('d4', 1)
    
def joue_e():
    haut_parleur.play('e4', 1)
    
bouton1.when_pressed = joue_c
bouton2.when_pressed = joue_d
bouton3.when_pressed = joue_e

--- /code ---

Quelle note sera jouée lorsque le bouton connecté à la broche GP20 est enfoncé ?

--- choices ---

- ( ) 'd4'

  --- feedback ---

  Ce n'est pas ça. Regarde attentivement quel bouton est connecté à la broche GP20 et ce qui se passe lorsqu'il est enfoncé.

  --- /feedback ---

- (x) 'e4'

  --- feedback ---

  Oui, c'est correct. `bouton3` utilise GP20 et `when_pressed` appelle la fonction `joue_e` qui joue la note `e4`.

  --- /feedback ---

- ( ) 'c4'

  --- feedback ---

Ce n'est pas ça. Regarde attentivement quel bouton est connecté à la broche GP20 et ce qui se passe lorsqu'il est enfoncé.

  --- /feedback ---

--- /choices ---

--- /question ---
