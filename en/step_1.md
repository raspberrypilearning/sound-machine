## Introduction

Create a sound machine that will play sound effects or music using buttons, switches or a potentiometer.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">**Sounds**</span> can be helpful, calming, annoying and energising. A newborn baby can find a white noise machine calming and the sound helps them sleep. DJs use portable sound machines to compose beats as they travel. Pranksters use sound effect machines to make people laugh. Can you think of a sound machine that you have used in your day to day life?
</p>

You will:

+ Design a device that uses sound for a specific purpose
+ Program music or sounds effects to play on a buzzer
+ Create an interface that allows user control of sounds

To complete this project you will need:

+ A Raspberry Pi Pico with pin headers soldered on
+ A data USB A to micro USB cable
+ A potentiometer or buttons (bought or crafted)
+ A passive tone buzzer 
+ Jumper wires
+ Craft materials including card, sticky tape and kitchen foil

Optional:

+ RGB LED(s) or single colour LED(s) with resistors and jumper wires
+ An additional passive tone buzzer for stereo sound

<mark>Image of many different examples in a strip</mark>

--- no-print ---

<mark>Add examples - we'll need audio for these. </mark>

--- task ---

### Try it 

**Look**

--- /task ---

### Get inspiration 

You are going to make some design decisions to create your sound board.

--- task ---

Explore these example projects to get more ideas for creating your sound machine:

**Sound effects board**
Description
![](images/image)

--- collapse ---
---
title: See inside
---
--- code ---
---
language: python
filename: 
line_numbers: true
line_number_start: 
line_highlights: 
---

--- /code ---


--- /collapse ---

**Play me a tune (using a drop switch)**
A drop switch has been crafted using two pieces of foil with foil also attached to the bottom of a character. When the character is dropped on the switch, the tune activates.

<video width="640" height="360" controls>
<source src="images/wicked-player.mp4" type="video/mp4">
Your browser does not support WebM video, try FireFox or Chrome
</video>

--- collapse ---
---
title: See inside
---
--- code ---
---
language: python
filename: 
line_numbers: true
line_number_start: 
line_highlights: 
---

--- /code ---


--- /collapse ---

**Sound Bomb (inverted party popper switch + annoying SFX cycle)**
Based on the previous Party popper project, when the piece of cardboard is pulled, it allows a spring loaded switch (a clothes peg with tin foil) to close and plays an endless loop of annoying sounds.

<video width="640" height="360" controls>
<source src="images/soundbomb.mp4" type="video/mp4">
Your browser does not support WebM video, try FireFox or Chrome
</video>

--- collapse ---
---
title: See inside
---
--- code ---
---
language: python
filename: soundbomb.py
line_numbers: true
line_number_start: 
line_highlights: 
---

from picozero import Speaker, RGBLED, Switch
from time import sleep
from random import randint

# State which pins the components are placed on the Pico
speaker = Speaker(5)
led = RGBLED(13, 14, 15)
trigger = Switch(18)

# A series of functions which create annoying tones

def tada(): # Ta-Daaa!
    led.color = (250,125,0)
    speaker.play(523, 0.1)
    led.color = (0,0,0)
    sleep(0.1)
    led.color = (250,125,0)
    speaker.play(523, 0.4)
    for i in range(100, 0, -1):
        speaker.play(523, 0.01, i/100)


def chirp(): # series of high-pitched chirps
    for _ in range(5):
        bc = 255
        rc = 0
        for i in range(5000, 2999, -100):
            led.color = (rc,0,bc)
            speaker.play(i, 0.02)
            bc -= 12
            rc += 12
        sleep(0.2)


def alarm(): # rising tones
    for _ in range(5):
        gc = 255
        bc = 0

        for i in range(2000, 5000, 100):
            led.color = (127,gc,bc)
            speaker.play(i, 0.05)
            gc -= 8
            bc += 8
        sleep(0.2)    


def siren(): # Nee-Nor!
    for i in range(10):
        led.color = (0,0,255)
        speaker.play(4500, 0.5)
        led.color = (255,0,0)
        speaker.play(2500, 0.5)


def bomb(): # Dropping 'bomb' to crash
    bc = 240
    for i in range(5000, 1000, -50):
        led.color = (127,255,bc)
        speaker.play(i, 0.05)
        bc -= 3
    led.color = (255,0,0)
    for i in range(1000): # white noise loop 1 sec
        tone = randint(1000,5000) # pick a random number 1k-5k
        speaker.play(tone, 0.001) # play tone for 1/1000th sec
    sleep(0.2)


