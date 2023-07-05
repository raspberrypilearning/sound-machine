## Stel je geluiden samen

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Je hebt een manier nodig waarop de gebruiker de geluiden kan regelen. In deze stap verbind en codeer je besturingsinterfaces en test je of dit werkt.
</div>
<div>
![Dit klankbord heeft een potentiometer die de snelheid regelt van de melodie van de eerste zoemer. Als je op de knop drukt, speel je een paar korte noten van de tweede zoemer af.](images/pot-speed.png){:width="300px"}
</div>
</div>

--- task ---

**Zoek** de invoercomponenten die je voor je klankmachine wilt gebruiken.

Je zou kunnen gebruiken:
+ Eén knop voor elke noot, melodie of effect
+ Een enkele knop om naar het volgende geluid te gaan
+ Twee bus–pin verbindingsdraden die je kunt aansluiten op een zelfgemaakte knop of schakelaar
+ Een potentiometer om de melodie of BPM (slagen per minuut) te selecteren, afhankelijk van de positie van het instelwiel

Je hebt ook twee verbindingsdraden met stekkerbussen nodig voor elke knop of drie van die draden voor een potentiometer.

--- /task ---

--- task ---

Sluit de gekozen invoercomponenten aan op de Raspberry Pi Pico.

\[[[single-button-wiring]]\] \[[[multiple-button-wiring\]]] \[[[potentiometer-wiring]]\] \[[[crafted-switch-button-wiring\]]] \[[[multiple-crafted-switch-button-wiring]]\] \[[[sharing-a-ground-pin\]]]

**Tip:** als je onderdelen wilt gebruiken die je nog niet eerder hebt gebruikt, of als je nog meer onderdelen wilt bekabelen, bezoek dan onze [Inleiding tot Raspberry Pi Pico](https://projects.raspberrypi.org/en/projects/introduction-to-the-pico){:target="_blank"} gids.

--- /task ---

--- task ---

Maak een variabele voor elke invoercomponent met behulp van de pin waarop je deze hebt aangesloten:

\[[[single-button-pins]]\] \[[[multiple-button-pins\]]] \[[[single-switch-pins]]\] \[[[multiple-switches-pins\]]] [[[potentiometer-pin]]]

--- /task ---

Nu moet je code toevoegen om je melodiefuncties op basis van de invoer te kunnen aanroepen.

--- task ---


--- collapse ---

---
Title: Speel een andere melodie af wanneer elke knop wordt ingedrukt
---

Je kunt meerdere knoppen hebben die elk een andere functie aanroepen wanneer ze worden ingedrukt.

Zorg ervoor dat je de functienamen van je project gebruikt. Roep het niet aan door haakjes toe te voegen.

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
Title: Ga naar de volgende melodie wanneer er op een knop wordt gedrukt
---

Gebruik een `optie` variabele om de huidige melodie bij te houden, zodat je kunt beslissen welke functie je daarna wilt aanroepen.

Zorg ervoor dat de functienamen overeenkomen met de melodiefuncties die je in de vorige stap hebt gedefinieerd:

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
Title: Verander de snelheid van een melodie met een potentiometer
---

Als je een potentiometer gebruikt om de snelheid van de melodie te regelen, dan moet je de volgende code gebruiken:

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

**Test:** Voer je script uit en zorg ervoor dat je je melodieën kunt bedienen.

Schakelen je knoppen tussen melodieën? Kun je de snelheid regelen met je potentiometer?

--- /task ---

--- task ---

**Fouten oplossen:** Mogelijk vind je enkele fouten in jouw project die je moet oplossen. Hier zijn enkele veelvoorkomende fouten.

\[[[debug-pico-code]]\] \[[[debug-pico-hardware\]]] [[[pico-debug-led]]]

Als je een fout vindt die hier niet wordt vermeld. Kun je achterhalen hoe je deze fout kan oplossen?

We horen graag over je fouten en hoe je ze hebt opgelost. Gebruik de **Feedback verzenden** knop onderaan deze pagina en vertel ons of je een andere fout in je project hebt gevonden.

--- /task ---

