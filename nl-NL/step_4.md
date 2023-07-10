## Regel je geluiden

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

[[[single-button-wiring]]]
[[[multiple-button-wiring]]]
[[[potentiometer-wiring]]]
[[[crafted-switch-button-wiring]]]
[[[multiple-crafted-switch-button-wiring]]]
[[[sharing-a-ground-pin]]]

**Tip:** als je onderdelen wilt gebruiken die je nog niet eerder hebt gebruikt, of als je nog meer onderdelen wilt bekabelen, bezoek dan onze [Inleiding tot Raspberry Pi Pico](https://projects.raspberrypi.org/nl-NL/projects/introduction-to-the-pico){:target="_blank"} gids.

--- /task ---

--- task ---

Maak een variabele voor elke invoercomponent met behulp van de pin waarop je deze hebt aangesloten:

[[[single-button-pins]]]
[[[multiple-button-pins]]]
[[[single-switch-pins]]]
[[[multiple-switches-pins]]]
[[[potentiometer-pin]]]

--- /task ---

Nu moet je code toevoegen om je melodiefuncties op basis van de invoer te kunnen aanroepen.

--- task ---


--- collapse ---

---
title: Speel een andere melodie af wanneer elke knop wordt ingedrukt
---

Je kunt meerdere knoppen hebben die elk een andere functie aanroepen wanneer ze worden ingedrukt.

Zorg ervoor dat je de functienamen van je project gebruikt. Roep het niet aan door haakjes toe te voegen.

--- code ---
---
language: python
filename: sound_machine.py
line_numbers: false
---

vervelende_knop.when_pressed = vervelend_geluid
kalmerende_knop.when_pressed = kalmerend_geluid
blije_knop.when_pressed = blij_geluid

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Ga naar de volgende melodie wanneer er op een knop wordt gedrukt
---

Gebruik een `optie` variabele om de huidige melodie bij te houden, zodat je kunt beslissen welke functie je daarna wilt aanroepen.

Zorg ervoor dat de functienamen overeenkomen met de melodiefuncties die je in de vorige stap hebt gedefinieerd:

--- code ---
---
language: python
filename: sound_machine.py
line_numbers: false
---
optie = 0 # Sla de huidige optie op.

def choice(): # Roep de volgende functie op en werk de optie bij
    global optie
    if optie == 0:
        vervelend_geluid() # Je eerste nummer
    elif optie == 1:
        kalmerend_geluid() # Je tweede nummer
    elif optie == 2:
        blij_geluid() # Je derde nummer
    elif optie == 3:    
        rgb.off()
    
    # Ga naar de volgende optie
    if optie == 3:
        optie = 0
    else:
        optie = optie + 1

button.when_pressed = choice # Roep de keuzefunctie aan wanneer de knop wordt ingedrukt

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Verander de snelheid van een melodie met een potentiometer
---

Als je een potentiometer gebruikt om de snelheid van de melodie te regelen, dan moet je de volgende code gebruiken:

--- code ---
---
language: python
filename: sound_machine.py
line_numbers: false
line_number_start: 1
line_highlights: 15
---
Slag = 0.4

liten_mus = [ ['d5', Slag / 2], ['d#5', Slag / 2], ['f5', Slag], ['d6', Slag], ['a#5', Slag], ['d5', Slag],  
              ['f5', Slag], ['d#5', Slag], ['d#5', Slag], ['c5', Slag / 2],['d5', Slag / 2], ['d#5', Slag], 
              ['c6', Slag], ['a5', Slag], ['d5', Slag], ['g5', Slag], ['f5', Slag], ['f5', Slag], ['d5', Slag / 2],
              ['d#5', Slag / 2], ['f5', Slag], ['g5', Slag], ['a5', Slag], ['a#5', Slag], ['a5', Slag], ['g5', Slag],
              ['g5', Slag], ['', Slag / 2], ['a#5', Slag / 2], ['c6', Slag / 2], ['d6', Slag / 2], ['c6', Slag / 2],
              ['a#5', Slag / 2], ['a5', Slag / 2], ['g5', Slag / 2], ['a5', Slag / 2], ['a#5', Slag / 2], ['c6', Slag],
              ['f5', Slag], ['f5', Slag], ['f5', Slag / 2], ['d#5', Slag / 2], ['d5', Slag], ['f5', Slag], ['d6', Slag],
              ['d6', Slag / 2], ['c6', Slag / 2], ['b5', Slag], ['g5', Slag], ['g5', Slag], ['c6', Slag / 2],
              ['a#5', Slag / 2], ['a5', Slag], ['f5', Slag], ['d6', Slag], ['a5', Slag], ['a#5', Slag * 1.5]]

for noot in liten_mus:
        luidspreker.play(noot) 
        sleep(instelwiel.value) # Laat een pauze tussen de noten, afhankelijk van de waarde van de potentiometer

--- /code ---

--- /collapse ---

--- /task ---


--- task ---

**Test:** Voer je script uit en zorg ervoor dat je je melodieën kunt bedienen.

Schakelen je knoppen tussen melodieën? Kun je de snelheid regelen met je potentiometer?

--- /task ---

--- task ---

**Fouten oplossen:** Mogelijk vind je enkele fouten in jouw project die je moet oplossen. Hier zijn enkele veelvoorkomende fouten.

[[[debug-pico-code]]] 
[[[debug-pico-hardware]]]
[[[pico-debug-led]]]

Als je een fout vindt die hier niet wordt vermeld. Kun je achterhalen hoe je deze fout kan oplossen?

We horen graag over je fouten en hoe je ze hebt opgelost. Gebruik de **Feedback verzenden** knop onderaan deze pagina en vertel ons of je een andere fout in je project hebt gevonden.

--- /task ---

