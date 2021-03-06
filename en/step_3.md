## Compose your sounds

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
It’s good practice to build your project up gradually. In this step, you will connect and code your buzzers to create different sounds and test that they are working.
</div>
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

Import Speaker from the picozero library, then set the pins:

[[[single-buzzer-pin]]]
[[[multiple-buzzer-pins]]]

--- /task ---
 
It is now time to code your first sound. 

--- task ---

**Define** a function for your first sound. Think of sensible names for your sounds. For example, a function that will play an annoying sound could be called `annoying_sound`.

--- code ---
---
language: python
filename: sound_machine.py
line_numbers: false

---

def sound_1(): # Your sound name

--- /code ---


--- /task ---
 
<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
A <span style="color: #0faeb0">**chiptune**</span>, or 8-bit music, is a tune created by programming the sound chips of computers to produce certain frequencies of sound rather than using traditional instruments — mostly in retro video games and arcade machines. Even though coding music now uses much more advanced techniques, people still love creating and listening to chiptunes because of their retro feel. You can recreate any piece of music you want using chiptune!
</p>


--- task ---

Add code within your new function to play a single note, a tune, or make a sound effect:

### Useful information about sound

[[[list-of-notes]]]

[[[note-length]]]

[[[frequency-numbers]]] 

[[[sheet-to-notes]]]

### Sound code samples

[[[play-single-note]]]

[[[play-a-tune]]]

[[[pico-sound-frequency]]]

[[[whitenoise-drum-beat]]]

[[[sharing-a-ground-pin]]]

[[[notes-in-loop]]]

[[[interrupt-tune]]]


--- collapse ---

---
title: Call a function 
---

Make sure that you have called the functions that you have written.

--- code ---
---
language: python
filename: sound_machine.py
line_numbers: false
line_number_start: 1
line_highlights: 4
---
def chirp(): # Bird chirp sound
    for _ in range(2):
        for i in range(5000, 2999, -100):
            speaker.play(i, 0.02)
        sleep(0.2)

chirp() 

--- /code ---

--- /collapse ---

**Tip:** You can look at the code for the example projects in the [Introduction](.) for more ideas.

--- /task ---

--- task ---

Enter code to **call** your first tune function. 

**Tip:** Make sure that your code to call the function is not indented.

--- /task ---

--- task ---

**Test:** Run your code to test that your sounds play as expected.

If you manually stop your code whilst the buzzer is making a noise, the noise might continue:

[[[buzzer-off-code-stopped]]]

--- /task ---

--- task ---

**Debug:** You might find some bugs that you need to fix. Here are some common bugs.

[[[debug-pico-code]]] 
[[[debug-pico-hardware]]]
[[[pico-debug-led]]]

--- collapse ---

---
title: My tune does not sound as I expected
---

Check your code carefully.
 
You may need to experiment with the notes and timing to get the tune just right.

--- /collapse ---

--- collapse ---

---
title: The main tune delays when I press a button
---

When you use an event such as `when_pressed` to run a function, that function will run until it is finished and it will stop other code from running. 

If you want to start a tune from an event, then you can use `play` with `wait=False`. The function will finish and the tune will continue playing without delaying the code running in your main code.

--- code ---
---
language: python
line_numbers: true
line_number_start: 
line_highlights: 
---

sound = [ [523, 0.1], [None, 0.1], [523, 0.4] ]

def annoying_sound():
    speaker.play(sound, wait=False) # Don't delay the main code 
    
button.when_pressed = annoying_sound

--- /code ---

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
