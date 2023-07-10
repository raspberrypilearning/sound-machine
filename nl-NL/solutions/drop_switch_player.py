from picozero import Speaker, Switch

luidspreker = Speaker(5)
schakelaar = Switch(18)

SLAG = 0.5 # 120 slagen per minuut

trotseren = [ ['a5', SLAG / 2], ['a5', SLAG], ['e6', SLAG], ['d6', SLAG * 1.5], ['f#5', SLAG], ['a5', SLAG * 1.5],  
              ['d5', SLAG], ['f#5', SLAG * 1.5], ['e5', SLAG / 2], ['e5', SLAG * 1.5]]

def speel_lied():
    probeer:
        luidspreker.play(trotseren)
           
    finally: # Schakel de luidspreker uit als deze wordt onderbroken
        luidspreker.off()

schakelaar.when_closed = speel_lied