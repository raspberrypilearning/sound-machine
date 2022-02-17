## Control your sounds

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
You need a way for the user to control the sounds. In this step, you will connect and code your control interfaces and test that this is working.
</div>
<div>
![](images/image.png){:width="300px"}
</div>
</div>

--- task ---

**Find** the input components that you want to use for your sound machine. 

You could use:
+ One button for each tune
+ A single button to move to the next tune
+ Two socket to pin jumper wires that you can connect to a crafted button or switch
+ A potentiometer to select the tune or BPM (beats per minute) depending on the dial position

You will also need two socket-socket jumper wires for each button or three socket-to-socket wires for a potentiometer. 

--- /task ---

--- task ---

Connect your input components to the Raspberry Pi Pico.

[[[single-button-wiring]]]
[[[multiple-button-wiring]]]
[[[potentiometer-wiring]]]
[[[crafted-switch-button-wiring]]]
[[[multiple-crafted-switch-button-wiring]]]
[[[sharing-a-ground-pin]]]

**Tip:** If you want to use components you have not used before, or need to wire some more, visit our [Introduction to the Pico](https://projects.raspberrypi.org/en/projects/introduction-to-the-pico){:target="_blank"} guide. 

--- /task ---

--- task ---

Import the type of input component you are using from the picozero library:

**Tip:** You can combine multiple imports into one line, for example `from picozero import LED, Button`.

--- collapse ---

---
title: Import Button
---

--- code ---
---
language: python
filename: mood-check-in.py
line_numbers: false
line_number_start: 1
line_highlights: 1
---

from picozero import Button

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Import Switch
---

--- code ---
---
language: python
filename: mood-check-in.py
line_numbers: false
line_number_start: 1
line_highlights: 1
---

from picozero import Switch

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Import Potentiometer
---

--- code ---
---
language: python
filename: mood-check-in.py
line_numbers: false
line_number_start: 1
line_highlights: 1
---

from picozero import Pot

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

Create a variable for each input component using the pin that you have connected it to:

[[[single-button-pins]]]
[[[multiple-button-pins]]]
[[[single-switch-pins]]]
[[[multiple-switches-pins]]]
[[[potentiometer-pin]]]

--- /task ---

Now you need to add code to call your tune functions based on the input. 

--- task ---


--- collapse ---

---
title: Play a different tune when each button is pressed
---

You can have multiple buttons that each call a different function when they are pressed. 

Make sure you use the function names from your project and just use the name of the function, do not call it by adding brackets.

--- code ---
---
language: python
filename: sound-machine.py
line_numbers: false
line_number_start: 
line_highlights: 
---

annoying_button.when_pressed = annoying_sound
calming_button.when_pressed = calming_sound
happy_button.when_pressed = happy_sound

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
language: python
filename: sound-machine.py
line_numbers: false
line_number_start: 
line_highlights: 
---
option = 0 # store the current option

def choice(): # call the next function and update the option
    global option
    if option == 0:
        annoying_sound() # your first tune
    elif option == 1:
        calming_sound() # your second tune
    elif option == 2:
        happy_sound() # your third tune
    elif option == 3:    
        rgb.off()
    
    # move to the next option
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

If you are using a potentiometer to control the speed of the tune then you will need to use the following code: 

<mark> Add code in when picozero has been updated </mark>

--- code ---
---
language: python
filename: sound-machine.py
line_numbers: false
line_number_start: 
line_highlights: 
---

--- /code ---

--- /collapse ---

--- /task ---


--- task ---

**Test:** Run your script and make sure that you can control your tunes. 

Do your buttons switch between tunes? Can you control the speed with your potentiometer? 

--- /task ---

--- task ---

**Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

[pico-common-code-errors]

<mark>add an ingredient about using the onboard led to test outputs when no sound is heard</mark>

Code runs, but nothings happens:
+ Check that your inputs are connected correctly and that you used the correct pin in your code
+ Check the Thonny Shell for any messages about variables or functions not being defined, you might have forgotten to change the examples to match your code
+ Check your code carefully. You could add `print` statements to help you understand what is happening. 

If you find a bug that is not listed here. Can you work out how to fix it?

We love hearing about your bugs and how you fixed them. Use the **Send feedback** button at the bottom of this page and tell us if you found a different bug in your project.

--- /task ---

--- save ---