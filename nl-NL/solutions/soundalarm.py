from picozero import Speaker, RGBLED, Switch
from time import sleep
from random import randint

# Geef aan op welke pennen de onderdelen op de Pico zijn bevestigd
luidspreker = Speaker(5)
led = RGBLED(13, 14, 15)
signaal = Switch(18)

# Een reeks functies die vervelende tonen creëren

def tada(): # Ta-Daaa!
    led.color = (250,125,0)
    luidspreker.play(523, 0.1)
    led.color = (0,0,0)
    sleep(0.1)
    led.color = (250,125,0)
    luidspreker.play(523, 0.6)


def tjilpen(): # Reeks hoge pieptonen
    for _ in range(5):
        bc = 255
        rc = 0
        for i in range(5000, 2999, -100):
            led.color = (rc,0,bc)
            luidspreker.play(i, 0.02)
            bc -= 12
            rc += 12
        sleep(0.2)


def alarm(): # Stijgende tonen
    for _ in range(5):
        gc = 255
        bc = 0

        for i in range(2000, 5000, 100):
            led.color = (127,gc,bc)
            luidspreker.play(i, 0.05)
            gc -= 8
            bc += 8
        sleep(0.2)    


def sirene(): # Nee-Naw!
    for i in range(10):
        led.color = (0,0,255)
        luidspreker.play(4500, 0.5)
        led.color = (255,0,0)
        luidspreker.play(2500, 0.5)


def bom(): # 'Bom' laten vallen om te crashen
    bc = 240
    for i in range(5000, 1000, -50):
        led.color = (127,255,bc)
        luidspreker.play(i, 0.05)
        bc -= 3
    led.color = (255,0,0)
    for i in range(1000): # Witte ruis lus 1 seconde
        toon = randint(1000,5000) # Kies een willekeurig getal tussen 1k-5k
        luidspreker.play(tone, 0.001) # Speel een toon gedurende 1/1000e seconde
    sleep(0.2)


def verlies(): # wah-wah-wah-waaaaahhhh
    led.color = (255,255,255) # Wit
    luidspreker.play(494, 0.5)
    led.color = (125,125,125) # Dim
    luidspreker.play(466, 0.5)
    led.color = (60,60,60) # Dimmer
    luidspreker.play(440, 0.5)
    for i in range(10):
        luidspreker.play(415, 0.05)
        led.color = (0,0,0) # Uit
        luidspreker.play(440, 0.05)
        led.color = (255,255,255) # Wit 
    luidspreker.play(415, 0.2)    


def herrie():
    geluid = randint(1,6) # Kies een getal tussen 1 en 6
    if geluid == 1:
        tada()
    elif geluid == 2:
        tjilpen()
    elif geluid == 3:
        sirene()
    elif geluid == 4:
        alarm()
    elif geluid == 5:
        bom()
    elif geluid == 6:
        verlies()
        
def veilig(): # Geen geluid of licht
    luidspreker.off()
    led.off()

# Lus om te controleren of de schakelaar gesloten is

while True: 
    if signaal.is_closed:
        herrie()
    else:
        veilig()
