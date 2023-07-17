## Ce que tu vas faire

Créer une machine à sons qui jouera des effets sonores ou de la musique à l'aide de boutons, d'interrupteurs ou d'un potentiomètre.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">**Les sons**</span> peuvent être utiles, apaisants, ennuyeux et énergisants. Un nouveau-né peut trouver une machine à bruit blanc apaisante et le son peut l'aider à dormir. Les DJ utilisent des machines à sons portables pour composer des rythmes lors de leurs déplacements. Les farceurs utilisent des machines à effets sonores pour faire rire les gens. Peux-tu penser à une machine à sons que tu as utilisée dans ta vie de tous les jours ? 
</p>

Tu vas devoir :

+ Concevoir un appareil qui utilise le son dans un but précis
+ Programmer de la musique ou des effets sonores à jouer sur un buzzer
+ Créer une interface qui permet à un utilisateur de contrôler les sons

Pour mener à bien ce projet, tu auras besoin de :

**Matériel :**

Tu peux acheter tout le matériel requis pour ce projet et les autres projets de ce parcours à partir de la boutique en ligne [Pimoroni.](https://shop.pimoroni.com/products/pico-intro-kit?variant=39893512945747){:target='_blank'} et la boutique en ligne [Kitronik.](https://kitronik.co.uk/products/5343-raspberry-pi-foundation-pico-pathway-pack){:target='_blank'}

+ Un Raspberry Pi Pico avec des broches soudées dessus
+ Un câble de données USB A vers micro USB
+ Un potentiomètre ou des boutons (achetés ou fabriqués)
+ Un buzzer à ton passif
+ Fils de connexion
+ Matériaux d'artisanat, y compris carte, ruban adhésif et papier d'aluminium

**Logiciel :**
+ Thonny – ce projet peut être réalisé à l'aide de l'éditeur Python Thonny, qui peut être installé sur un ordinateur Linux, Windows ou Mac.

[[[thonny-install]]]

[[[change-theme-thonny]]]

+ picozero - tu devras configurer la librairie picozero sur ton Raspberry Pi Pico

[[[set-up-picozero]]]

Facultatif :

+ LED(s) RVB à cathode commune ou LED(s) unicolore(s) avec résistances et fils de liaison
+ Un buzzer passif supplémentaire pour un son stéréo

--- no-print ---

--- task ---

### Découvrir ▶️

**Carte d'effets sonores** Cette carte à sons a été fabriquée en carton avec un certain nombre de boutons en aluminium qui produisent des effets sonores lorsqu'ils sont activés.

<video width="640" height="360" controls preload="none" poster="images/sound-board-placeholder.png">
<source src="images/sound_board.mp4" type="video/mp4">
Ton navigateur ne prend pas en charge la vidéo WebM, essaye FireFox ou Chrome
</video>

--- collapse ---
---
title: Voir en détails
---
--- code ---
---
language: python
filename: sound_board.py
line_numbers: true
line_number_start: 
line_highlights: 
---

from picozero import Speaker, Button
from time import sleep
from random import randint

# Indique à quelles broches les composants sont reliés sur le Pico
haut_parleur = Speaker(5)
bouton1 = Button(18)
bouton2 = Button(19)
bouton3 = Button(20)
bbouton4 = Button(21)

# Une série de fonctions qui créent des tonalités gênantes
def tada(): # Ta-Daaa!
    haut_parleur.play(523, 0.1)
    sleep(0.1)
    haut_parleur.play(523, 0.4)
        
def gazouiller(): # Série de gazouillis aigus
    for _ in range(2):
        for i in range(5000, 2999, -100):
            haut_parleur.play(i, 0.02)
        sleep(0.2)
        
def gagner(): # Tonalités montantes
    for i in range(2000, 5000, 100):
        haut_parleur.play(i, 0.05)        
    
def perdre(): # Wah-wah-wah-waaaaahhhh
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
bouton3.when_pressed = gagner
bouton4.when_pressed = perdre

try:
    while True:
        sleep(0.1)
finally:
    stop()

--- /code ---

--- /collapse ---

--- /task ---

### Trouver des idées 💭

Tu vas prendre des décisions de conception pour créer ta carte à sons.

--- task ---

Explore ces exemples de projets pour obtenir plus d'idées pour créer ta machine à sons :

**Joue-moi une mélodie (à l'aide d'un interrupteur à contact)** Un interrupteur à contact a été fabriqué à l'aide de deux morceaux de papier d'aluminium avec du papier d'aluminium également attaché au bas d'un personnage. Lorsque le personnage est déposé sur l'interrupteur, la mélodie s'active.

<video width="640" height="360" controls preload="none" poster="images/wicked-placeholder.png">
<source src="images/wicked-player.mp4" type="video/mp4">
Ton navigateur ne prend pas en charge la vidéo WebM, essaye FireFox ou Chrome
</video>

--- collapse ---
---
title: Voir en détails
---
--- code ---
---
language: python
filename: drop_switch_player.py
line_numbers: true
line_number_start: 1
line_highlights: 
---
from picozero import Speaker, Switch

haut_parleur = Speaker(5)
interrupteur = Switch(18)

RYTHME = 0.5 # 120 BPM

defiant = [ ['a5', RYTHME / 2], ['a5', RYTHME], ['e6', RYTHME], ['d6', RYTHME * 1.5], ['f#5', RYTHME], ['a5', RYTHME * 1.5],  
              ['d5', RYTHME], ['f#5', RYTHME * 1.5], ['e5', RYTHME / 2], ['e5', RYTHME * 1.5] ]

def joue_morceau():
    try:
        haut_parleur.play(defiant)
           
    finally: # Éteindre le haut-parleur en cas d'interruption
        haut_parleur.off()

interrupteur.when_closed = joue_morceau
--- /code ---

--- /collapse ---

**Alarme sonore (interrupteur party popper inversé + cycle SFX gênant)** Basé sur le projet Party popper précédent : lorsque le morceau de carton est tiré, il permet à un interrupteur à ressort (une pince à linge avec du papier d'aluminium) de se fermer puis joue une boucle sans fin de sons gênants et de lumières colorées qui les accompagnent.

<video width="640" height="360" controls preload="none" poster="images/soundalarm-placeholder.png">
<source src="images/soundalarm.mp4" type="video/mp4">
Ton navigateur ne prend pas en charge la vidéo WebM, essaye FireFox ou Chrome
</video>

--- collapse ---
---
title: Voir en détails
---
--- code ---
---
language: python
filename: soundalarm.py
line_numbers: true
line_number_start: 
line_highlights: 
---

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
    haut_parleur.play(523, 0.4)
    for i in range(100, 0, -1):
        haut_parleur.play(523, 0.01, i/100)


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


def bombe(): # 'Alarme' décroissante pour planter
    bc = 240
    for i in range(5000, 1000, -50):
        led.color = (127,255,bc)
        haut_parleur.play(i, 0.05)
        bc -= 3
    led.color = (255,0,0)
    for i in range(1000): # Boucle de bruit blanc 1 seconde
        ton = randint(1000,5000) # Choisir un nombre au hasard
        haut_parleur.play(tone, 0.001) # Joue la tonalité pendant 1/1000e de seconde
    sleep(0.2)


def perdre(): # Wah-wah-wah-waaaaahhhh
    led.color = (255,255,255) # Blanc
    haut_parleur.play(494, 0.5)
    led.color = (125,125,125) # Dim
    haut_parleur.play(466, 0.5)
    led.color = (60,60,60) # Variateur
    haut_parleur.play(440, 0.5)
    for i in range(10):
        haut_parleur.play(415, 0.05)
        led.color = (0,0,0) # Off
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

--- /code ---


--- /collapse ---

**Instrument de musique avec deux buzzers – un avec un battement de bruit blanc contrôlé par un potentiomètre** Cette machine à sons possède un potentiomètre qui contrôle la vitesse de la mélodie jouée à partir du premier buzzer. Appuyer sur le bouton joue quelques notes courtes sur le deuxième buzzer.

<video width="640" height="360" controls preload="none" poster="images/instrument-placeholder.png">
<source src="images/pot-speed.mp4" type="video/mp4">
Ton navigateur ne prend pas en charge la vidéo WebM, essaye FireFox ou Chrome
</video>

--- collapse ---
---
title: Voir en détails
---
--- code ---
---
language: python
filename: dj_desk.py
line_numbers: true
line_number_start: 
line_highlights: 
---

from picozero import Speaker, Pot, Button
from time import sleep

haut_parleur = Speaker(5)
haut_parleur2 = Speaker(10)
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

son = [ [523, 0.1], [None, 0.1], [523, 0.4] ]

def son_ennuyeux():
    haut_parleur.play(son, wait=False)
    
bouton.when_pressed = son_ennuyeux

try:
    for note in liten_mus:
        haut_parleur2.play(note) 
        sleep(cadran.value) # Laisse un espace entre les notes en fonction de la valeur du potentiomètre
finally:
    haut_parleur.off() # Éteint le haut-parleur lorsque le code est arrêté par l'utilisateur
    haut_parleur2.off() # Éteint le haut-parleur2 lorsque le code est arrêté par l'utilisateur

--- /code ---


--- /collapse ---

--- /task ---

--- /no-print ---

--- print-only ---

### Trouve des idées 💭

Tu vas prendre des décisions de conception pour créer ta carte son. Voici quelques exemples de cartes à sons pour t'aider dans tes idées :

**Carte d'effets sonores** Cette carte à sons a été fabriquée en carton avec un certain nombre de boutons en aluminium qui produisent des effets sonores lorsqu'ils sont activés.  
![](images/sound-board.png){:width="300px"}

**Joue-moi une mélodie (à l'aide d'un interrupteur à contact)** Un interrupteur à contact a été fabriqué à l'aide de deux morceaux de papier d'aluminium avec du papier d'aluminium également attaché au bas d'un personnage. Lorsque le personnage est déposé sur l'interrupteur, la mélodie s'active. ![](images/wicked-player.jpeg){:width="300px"}

**Bombe sonore (interrupteur Party Popper inversé + cycle SFX gênant)** Basé sur le projet Party Popper précédent, lorsque le morceau de carton est tiré, il permet à un interrupteur à ressort (une pince à linge avec du papier d'aluminium) de se fermer et de jouer une boucle sans fin de sons gênants. ![](images/sound-bomb.PNG){:width="300px"}

**Instrument de musique avec deux buzzers – un avec un battement de bruit blanc contrôlé par un potentiomètre** Cette machine à sons possède un potentiomètre qui contrôle la vitesse de la mélodie jouée à partir du premier buzzer. Appuyer sur le bouton joue quelques notes courtes à partir du deuxième buzzer. ![](images/pot-speed.png){:width="300px"}

--- /print-only ---

