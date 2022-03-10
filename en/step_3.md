## Compose your sounds

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
</div>
It’s good practice to build your project up gradually. In this step, you will connect and code your buzzers to create different sounds and test that they are working.
<div>
![A large gripping tool is stuck with sticky tape to the top of a glass jar. A pull switch is inside the gripping tool waiting to be pulled to create a sound.](images/sound-bomb.PNG){:width="300px"}
</div>
</div>

--- task ---

Connect your buzzer(s) to the Raspberry Pi Pico:

[[[single-buzzer-wire]]]
[[[stereo-buzzer-wiring]]]
[[[earphones-wiring]]]

--- /task ---

--- task ---

Import `Speaker` from the picozero library:

--- collapse ---

---
title: Import Speaker 
---

--- code ---
---
language: python
filename: sound-machine.py
line_numbers: false
line_number_start: 1
line_highlights: 1
---

from picozero import Speaker

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

Add code to set the pins for your connected buzzer(s):

[[[single-buzzer-pin]]]
[[[multiple-buzzer-pins]]]

--- /task ---
 
It is now time to code your first tune. 

--- task ---

**Define:** a function for your first tune. Think of sensible names for your tune. For example, a function that will play an annoying sound could be called `annoying_sound`.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 1
---

def sound_1(): # Your sound name

--- /code ---


--- /task ---
 
<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
A <span style="color: #0faeb0">**Chiptune**</span>, or 8-bit music, is a tune created by programming the sound chips of computers to produce certain frequencies of sound rather than using traditional instruments - mostly in retro video games and arcade machines. Even though coding music now uses much more advanced techniques, people still love creating and listening to chiptunes because of their retro feel. You can recreate any piece of music at all using chiptune!
</p>

--- task ---

Add code within your new function to play a single note, a tune or make a sound effect:

--- collapse ---

---
title: Add a function to play a single note
---

Play a note and wait for it to finish:

--- code ---
---
language: python
filename: sound-machine.py
line_numbers: false
line_number_start: 1
line_highlights: 1-2
---
def c_note(): 
    speaker.play(523, 0.5) 

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Play a note and allow other actions to take place while it is playing
---

--- code ---
---
language: python
filename: sound-machine.py
line_numbers: false
line_number_start: 1
line_highlights: 1-2
---
def high_sound(): 
    speaker.play(600, 0.5) 
    sleep(0.1)

def low_sound():
    speaker.play(400, 0.5)

button.when_pressed = low_sound

while True: 
    high_sound()

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Make a sound effect
---

<mark>Include library of examples</mark>

--- code ---
---
language: python
filename: sound-machine.py
line_numbers: false
line_number_start: 1
line_highlights: 1-5
---

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Make a whitenoise drum beat effect
---

<mark>Include library of examples</mark>

--- code ---
---
language: python
filename: sound-machine.py
line_numbers: false
line_number_start: 1
line_highlights: 1-5
---
for i in range(100):
    speaker.play(randint(500, 5000), duration=None)
        sleep(0.001)
    speaker.stop()
    sleep(0.5)
--- /code ---

--- /collapse ---

--- collapse ---

---
title: Play a tune
---

<mark>Include library of examples</mark>

--- code ---
---
language: python
filename: sound-machine.py
line_numbers: false
line_number_start: 1
line_highlights: 1-2
---

--- /code ---

--- /collapse ---

<mark>Make an ingredient on reading music and turning it into a chiptune</mark>

--- /task ---

--- task ---

Enter code to **call** your first tune function. 

**Tip:** Make sure that your code to call the function is not indented

--- collapse ---

---
title: Call a function 
---

--- code ---
---
language: python
filename: sound-machine.py
line_numbers: false
line_number_start: 1
line_highlights: 4
---
def chirp(): # Bird chirp sound
    TBD

chirp() 

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Test:** Run your code to test that your sounds play as expected.

--- /task ---

--- task ---

A user can manually stop code that is running using the red stop icon in Thonny. At this point, if a buzzer is making a sound the sound will continue playing - this can be very annoying! 

--- collapse ---

---
title: Turn buzzers off when code is stopped before it has finished
---

--- code ---
---
language: python
filename: sound-machine.py
line_numbers: false
line_number_start: 1
line_highlights: 14, 18-19
---
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


try:
    for note in liten_mus:
        speaker.play(note) 

finally:
    speaker.off() # turns speaker off when code is stopped by user

--- /code ---

--- /collapse ---


--- /task ---

--- task ---

**Debug:** You might find some bugs in your tune that you need to fix. Here are some common bugs.

[[[debug-pico-code]]] 
[[[debug-pico-hardware]]]

--- collapse ---

---
title: My tune does not sound as I expected
---

Check your code carefully.
 
You may need to experiment with the notes and timing to get the tune just right.

--- /collapse ---

If you find a bug that is not listed here. Can you work out how to fix it?

We love hearing about your bugs and how you fixed them. Use the **Send feedback** button at the bottom of this page and tell us if you found a different bug in your project.

--- /task ---

--- task ---

**Create** and **test** the rest of the tune functions that you would like to create. 

Remember to:
+ Define the function
+ Enter the code to play your tune
+ Call the function
+ Test the function

**Tip:** Remember to comment out `#` or delete the function call of the previous tune so that you only hear the one that you would like to test. 

--- /task ---

--- save ---