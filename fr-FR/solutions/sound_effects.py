from picozero import Speaker, Button
from time import sleep

# Indique à quelles broches les composants sont reliés sur le Pico
haut_parleur = Speaker(5)
bouton1 = Button(18)
bouton2 = Button(19)
bouton3 = Button(20)
bouton4 = Button(21)

# Une série de fonctions qui créent des tonalités gênantes
def tada(): # Ta-Daaa!
    haut_parleur.play(523, 0.1)
    sleep(0.1)
    haut_parleur.play(523, 0.8)
        
def gazouiller(): # Série de gazouillis aigus
    for _ in range(2):
        for i in range(5000, 2999, -100):
            haut_parleur.play(i, 0.02)
        sleep(0.2)
        
def gagner(): # Tonalités montantes
    for i in range(2000, 5000, 100):
        haut_parleur.play(i, 0.05)        
    
def perdre(): # wah-wah-wah-waaaaahhhh
    haut_parleur.play(494, 0.5)
    haut_parleur.play(466, 0.5)
    haut_parleur.play(440, 0.5)
    for i in range(10):
        haut_parleur.play(415, 0.05)
        haut_parleur.play(440, 0.05)
    haut_parleur.play(415, 0.2)
            
def stop(): # Pas de son ni de lumière
    
    led.off()
    
bouton1.when_pressed = tada
bouton2.when_pressed = gazouiller
bouton3.when_pressed = perdre
bouton4.when_pressed = gagner

try:
    while True:
        sleep(0.1)
finally:
    stop()