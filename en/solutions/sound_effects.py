from picozero import Speaker, RGBLED, Button
from time import sleep
from random import randint

# State which pins the components are placed on the Pico
speaker = Speaker(5)
button1 = Button(18)
button2 = Button(19)
button3 = Button(20)
button4 = Button(21)

#A series of functions which create annoying tones
def tada(): # Ta-Daaa!
    speaker.play(523, 0.1)
    sleep(0.1)
    speaker.play(523, 0.8)
        
def chirp(): # series of high-pitched chirps
    for _ in range(2):
        for i in range(5000, 2999, -100):
            speaker.play(i, 0.02)
        sleep(0.2)
        
def win(): # rising tones
    for i in range(2000, 5000, 100):
        speaker.play(i, 0.05)        
    
def womp(): # wah-wah-wah-waaaaahhhh
    speaker.play(494, 0.5)
    speaker.play(466, 0.5)
    speaker.play(440, 0.5)
    for i in range(10):
        speaker.play(415, 0.05)
        speaker.play(440, 0.05)
    speaker.play(415, 0.2)
            
def stop(): # no sound or light
    
    led.off()
    
button1.when_pressed = tada
button2.when_pressed = chirp
button3.when_pressed = womp
button4.when_pressed = win

try:
    while True:
        sleep(0.1)
finally:
    stop()