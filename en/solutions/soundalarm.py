from picozero import Speaker, RGBLED, Switch
from time import sleep
from random import randint

# State which pins the components are placed on the Pico
speaker = Speaker(5)
led = RGBLED(13, 14, 15)
trigger = Switch(18)

#A series of functions which create annoying tones

def tada(): # Ta-Daaa!
    led.color = (250,125,0)
    speaker.play(523, 0.1)
    led.color = (0,0,0)
    sleep(0.1)
    led.color = (250,125,0)
    speaker.play(523, 0.6)


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
