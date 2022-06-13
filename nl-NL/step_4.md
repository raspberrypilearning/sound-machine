## Control your sounds

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
You need a way for the user to control the sounds. In this step, you will connect and code your control interfaces and test that this is working.
</div>
<div>
![This sound machine has a potentiometer that controls the speed of the tune played from the first buzzer. Pressing the button plays a couple of short notes from the second buzzer.](images/pot-speed.png){:width="300px"}
</div>
</div>

--- task ---

**Find** the input components that you want to use for your sound machine.

You could use:
+ One button for each note, tune, or effect
+ A single button to move to the next sound
+ Two socket–pin jumper wires that you can connect to a crafted button or switch
+ A potentiometer to select the tune or BPM (beats per minute) depending on the dial position

You will also need two socket–socket jumper wires for each button or three socket–socket wires for a potentiometer.

--- /task ---

--- task ---

Connect your input components to the Raspberry Pi Pico.

\[[[single-button-wiring]]\] \[[[multiple-button-wiring\]]] \[[[potentiometer-wiring]]\] \[[[crafted-switch-button-wiring\]]] \[[[multiple-crafted-switch-button-wiring]]\] \[[[sharing-a-ground-pin\]]]

**Tip:** If you want to use components you have not used before, or need to wire some more, visit our [Introduction to the Pico](https://projects.raspberrypi.org/en/projects/introduction-to-the-pico){:target="_blank"} guide.

--- /task ---

--- task ---

Create a variable for each input component using the pin that you have connected it to:

\[[[single-button-pins]]\] \[[[multiple-button-pins\]]] \[[[single-switch-pins]]\] \[[[multiple-switches-pins\]]] [[[potentiometer-pin]]]

--- /task ---

Now you need to add code to call your tune functions based on the input.

--- task ---


--- collapse ---

---
title: Play a different tune when each button is pressed
---

You can have multiple buttons that each call a different function when they are pressed.

Make sure you use the function names from your project and just use the name of the function. Do not call it by adding brackets.

--- code ---
---
language: python filename: sound_machine.py
line_numbers: false
---

annoying_button.when_pressed = annoying_sound calming_button.when_pressed = calming_sound happy_button.when_pressed = happy_sound

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Change to the next tune when a single button is pressed
---

Use an `option` variable to keep track of the current tune so that you can decide which function to call next.

Make sure the function names match the tune functions you defined in the previous step:

--- code ---
---
language: python filename: sound_machine.py
line_numbers: false
---
option = 0 # Store the current option

def choice(): # Call the next function and update the option global option if option == 0: annoying_sound() # Your first tune elif option == 1: calming_sound() # Your second tune elif option == 2: happy_sound() # Your third tune elif option == 3:    
rgb.off()

    # Move to the next option
    if option == 3:
        option = 0
    else:
        option = option + 1

button.when_pressed = choice # Call the choice function when the button is pressed

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Change the speed of a tune using a potentiometer
---

If you are using a potentiometer to control the speed of the tune, then you will need to use the following code:

--- code ---
---
language: python filename: sound_machine.py line_numbers: false line_number_start: 1
line_highlights: 15
---
BEAT = 0.4

liten_mus = [ ['d5', BEAT / 2], ['d#5', BEAT / 2], ['f5', BEAT], ['d6', BEAT], ['a#5', BEAT], ['d5', BEAT],  
['f5', BEAT], ['d#5', BEAT], ['d#5', BEAT], ['c5', BEAT / 2],['d5', BEAT / 2], ['d#5', BEAT], ['c6', BEAT], ['a5', BEAT], ['d5', BEAT], ['g5', BEAT], ['f5', BEAT], ['f5', BEAT], ['d5', BEAT / 2], ['d#5', BEAT / 2], ['f5', BEAT], ['g5', BEAT], ['a5', BEAT], ['a#5', BEAT], ['a5', BEAT], ['g5', BEAT], ['g5', BEAT], ['', BEAT / 2], ['a#5', BEAT / 2], ['c6', BEAT / 2], ['d6', BEAT / 2], ['c6', BEAT / 2], ['a#5', BEAT / 2], ['a5', BEAT / 2], ['g5', BEAT / 2], ['a5', BEAT / 2], ['a#5', BEAT / 2], ['c6', BEAT], ['f5', BEAT], ['f5', BEAT], ['f5', BEAT / 2], ['d#5', BEAT / 2], ['d5', BEAT], ['f5', BEAT], ['d6', BEAT], ['d6', BEAT / 2], ['c6', BEAT / 2], ['b5', BEAT], ['g5', BEAT], ['g5', BEAT], ['c6', BEAT / 2], ['a#5', BEAT / 2], ['a5', BEAT], ['f5', BEAT], ['d6', BEAT], ['a5', BEAT], ['a#5', BEAT * 1.5]]

for note in liten_mus: speaker.play(note) sleep(dial.value) # Leave a gap between notes depending on the potentiometer value

--- /code ---

--- /collapse ---

--- /task ---


--- task ---

**Test:** Run your script and make sure that you can control your tunes.

Do your buttons switch between tunes? Can you control the speed with your potentiometer?

--- /task ---

--- task ---

**Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

\[[[debug-pico-code]]\] \[[[debug-pico-hardware\]]] [[[pico-debug-led]]]

If you find a bug that is not listed here. Can you work out how to fix it?

We love hearing about your bugs and how you fixed them. Use the **Send feedback** button at the bottom of this page and tell us if you found a different bug in your project.

--- /task ---

