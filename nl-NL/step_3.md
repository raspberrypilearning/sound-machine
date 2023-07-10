## Stel je geluiden samen

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Het is een goede gewoonte om je project geleidelijk op te bouwen. In deze stap maak je verbinding en codeer je zoemers om verschillende geluiden te maken en te testen of ze werken.
</div>
<div>
![Een grote lijmklem is met plakband vastgemaakt aan de bovenkant van een glazen pot. De lijmklem houdt een trekschakelaar vast, als je daar aan trekt wordt een geluid gemaakt.](images/sound-bomb.PNG){:width="300px"}
</div>
</div>

--- task ---

Sluit je zoemer(s) aan op de Raspberry Pi Pico:

[[[single-buzzer-wire]]]
[[[stereo-buzzer-wiring]]]
[[[earphones-wiring]]]

--- /task ---

--- task ---

Importeer Speaker uit de picozero-bibliotheek en stel vervolgens de pinnen in:

[[[single-buzzer-pin]]]
[[[multiple-buzzer-pins]]]

--- /task ---

Het is nu tijd om je eerste geluid te coderen.

--- task ---

**Definieer** een functie voor je eerste geluid. Bedenk logische namen voor je geluiden. Een functie die een irritant geluid afspeelt, kan bijvoorbeeld `irritant_geluid` heten.

--- code ---
---
language: python
filename: sound_machine.py
line_numbers: false

---

def geluid_1(): # Je geluidsnaam

--- /code ---


--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Een <span style="color: #0faeb0">**chiptune**</span>, of 8-bit muziek, is een melodie die is gemaakt door de geluidschips van computers te programmeren om bepaalde frequenties geluid te produceren in plaats van traditionele instrumenten te gebruiken, vooral in retro-videogames en arcade-machines. Hoewel het coderen van muziek nu veel geavanceerdere technieken gebruikt, houden mensen nog steeds van het maken en luisteren naar chiptunes vanwege hun retro-gevoel. Je kunt elk muziekstuk dat je wilt opnieuw maken met chiptune!
</p>

--- task ---

Voeg code toe aan je nieuwe functie om een enkele noot of een melodie af te spelen of een geluidseffect te maken:

### Nuttige informatie over geluid

[[[list-of-notes]]]

[[[note-length]]]

[[[frequency-numbers]]]

[[[sheet-to-notes]]]

### Voorbeelden van geluidscodes

[[[play-single-note]]]

[[[play-a-tune]]]

[[[pico-sound-frequency]]]

[[[whitenoise-drum-beat]]]

[[[sharing-a-ground-pin]]]

[[[notes-in-loop]]]

[[[interrupt-tune]]]


--- collapse ---

---
title: Roep een functie aan
---

Zorg ervoor dat je de functies die je hebt geschreven worden aangeroepen.

--- code ---
---
language: python
filename: sound_machine.py
line_numbers: false
line_number_start: 1
line_highlights: 4
---
def tjilpen(): # Vogel getjilp geluid
    for _ in range(2):
        for i in range(5000, 2999, -100):
            luidspreker.play(i, 0.02)
        sleep(0.2)

tjilpen() 

--- /code ---

--- /collapse ---

**Tip:** je kunt de code voor de voorbeeldprojecten bekijken in de [Inleiding](.) voor meer ideeën.

--- /task ---

--- task ---

Voer code in om je eerste functie voor een noot of melodie **aan te roepen**.

**Tip:** Zorg ervoor dat je nieuwe code niet inspringt.

--- /task ---

--- task ---

**Test:** Voer je code uit om te testen of je geluiden worden afgespeeld zoals verwacht.

Als je de code handmatig stopt terwijl de zoemer een geluid maakt, kan het geluid aanhouden:

[[[buzzer-off-code-stopped]]]

--- /task ---

--- task ---

**Fouten oplossen:** Mogelijk vind je enkele fouten in jouw project die je moet oplossen. Hier zijn enkele veelvoorkomende fouten.

[[[debug-pico-code]]] 
[[[debug-pico-hardware]]]
[[[pico-debug-led]]]

--- collapse ---

---
title: Mijn melodie klinkt niet zoals ik had verwacht
---

Controleer je code zorgvuldig.

Je moet misschien experimenteren met de noten en de timing om de melodie juist te krijgen.

--- /collapse ---

--- collapse ---

---
title: De hoofdmelodie wordt te laat afgespeeld wanneer ik op een knop druk
---

Wanneer je een gebeurtenis gebruikt zoals `wanneer_ingedrukt` om een functie uit te voeren, wordt die functie uitgevoerd totdat deze is voltooid en stopt de andere code.

Als je een melodie met een gebeurtenis ("event") wilt starten, kun je `PLAY` gebruiken met `wait=False`. De functie wordt voltooid en de melodie blijft spelen zonder de code, die in je hoofdcode wordt uitgevoerd, te vertragen.

--- code ---
---
language: python
line_numbers: true
line_number_start: 
line_highlights: 
---

geluid = [ [523, 0.1], [None, 0.1], [523, 0.4] ]

def vervelend_geluid():
    luidspreker.play(geluid, wait=False) # Vertraag de hoofdcode niet 
    
knop.when_pressed = vervelend_geluid

--- /code ---

--- /collapse ---

Als je een fout vindt die hier niet wordt vermeld. Kun je erachter komen hoe je het kunt oplossen?

We horen graag over je fouten en hoe je ze hebt opgelost. Gebruik de **Feedback verzenden** knop onderaan deze pagina en vertel ons of je een andere fout in je project hebt gevonden.

--- /task ---

--- task ---

**Maak** en **test** de rest van de melodiefuncties die je wilt maken.

Vergeet niet om:
+ De functie te definiëren
+ De code in te voeren om je melodie af te spelen
+ De functie aan te roepen
+ De functie te testen

**Tip:** Vergeet niet om `#` een commentaarregel te gebruiken, of de functie-aanroep van de vorige melodie te verwijderen, zodat je alleen de melodie hoort die je wilt testen.

--- /task ---
