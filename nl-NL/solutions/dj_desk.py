from picozero import Speaker, Pot, Button
from time import sleep

luidspreker = Speaker(5)
luidspreker2 = Speaker(13)
knop = Button(18)
instelwiel = Pot(0)

SLAG = 0.4

liten_mus = [ ['d5', SLAG / 2], ['d#5', SLAG / 2], ['f5', SLAG], ['d6', SLAG], ['a#5', SLAG], ['d5', SLAG],  
              ['f5', SLAG], ['d#5', SLAG], ['d#5', SLAG], ['c5', SLAG / 2],['d5', SLAG / 2], ['d#5', SLAG], 
              ['c6', SLAG], ['a5', SLAG], ['d5', SLAG], ['g5', SLAG], ['f5', SLAG], ['f5', SLAG], ['d5', SLAG / 2],
              ['d#5', SLAG / 2], ['f5', SLAG], ['g5', SLAG], ['a5', SLAG], ['a#5', SLAG], ['a5', SLAG], ['g5', SLAG],
              ['g5', SLAG], ['', SLAG / 2], ['a#5', SLAG / 2], ['c6', SLAG / 2], ['d6', SLAG / 2], ['c6', SLAG / 2],
              ['a#5', SLAG / 2], ['a5', SLAG / 2], ['g5', SLAG / 2], ['a5', SLAG / 2], ['a#5', SLAG / 2], ['c6', SLAG],
              ['f5', SLAG], ['f5', SLAG], ['f5', SLAG / 2], ['d#5', SLAG / 2], ['d5', SLAG], ['f5', SLAG], ['d6', SLAG],
              ['d6', SLAG / 2], ['c6', SLAG / 2], ['b5', SLAG], ['g5', SLAG], ['g5', SLAG], ['c6', SLAG / 2],
              ['a#5', SLAG / 2], ['a5', SLAG], ['f5', SLAG], ['d6', SLAG], ['a5', SLAG], ['a#5', SLAG * 1.5] ]

def vervelend_geluid():
    luidspreker.play(523, 0.1)
    sleep(0.1)
    luidspreker.play(523, 0.4)

knop.when_pressed = vervelend_geluid

try:
    for noot in liten_mus:
        luidspreker.play(noot) 
        sleep(instelwiel.value) # Laat een pauze tussen de noten, afhankelijk van de waarde van de potentiometer
finally:
    luidspreker.off() # Hiermee schakel je de luidspreker uit wanneer de code wordt gestopt door de gebruiker
    luidspreker2.off() # Schakelt luidspreker2 uit wanneer de code wordt gestopt door de gebruiker