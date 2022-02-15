## Compose your sounds

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
</div>
It’s good practice to build your project up gradually. In this step, you will connect and code your buzzers to create different sounds and test that they are working.
<div>
![](images/image.png){:width="300px"}
</div>
</div>

--- task ---

Connect your buzzer(s) to the Raspberry Pi Pico:

[[[single-buzzer-wire]]]
stereo-buzzer-wiring
earphones-wiring

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

<mark>Add StereoSpeaker if added to picozero</mark>

--- /task ---

--- task ---

Add code to set the pins for your connected LED(s):

[[[single-buzzer-pin]]]
multiple-buzzer-pins

<mark>Add StereoSpeaker if added to picozero</mark>

--- /task ---
 
<mark>Music notes and chords? Chiptunes</mark>
<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">**Term**</span> description of term or interesting phrase.
</p>

**Tip:** Create and then test functions one at a time. 

--- task ---

**Create:** functions for each sound or tune that you want to include in your project. 

Add code within the new functions to play a single note, a tune or make a sound effect:

<mark>Need to make decisions on concurrency model.</mark>

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

Play a note and allow other actions to take place while it is playing:

--- code ---
---
language: python
filename: sound-machine.py
line_numbers: false
line_number_start: 1
line_highlights: 1-2
---
def c_note(): 
    speaker.play(523, 0.5, wait=False) 

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

**Tip:** Give your functions names that match the kind of sound they make so you will remember what they do.

--- /task ---

--- task ---

At the end of your code, underneath your mood function definitions, add code to call the function that you want to test. 

**Tip:** Make sure you new code is not indented.

**Test:** Run your code to test that your sounds play as expected.

Update you new code to call your sound functions one at a time testing each one by running your code.

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
line_highlights: 7
---
def chirp(): # Bird chirp sound
    TBD

chirp() 

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

--- collapse ---

---
title: I don't hear anything when I run my sound function
---

+ Check that the pins in your code match the pins your Speaker is connected to.
+ Check that you have removed the sticker that covers the sound hole in new buzzwea

--- /collapse ---

If you find a bug that is not listed here. Can you work out how to fix it?

We love hearing about your bugs and how you fixed them. Use the **Send feedback** button at the bottom of this page and tell us if you found a different bug in your project.

--- /task ---

--- save ---