def womp(): # wah-wah-wah-waaaaahhhh
    led.color = (255,255,255) # white
    speaker.play(494, 0.5)
    led.color = (125,125,125) # dim
    speaker.play(466, 0.5)
    led.color = (60,60,60) # dimmer
    speaker.play(440, 0.5)
    for i in range(10):
        speaker.play(415, 0.05)
        led.color = (0,0,0) # off
        speaker.play(440, 0.05)
        led.color = (255,255,255) # white 
    speaker.play(415, 0.2)    


def noise():
    sound = randint(1,6) # pick a number between 1-6
    if sound == 1:
        tada()
    elif sound == 2:
        chirp()
    elif sound == 3:
        siren()
    elif sound == 4:
        alarm()
    elif sound == 5:
        bomb()
    elif sound == 6:
        womp()
        
def safe(): # no sound or light
    speaker.off()
    led.off()

# loop to check if switch is closed

while True: 
    if trigger.is_closed:
        noise()
    else:
        safe()

--- /code ---


--- /collapse ---

**Musical instrument with two buzzers - one with a whitenoise beat controlled by a potentiometer**
This sound machine has a potentiometer that controls the speed of the tune played from the first buzzer. Pressing the button plays a couple of short notes from the second buzzer.

<video width="640" height="360" controls>
<source src="images/pot-speed.mp4" type="video/mp4">
Your browser does not support WebM video, try FireFox or Chrome
</video>

--- collapse ---
---
title: See inside
---
--- code ---
---
language: python
filename: 
line_numbers: true
line_number_start: 
line_highlights: 
---

from picozero import Speaker, Pot, Button
from time import sleep

speaker = Speaker(5)
speaker2 = Speaker(13)
button = Button(18)
dial = Pot(0)

BEAT = 0.4

liten_mus = [ ['d5', BEAT / 2], ['d#5', BEAT / 2], ['f5', BEAT], ['d6', BEAT], ['a#5', BEAT], ['d5', BEAT],  
              ['f5', BEAT], ['d#5', BEAT], ['d#5', BEAT], ['c5', BEAT / 2],['d5', BEAT / 2], ['d#5', BEAT], 
              ['c6', BEAT], ['a5', BEAT], ['d5', BEAT], ['g5', BEAT], ['f5', BEAT], ['f5', BEAT], ['d5', BEAT / 2],
              ['d#5', BEAT / 2], ['f5', BEAT], ['g5', BEAT], ['a5', BEAT], ['a#5', BEAT], ['a5', BEAT], ['g5', BEAT],
              ['g5', BEAT], ['', BEAT / 2], ['a#5', BEAT / 2], ['c6', BEAT / 2], ['d6', BEAT / 2], ['c6', BEAT / 2],
              ['a#5', BEAT / 2], ['a5', BEAT / 2], ['g5', BEAT / 2], ['a5', BEAT / 2], ['a#5', BEAT / 2], ['c6', BEAT],
              ['f5', BEAT], ['f5', BEAT], ['f5', BEAT / 2], ['d#5', BEAT / 2], ['d5', BEAT], ['f5', BEAT], ['d6', BEAT],
              ['d6', BEAT / 2], ['c6', BEAT / 2], ['b5', BEAT], ['g5', BEAT], ['g5', BEAT], ['c6', BEAT / 2],
              ['a#5', BEAT / 2], ['a5', BEAT], ['f5', BEAT], ['d6', BEAT], ['a5', BEAT], ['a#5', BEAT * 1.5]]

def annoying_sound():
    speaker.play(523, 0.1)
    sleep(0.1)
    speaker.play(523, 0.4)

button.when_pressed = annoying_sound

try:
    for note in liten_mus:
        speaker.play(note) 
        sleep(dial.value) # leave a gap between notes depending on potentiometer value
finally:
    speaker.off()
    speaker2.off()

--- /code ---


--- /collapse ---

--- /task ---

--- /no-print ---

--- print-only ---

### Get inspiration 

You are going to make some design decisions to create your sound board. Here are some example sound boards to help you with your ideas:

<mark>Images of below with short descriptions</mark>

**Sound effects board**
Description
![](images/image)

**Play me a tune (using a drop switch)**
A drop switch has been crafted using two pieces of foil with foil also attached to the bottom of a character. When the character is dropped on the switch, the tune activates.
![A character is dropped on two pieces of kitchen foil and a tune play.](images/wicked-player.jpeg){:width="300px"}

**Sound Bomb (inverted party popper switch + annoying SFX cycle)**
Description
![](images/image)

**Musical instrument with two buzzers - one with a whitenoise beat controlled by a potentiometer**
This sound machine has a potentiometer that controls the speed of the tune played from the first buzzer. Pressing the button plays a couple of short notes from the second buzzer.
![](images/pot-speed.png)

--- /print-only ---

