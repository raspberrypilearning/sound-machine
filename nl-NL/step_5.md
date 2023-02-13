## Maak je apparaat

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Maak de fysieke onderdelen van je nieuwe klankbord.
</div>
<div>
![Dit klankbord is gemaakt van karton met een aantal knoppen van folie die geluidseffecten afspelen wanneer je ze activeert.](images/sound-board.png){:width="300px"}
</div>
</div>

--- task ---

**denk na:** Enkele vragen die je moet stellen bij het ontwerp van de behuizing en interface voor je klankbord zijn:

+ Welke materialen ga je gebruiken? Wat heb je beschikbaar?
+ Als je knoppen of schakelaars zelf maakt, wat voor soort ga je dan maken? Hoe gaan ze werken?
+ Hoe bevestig je de bedieningselementen zodat ze stevig en gemakkelijk te bereiken zijn?

--- /task ---

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
<span style="color: #0faeb0">Akoestische technici</span> bestuderen de wetenschap van geluid en nemen beslissingen om de beste ervaring aan het publiek te bieden. Hoe ga je ervoor zorgen dat het ontwerp van je geluidsapparaat een goede geluidskwaliteit biedt? 
</p>

--- task ---

**Tip:** Zorg ervoor dat je code **opgeslagen** is en dat je Thonny-console geminimaliseerd is. Dit helpt je om te voorkomen dat je per ongeluk op je toetsenbord tikt en je code bewerkt terwijl je je klankbord maakt.

--- /task ---

--- task ---

**Zoek** de materialen die je gaat gebruiken om de fysieke onderdelen van je klankbord te maken.

Je zou kunnen gebruiken:
+ Kartonnen dozen
+ Gerecyclede plastic voorwerpen
+ Oud speelgoed
+ LEGO
+ Duct tape
+ Hete lijm (vraag een volwassene!)
+ Schaar (vraag een volwassene!)
+ Stanley mes (vraag een volwassene!)
+ 3D-printer (als je geluk hebt!)

--- /task ---

--- task ---

Als je ervoor hebt gekozen om knoppen of schakelaars zelf te maken, is dit het moment om ze te maken.

Er zijn veel verschillende manieren om knoppen en schakelaars te maken die je kunt verbinden met de Raspberry Pi Pico.

Je moet geleidend materiaal zoals aluminiumfolie gebruiken en een verbinding maken tussen een **GND** pin en een **GP** pin. De Raspberry Pi Pico zal kunnen lezen of GND en de GP pin zijn aangesloten.

Hier zijn enkele voorbeelden:

[[[drop-switch]]]

[[[pull-switch]]]

Wees voorzichtig als je scherp of heet gereedschap gebruikt en zorg dat je toestemming en begeleiding hebt van volwassenen voordat je begint.

[[[using-craft-knife]]]

--- /task ---

--- task ---

Noteer welke pinnen voor elk onderdeel zijn gebruikt. Dit helpt je om de draden weer op je Raspberry Pi Pico aan te sluiten.

**Tip**: De pinnen staan bovenaan je code.

--- /task ---

--- task ---

Zet je klankbord in elkaar. Probeer de behuizing niet permanent aan elkaar te lijmen, omdat je draden of onderdelen later mogelijk wilt vervangen.

**Tip:** gebruik plakband om de draden vast te zetten, omdat de bedrading kan losraken tijdens het monteren van het klankbord.

[[[joining-jumper-wires]]]

[[[mount-components]]]

[[[taping-components]]]

--- /task ---

--- task ---

**Test** je klankbord. Nu dat de onderdelen zijn gemonteerd, controleer of ze nog steeds werken zoals bedoeld.

--- /task ---

--- task ---

**Fouten oplossen:**

Je code werkte voordat je het klankbord samenstelde. Het is onwaarschijnlijk dat je code in dit stadium gebroken is. Het merendeel van de fouten zal afkomstig zijn van bedrading en componenten.

[[[debug-pico-hardware]]]

--- collapse ---
---
title: Mijn draden zijn niet lang genoeg nu ze in mijn klankbord zitten
---

Nu je je klankbord hebt gemaakt, heb je mogelijk extra lange draden nodig om je component aan je Raspberry Pi-pinnen te bevestigen. Bekijk de instructies hierboven om 'verbindingsdraden te verbinden om ze te verlengen'.

--- /collapse ---

--- collapse ---
---
title: Mijn draden of componenten blijven niet op hun plaats zitten
---

Sommige verbindingen zijn sterker dan andere, dus het kan zijn dat je tape moet gebruiken om je draden verbonden te houden met je componenten of om je componenten op hun plaats te houden. Bekijk de instructies hierboven om 'draden en componenten vast te zetten met tape'.

--- /collapse ---

--- /task ---


