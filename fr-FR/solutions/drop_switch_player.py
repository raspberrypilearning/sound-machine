from picozero import Speaker, Switch

haut_parleur = Speaker(5)
interrupteur = Switch(18)

RYTHME = 0.5 # 120 BPM

defiant = [ ['a5', RYTHME / 2], ['a5', RYTHME], ['e6', RYTHME], ['d6', RYTHME * 1.5], ['f#5', RYTHME], ['a5', RYTHME * 1.5],  
              ['d5', RYTHME], ['f#5', RYTHME * 1.5], ['e5', RYTHME / 2], ['e5', RYTHME * 1.5]]

def joue_morceau():
    try:
        haut_parleur.play(defiant)
           
    finally: # Éteindre le haut-parleur en cas d'interruption
        haut_parleur.off()

interrupteur.when_closed = joue_morceau