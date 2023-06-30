from picozero import Speaker, Button
from time import sleep

# Geef aan op welke pennen de onderdelen op de Pico zijn bevestigd
luidspreker = Speaker(5)
knop1 = Button(18)
knop2 = Button(19)
knop3 = Button(20)
knop4 = Button(21)

# Een reeks functies die vervelende tonen creëren
def tada(): # Ta-Daaa!
    luidspreker.play(523, 0.1)
    sleep(0.1)
    luidspreker.play(523, 0.8)
        
def tjilpen(): # Reeks hoge pieptonen
    for _ in range(2):
        for i in range(5000, 2999, -100):
            luidspreker.play(i, 0.02)
        sleep(0.2)
        
def win(): # Stijgende tonen
    for i in range(2000, 5000, 100):
        luidspreker.play(i, 0.05)        
    
def verlies(): # wah-wah-wah-waaaaahhhh
    luidspreker.play(494, 0.5)
    luidspreker.play(466, 0.5)
    luidspreker.play(440, 0.5)
    for i in range(10):
        luidspreker.play(415, 0.05)
        luidspreker.play(440, 0.05)
    luidspreker.play(415, 0.2)
            
def stop(): # Geen geluid of licht
    
    led.off()
    
knop1.when_pressed = tada
knop2.when_pressed = tjilpen
knop3.when_pressed = verlies
knop4.when_pressed = win

try:
    while True:
        sleep(0.1)
finally:
    stop()