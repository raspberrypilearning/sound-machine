## Wat ga je maken

Maak een klankbord dat geluidseffecten of muziek afspeelt met knoppen, schakelaars of een potentiometer.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">**Geluiden**</span> kunnen behulpzaam, kalmerend, vervelend en stimulerend zijn. Een pasgeboren baby vindt een witte ruis machine rustgevend en het geluid kan hen helpen bij het slapen. Dj's maken gebruik van draagbare klankborden om beats samen te stellen terwijl ze op reis zijn. Grapjassen gebruiken machines voor geluidseffecten om mensen te laten lachen. Kun je een klankbord bedenken dat je in je dagelijks leven hebt gebruikt? 
</p>

Je gaat:

+ Een apparaat ontwerpen dat geluid gebruikt voor een specifiek doel
+ Muziek of geluidseffecten programmeren om op een zoemer af te spelen
+ Een interface maken die een gebruiker helpt om geluiden te besturen

Om dit project te voltooien heb je het volgende nodig:

**Hardware:**

Je kunt alle benodigde hardware voor dit project en de andere projecten in dit pad kopen in de [Pimoroni webwinkel](https://shop.pimoroni.com/products/pico-intro-kit?variant=39893512945747){:target='_blank'} en de [Kitronik webwinkel.](https://kitronik.co.uk/products/5343-raspberry-pi-foundation-pico-pathway-pack){:target='_blank'}

+ Een Raspberry Pi Pico met gesoldeerde aansluitpinnen
+ Een data USB A naar micro USB-kabel
+ Een potentiometer of knoppen (gekocht of zelfgemaakt)
+ Een passieve toon-zoemer
+ Verbindingsdraden
+ Knutselmaterialenmaterialen zoals papier, karton, plakband en folie

**Software:**
+ Thonny – dit project kan worden voltooid met de Thonny Python editor, die kan worden geïnstalleerd op een Linux-, Windows- of Mac-computer.

[[[thonny-install]]]

[[[change-theme-thonny]]]

+ picozero - je moet picozero instellen op je Raspberry Pi Pico

[[[set-up-picozero]]]

Optioneel:

+ RGB-led(s) met gemeenschappelijke kathode of eenkleurige led(s) met weerstanden en verbindingsdraden
+ Een extra passieve toon-zoemer voor stereogeluid

--- no-print ---

--- task ---

### Ontdek ▶️

**Geluidseffectenbord**
Dit klankbord is gemaakt van karton met een aantal folieknoppen die geluidseffecten afspelen wanneer ze worden geactiveerd.

<video width="640" height="360" controls preload="none" poster="images/sound-board-placeholder.png">
<source src="images/sound_board.mp4" type="video/mp4">
Je browser ondersteunt geen WebM-video, probeer Firefox of Chrome
</video>

--- collapse ---
---
title: Zie binnenkant
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
    luidspreker.play(523, 0.4)
        
def tjilpen(): # Reeks hoge pieptonen
    for _ in range(2):
        for i in range(5000, 2999, -100):
            luidspreker.play(i, 0.02)
        sleep(0.2)
        
def win(): # Stijgende tonen
    for i in range(2000, 5000, 100):
        luidspreker.play(i, 0.05)        
    
def verlies(): # Wah-wah-wah-waaaaahhhh
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

--- /code ---

--- /collapse ---

--- /task ---

### Ideeën opdoen 💭

Je gaat een aantal ontwerpbeslissingen nemen om je klankbord te maken.

--- task ---

Bekijk deze voorbeeldprojecten om meer ideeën te krijgen voor het maken van je klankbord:

**Speel een deuntje voor mij (met behulp van een drop-schakelaar)** Er is een drop-schakelaar gemaakt met twee stukjes folie met folie die ook aan de onderkant van een poppetje is bevestigd. Wanneer het poppetje op de schakelaar wordt gezet, wordt de melodie geactiveerd.

<video width="640" height="360" controls preload="none" poster="images/wicked-placeholder.png">
<source src="images/wicked-player.mp4" type="video/mp4">
Je browser ondersteunt geen WebM-video, probeer Firefox of Chrome
</video>

--- collapse ---
---
title: Zie binnenkant
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

luidspreker = Speaker(5)
schakelaar = Switch(18)

beat = 0.5 # 120 slagen per minuut

trotseren = [ ['a5', beat / 2], ['a5', beat], ['e6', beat], ['d6', beat * 1.5], ['f#5', beat], ['a5', beat * 1.5],  
              ['d5', beat], ['f#5', beat * 1.5], ['e5', beat / 2], ['e5', beat * 1.5] ]

def speel_lied():
    try:
        luidspreker.play(trotseren)
           
    finally: # Schakel de luidspreker uit als deze wordt onderbroken
        luidspreker.off()

schakelaar.when_closed = speel_lied
--- /code ---

--- /collapse ---

**Geluidsbom (omgekeerde party popper-schakelaar + vervelende SFX-cyclus)**
Gebaseerd op het vorige Party popper-project: wanneer aan het stuk karton wordt getrokken, kan een veerbelaste schakelaar (een wasknijper met keukenfolie) sluiten en vervolgens speelt een eindeloze lus van irritante geluiden en bijbehorende gekleurde lampjes.

<video width="640" height="360" controls preload="none" poster="images/soundalarm-placeholder.png">
<source src="images/soundalarm.mp4" type="video/mp4">
Je browser ondersteunt geen WebM-video, probeer Firefox of Chrome
</video>

--- collapse ---
---
title: Zie binnenkant
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
    luidspreker.play(523, 0.4)
    for i in range(100, 0, -1):
        luidspreker.play(523, 0.01, i/100)


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


def bom(): # 'Alarm' laten vallen om te crashen
    bc = 240
    for i in range(5000, 1000, -50):
        led.color = (127,255,bc)
        luidspreker.play(i, 0.05)
        bc -= 3
    led.color = (255,0,0)
    for i in range(1000): # Witte ruis lus 1 seconde
        toon = randint(1000,5000) # Kies een willekeurig getal
        luidspreker.play(toon, 0.001) # Speel een toon gedurende 1/1000e seconde
    sleep(0.2)


def verlies(): # Wah-wah-wah-waaaaahhhh
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
        
def safe(): # Geen geluid of licht
    luidspreker.off()
    led.off()

# Lus om te controleren of de schakelaar gesloten is

while True: 
    if signaal.is_closed:
        herrie()
    else:
        safe()

--- /code ---


--- /collapse ---

**Muziekinstrument met twee zoemers – een met een witte ruis die wordt geregeld door een potentiometer**
Dit klankbord heeft een potentiometer die de snelheid van het geluid van de eerste zoemer regelt. Door op de knop te drukken, speel je een paar korte noten van de tweede zoemer af.

<video width="640" height="360" controls preload="none" poster="images/instrument-placeholder.png">
<source src="images/pot-speed.mp4" type="video/mp4">
Je browser ondersteunt geen WebM-video, probeer Firefox of Chrome
</video>

--- collapse ---
---
title: Zie binnenkant
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

luidspreker = Speaker(5)
luidspreker2 = Speaker(10)
knop = Button(18)
dial = Pot(0)

beat = 0.4

liten_mus = [ ['d5', beat / 2], ['d#5', beat / 2], ['f5', beat], ['d6', beat], ['a#5', beat], ['d5', beat],  
              ['f5', beat], ['d#5', beat], ['d#5', beat], ['c5', beat / 2],['d5', beat / 2], ['d#5', beat], 
              ['c6', beat], ['a5', beat], ['d5', beat], ['g5', beat], ['f5', beat], ['f5', beat], ['d5', beat / 2],
              ['d#5', beat / 2], ['f5', beat], ['g5', beat], ['a5', beat], ['a#5', beat], ['a5', beat], ['g5', beat],
              ['g5', beat], ['', beat / 2], ['a#5', beat / 2], ['c6', beat / 2], ['d6', beat / 2], ['c6', beat / 2],
              ['a#5', beat / 2], ['a5', beat / 2], ['g5', beat / 2], ['a5', beat / 2], ['a#5', beat / 2], ['c6', beat],
              ['f5', beat], ['f5', beat], ['f5', beat / 2], ['d#5', beat / 2], ['d5', beat], ['f5', beat], ['d6', beat],
              ['d6', beat / 2], ['c6', beat / 2], ['b5', beat], ['g5', beat], ['g5', beat], ['c6', beat / 2],
              ['a#5', beat / 2], ['a5', beat], ['f5', beat], ['d6', beat], ['a5', beat], ['a#5', beat * 1.5] ]

geluid = [ [523, 0.1], [None, 0.1], [523, 0.4] ]

def vervelend_geluid():
    luidspreker.play(geluid, wait=False)
    
knop.when_pressed = vervelend_geluid

try:
    for noot in liten_mus:
        luidspreker2.play(noot) 
        sleep(dial.value) # Laat een pauze tussen de noten, afhankelijk van de waarde van de potentiometer
finally:
    luidspreker.off() # Hiermee schakel je de luidspreker uit wanneer de code wordt gestopt door de gebruiker
    luidspreker2.off() # Schakelt luidspreker2 uit wanneer de code wordt gestopt door de gebruiker

--- /code ---


--- /collapse ---

--- /task ---

--- /no-print ---

--- print-only ---

### Ideeën opdoen 💭

Je gaat een aantal ontwerpbeslissingen nemen om je geluidskaart te maken. Hier zijn enkele voorbeelden van geluidsborden die je helpen met je ideeën:

**Geluidseffecten bord**
Dit geluidsbord is gemaakt van karton met een aantal folieknoppen die geluidseffecten afspelen wanneer je ze activeert.  
![](images/sound-board.png){:width="300px"}

**Speel me een melodie (met behulp van een stopknop)**
Er is een drop-switch gemaakt met twee stukjes folie met folie die ook aan de onderkant van een personage is bevestigd. Wanneer het teken op de schakelaar wordt gezet, wordt het deuntje geactiveerd. ![](images/wicked-player.jpeg){:width="300px"}

**Geluidsbom (omgekeerde feestpopper-schakelaar + vervelende SFX-cyclus)**
Op basis van het vorige Party popper-project laat het een veerbelaste schakelaar (een wasknijper met keukenfolie) sluiten en speelt een eindeloze lus van vervelende geluiden af. ![](images/sound-bomb.PNG){:width="300px"}

**Muziekinstrument met twee zoemers – een met een witte ruis die wordt geregeld door een potentiometer**
Dit klankbord heeft een potentiometer die de snelheid van het geluid van de eerste zoemer regelt. Door op de knop te drukken, speel je een paar korte noten van de tweede zoemer af. ![](images/pot-speed.png){:width="300px"}

--- /print-only ---

