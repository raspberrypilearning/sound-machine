from picozero import Speaker, Pot, Button
from time import sleep

haut_parleur = Speaker(5)
haut_parleur2 = Speaker(13)
bouton = Button(18)
cadran = Pot(0)

RYTHME = 0.4

liten_mus = [ ['d5', RYTHME / 2], ['d#5', RYTHME / 2], ['f5', RYTHME], ['d6', RYTHME], ['a#5', RYTHME], ['d5', RYTHME],  
              ['f5', RYTHME], ['d#5', RYTHME], ['d#5', RYTHME], ['c5', RYTHME / 2],['d5', RYTHME / 2], ['d#5', RYTHME], 
              ['c6', RYTHME], ['a5', RYTHME], ['d5', RYTHME], ['g5', RYTHME], ['f5', RYTHME], ['f5', RYTHME], ['d5', RYTHME / 2],
              ['d#5', RYTHME / 2], ['f5', RYTHME], ['g5', RYTHME], ['a5', RYTHME], ['a#5', RYTHME], ['a5', RYTHME], ['g5', RYTHME],
              ['g5', RYTHME], ['', RYTHME / 2], ['a#5', RYTHME / 2], ['c6', RYTHME / 2], ['d6', RYTHME / 2], ['c6', RYTHME / 2],
              ['a#5', RYTHME / 2], ['a5', RYTHME / 2], ['g5', RYTHME / 2], ['a5', RYTHME / 2], ['a#5', RYTHME / 2], ['c6', RYTHME],
              ['f5', RYTHME], ['f5', RYTHME], ['f5', RYTHME / 2], ['d#5', RYTHME / 2], ['d5', RYTHME], ['f5', RYTHME], ['d6', RYTHME],
              ['d6', RYTHME / 2], ['c6', RYTHME / 2], ['b5', RYTHME], ['g5', RYTHME], ['g5', RYTHME], ['c6', RYTHME / 2],
              ['a#5', RYTHME / 2], ['a5', RYTHME], ['f5', RYTHME], ['d6', RYTHME], ['a5', RYTHME], ['a#5', RYTHME * 1.5] ]

def son_ennuyeux():
    haut_parleur.play(523, 0.1)
    sleep(0.1)
    haut_parleur.play(523, 0.4)

bouton.when_pressed = son_ennuyeux

try:
    for note in liten_mus:
        haut_parleur.play(note) 
        sleep(cadran.value) # Laisse un espace entre les notes en fonction de la valeur du potentiomètre
finally:
    haut_parleur.off() # Éteint le haut-parleur lorsque le code est arrêté par l'utilisateur
    haut_parleur2.off() # Éteint le haut-parleur2 lorsque le code est arrêté par l'utilisateur