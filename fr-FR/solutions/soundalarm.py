from picozero import Speaker, RGBLED, Switch
from time import sleep
from random import randint

# Indique à quelles broches les composants sont reliés sur le Pico
haut_parleur = Speaker(5)
led = RGBLED(13, 14, 15)
declencher = Switch(18)

# Une série de fonctions qui créent des tonalités gênantes

def tada(): # Ta-Daaa!
    led.color = (250,125,0)
    haut_parleur.play(523, 0.1)
    led.color = (0,0,0)
    sleep(0.1)
    led.color = (250,125,0)
    haut_parleur.play(523, 0.6)


def gazouiller(): # Série de gazouillis aigus
    for _ in range(5):
        bc = 255
        rc = 0
        for i in range(5000, 2999, -100):
            led.color = (rc,0,bc)
            haut_parleur.play(i, 0.02)
            bc -= 12
            rc += 12
        sleep(0.2)


def alarme(): # Tonalités montantes
    for _ in range(5):
        gc = 255
        bc = 0

        for i in range(2000, 5000, 100):
            led.color = (127,gc,bc)
            haut_parleur.play(i, 0.05)
            gc -= 8
            bc += 8
        sleep(0.2)    


def sirene(): # Nee-Nor!
    for i in range(10):
        led.color = (0,0,255)
        haut_parleur.play(4500, 0.5)
        led.color = (255,0,0)
        haut_parleur.play(2500, 0.5)


def bombe(): # 'Bombe' décroissante pour planter
    bc = 240
    for i in range(5000, 1000, -50):
        led.color = (127,255,bc)
        haut_parleur.play(i, 0.05)
        bc -= 3
    led.color = (255,0,0)
    for i in range(1000): # Boucle de bruit blanc 1 seconde
         = randint(1000,5000) # Choisir un nombre au hasard
        haut_parleur.play(ton, 0.001) # Joue la tonalité pendant 1/1000e de seconde
    sleep(0.2)


def perdre(): # wah-wah-wah-waaaaahhhh
    led.color = (255,255,255) # Blanc
    haut_parleur.play(494, 0.5)
    led.color = (125,125,125) # Dim
    haut_parleur.play(466, 0.5)
    led.color = (60,60,60) # Variateur
    haut_parleur.play(440, 0.5)
    for i in range(10):
        haut_parleur.play(415, 0.05)
        led.color = (0,0,0) # off
        haut_parleur.play(440, 0.05)
        led.color = (255,255,255) # Blanc 
    haut_parleur.play(415, 0.2)    


def bruit():
    son = randint(1,6) # Choisit un nombre entre 1 et 6
    if son == 1:
        tada()
    elif son == 2:
        gazouiller()
    elif son == 3:
        sirene()
    elif son == 4:
        alarme()
    elif son == 5:
        bombe()
    elif son == 6:
        perdre()
        
def sur(): # Pas de son ni de lumière
    haut_parleur.off()
    led.off()

# Boucle pour vérifier si l'interrupteur est fermé

while True: 
    if declencher.is_closed:
        bruit()
    else:
        sur()
