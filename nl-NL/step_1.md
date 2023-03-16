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

You can purchase all the required hardware for this project and the other projects in this path from the [Pimoroni web store.](https://shop.pimoroni.com/products/pico-intro-kit?variant=39893512945747){:target='_blank'} and the [Kitronik web store.](https://kitronik.co.uk/products/5343-raspberry-pi-foundation-pico-pathway-pack){:target='_blank'}

+ Een Raspberry Pi Pico met daarop gesoldeerde pinkoppen
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

**geluidseffectenbord** Dit klankbord is gemaakt van karton met een aantal folieknoppen die geluidseffecten afspelen wanneer ze worden geactiveerd.

<video width="640" height="360" controls preload="none" poster="images/sound-board-placeholder.png">
<source src="images/sound_board.mp4" type="video/mp4">
Je browser ondersteunt geen WebM-video, probeer Firefox of Chrome
</video>

--- collapse ---
---
Title: Zie binnenkant
---
--- code ---
---
language: python filename: sound_board.py line_numbers: true line_number_start:
line_highlights:
---

from picozero import Speaker, Button from time import sleep from random import randint

# Geef aan op welke pennen de onderdelen op de Pico zijn bevestigd
speaker = Speaker(5) button1 = Button(18) button2 = Button(19) button3 = Button(20) button4 = Button(21)

# Een reeks functies die vervelende tonen creëren
def tada(): # Ta-Daaa! speaker.play(523, 0.1) sleep(0.1) speaker.play(523, 0.4)

def chirp(): # Series of high-pitched chirps for _ in range(2): for i in range(5000, 2999, -100): speaker.play(i, 0.02) sleep(0.2)

def win(): # Rising tones for i in range(2000, 5000, 100): speaker.play(i, 0.05)

def womp(): # Wah-wah-wah-waaaaahhhh speaker.play(494, 0.5) speaker.play(466, 0.5) speaker.play(440, 0.5) for i in range(10): speaker.play(415, 0.05) speaker.play(440, 0.05) speaker.play(415, 0.2)

def stop(): # No sound or light

    led.off()

button1.when_pressed = tada button2.when_pressed = chirp button3.when_pressed = womp button4.when_pressed = win

try: while True: sleep(0.1) finally: stop()

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
Title: Zie binnenkant
---
--- code ---
---
language: python filename: drop_switch_player.py line_numbers: true line_number_start: 1
line_highlights:
---
from picozero import Speaker, Switch

speaker = Speaker(5) switch = Switch(18)

BEAT = 0.5 # 120 BPM

defying = [ ['a5', BEAT / 2], ['a5', BEAT], ['e6', BEAT], ['d6', BEAT * 1.5], ['f#5', BEAT], ['a5', BEAT * 1.5],  
['d5', BEAT], ['f#5', BEAT * 1.5], ['e5', BEAT / 2], ['e5', BEAT * 1.5] ]

def play_song(): try: speaker.play(defying)

    finally: # Turn speaker off if interrupted
        speaker.off()

switch.when_closed = play_song --- /code ---

--- /collapse ---

**Geluidsbom (omgekeerde party popper-schakelaar + vervelende SFX-cyclus)** Gebaseerd op het vorige Party popper-project: wanneer aan het stuk karton wordt getrokken, kan een veerbelaste schakelaar (een wasknijper met keukenfolie) sluiten en vervolgens speelt een eindeloze lus van irritante geluiden en bijbehorende gekleurde lampjes.

<video width="640" height="360" controls preload="none" poster="images/soundalarm-placeholder.png">
<source src="images/soundalarm.mp4" type="video/mp4">
Je browser ondersteunt geen WebM-video, probeer Firefox of Chrome
</video>

--- collapse ---
---
Title: Zie binnenkant
---
--- code ---
---
language: python filename: soundalarm.py line_numbers: true line_number_start:
line_highlights:
---

from picozero import Speaker, RGBLED, Switch from time import sleep from random import randint

# Geef aan op welke pennen de onderdelen op de Pico zijn bevestigd
speaker = Speaker(5) led = RGBLED(13, 14, 15) trigger = Switch(18)

# Een reeks functies die vervelende tonen creëren

def tada(): # Ta-Daaa! led.color = (250,125,0) speaker.play(523, 0.1) led.color = (0,0,0) sleep(0.1) led.color = (250,125,0) speaker.play(523, 0.4) for i in range(100, 0, -1): speaker.play(523, 0.01, i/100)


def chirp(): # Series of high-pitched chirps for _ in range(5): bc = 255 rc = 0 for i in range(5000, 2999, -100): led.color = (rc,0,bc) speaker.play(i, 0.02) bc -= 12 rc += 12 sleep(0.2)


def alarm(): # Rising tones for _ in range(5): gc = 255 bc = 0

        for i in range(2000, 5000, 100):
            led.color = (127,gc,bc)
            speaker.play(i, 0.05)
            gc -= 8
            bc += 8
        sleep(0.2)


def siren(): # Nee-Nor! for i in range(10): led.color = (0,0,255) speaker.play(4500, 0.5) led.color = (255,0,0) speaker.play(2500, 0.5)


def bomb(): # Dropping 'alarm' to crash bc = 240 for i in range(5000, 1000, -50): led.color = (127,255,bc) speaker.play(i, 0.05) bc -= 3 led.color = (255,0,0) for i in range(1000): # White noise loop 1 second tone = randint(1000,5000) # Pick a random number speaker.play(tone, 0.001) # Play tone for 1/1000th second sleep(0.2)


def womp(): # Wah-wah-wah-waaaaahhhh led.color = (255,255,255) # White speaker.play(494, 0.5) led.color = (125,125,125) # Dim speaker.play(466, 0.5) led.color = (60,60,60) # Dimmer speaker.play(440, 0.5) for i in range(10): speaker.play(415, 0.05) led.color = (0,0,0) # Off speaker.play(440, 0.05) led.color = (255,255,255) # White speaker.play(415, 0.2)


def noise(): sound = randint(1,6) # Pick a number between 1–6 if sound == 1: tada() elif sound == 2: chirp() elif sound == 3: siren() elif sound == 4: alarm() elif sound == 5: bomb() elif sound == 6: womp()

def safe(): # No sound or light speaker.off() led.off()

# Lus om te controleren of de schakelaar gesloten is

while True: if trigger.is_closed: noise() else: safe()

--- /code ---


--- /collapse ---

**muziekinstrument met twee zoemers – een met een witte ruis die wordt geregeld door een potentiometer** Dit klankbord heeft een potentiometer die de snelheid van het geluid van de eerste zoemer regelt. Door op de knop te drukken, speel je een paar korte noten van de tweede zoemer af.

<video width="640" height="360" controls preload="none" poster="images/instrument-placeholder.png">
<source src="images/pot-speed.mp4" type="video/mp4">
Je browser ondersteunt geen WebM-video, probeer Firefox of Chrome
</video>

--- collapse ---
---
Title: Zie binnenkant
---
--- code ---
---
language: python filename: dj_desk.py line_numbers: true line_number_start:
line_highlights:
---

from picozero import Speaker, Pot, Button from time import sleep

speaker = Speaker(5) speaker2 = Speaker(10) button = Button(18) dial = Pot(0)

BEAT = 0.4

liten_mus = [ ['d5', BEAT / 2], ['d#5', BEAT / 2], ['f5', BEAT], ['d6', BEAT], ['a#5', BEAT], ['d5', BEAT],  
['f5', BEAT], ['d#5', BEAT], ['d#5', BEAT], ['c5', BEAT / 2],['d5', BEAT / 2], ['d#5', BEAT], ['c6', BEAT], ['a5', BEAT], ['d5', BEAT], ['g5', BEAT], ['f5', BEAT], ['f5', BEAT], ['d5', BEAT / 2], ['d#5', BEAT / 2], ['f5', BEAT], ['g5', BEAT], ['a5', BEAT], ['a#5', BEAT], ['a5', BEAT], ['g5', BEAT], ['g5', BEAT], ['', BEAT / 2], ['a#5', BEAT / 2], ['c6', BEAT / 2], ['d6', BEAT / 2], ['c6', BEAT / 2], ['a#5', BEAT / 2], ['a5', BEAT / 2], ['g5', BEAT / 2], ['a5', BEAT / 2], ['a#5', BEAT / 2], ['c6', BEAT], ['f5', BEAT], ['f5', BEAT], ['f5', BEAT / 2], ['d#5', BEAT / 2], ['d5', BEAT], ['f5', BEAT], ['d6', BEAT], ['d6', BEAT / 2], ['c6', BEAT / 2], ['b5', BEAT], ['g5', BEAT], ['g5', BEAT], ['c6', BEAT / 2], ['a#5', BEAT / 2], ['a5', BEAT], ['f5', BEAT], ['d6', BEAT], ['a5', BEAT], ['a#5', BEAT * 1.5] ]

sound = [ [523, 0.1], [None, 0.1], [523, 0.4] ]

def annoying_sound(): speaker.play(sound, wait=False)

button.when_pressed = annoying_sound

try: for note in liten_mus: speaker2.play(note) sleep(dial.value) # Leave a gap between notes depending on potentiometer value finally: speaker.off() # Turns speaker off when code is stopped by user speaker2.off() # Turns speaker2 off when code is stopped by user

--- /code ---


--- /collapse ---

--- /task ---

--- /no-print ---

--- print-only ---

### Ideeën opdoen 💭

Je gaat een aantal ontwerpbeslissingen nemen om je geluidskaart te maken. Hier zijn enkele voorbeelden van geluidsborden die je helpen met je ideeën:

**geluidseffecten bord** Dit geluidsbord is gemaakt van karton met een aantal folieknoppen die geluidseffecten afspelen wanneer je ze activeert.  
![](images/sound-board.png){:width="300px"}

**Speel me een melodie (met behulp van een stopknop)** Er is een drop-switch gemaakt met twee stukjes folie met folie die ook aan de onderkant van een personage is bevestigd. Wanneer het teken op de schakelaar wordt gezet, wordt het deuntje geactiveerd. ![](images/wicked-player.jpeg){:width="300px"}

**Geluidsbom (omgekeerde feestpopper-schakelaar + vervelende SFX-cyclus)** op basis van het vorige Party popper-project laat het een veerbelaste schakelaar (een wasknijper met keukenfolie) sluiten en speelt een eindeloze lus van vervelende geluiden af. ![](images/sound-bomb.PNG){:width="300px"}

**muziekinstrument met twee zoemers – een met een witte ruis die wordt geregeld door een potentiometer** Dit klankbord heeft een potentiometer die de snelheid van het geluid van de eerste zoemer regelt. Door op de knop te drukken, speel je een paar korte noten van de tweede zoemer af. ![](images/pot-speed.png){:width="300px"}

--- /print-only ---

