## Contrôle tes sons

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Tu as besoin d'un moyen pour que l'utilisateur puisse contrôler les sons. Dans cette étape, tu vas connecter et coder tes interfaces de contrôle et tester que cela fonctionne.
</div>
<div>
![Cette machine à sons possède un potentiomètre qui contrôle la vitesse du morceau joué sur le premier buzzer. Appuyer sur le bouton pour jouer quelques notes courtes sur le deuxième buzzer.](images/pot-speed.png){:width="300px"}
</div>
</div>

--- task ---

**Recherche** les composants d'entrée que tu souhaites utiliser pour ta machine à sons.

Tu peux utiliser :
+ Un bouton pour chaque note, mélodie ou effet
+ Un seul bouton pour passer au son suivant
+ Deux fils mâle-femelle que tu peux connecter à un bouton ou un interrupteur fabriqué
+ Un potentiomètre pour sélectionner la mélodie ou le BPM (battements par minute) en fonction de la position du cadran

Tu auras également besoin de deux fils femelle-femelle pour chaque bouton ou de trois fils mâle-mâle pour un potentiomètre.

--- /task ---

--- task ---

Connecte tes composants d'entrée au Raspberry Pi Pico.

\[[[single-button-wiring]]\] \[[[multiple-button-wiring\]]] \[[[potentiometer-wiring]]\] \[[[crafted-switch-button-wiring\]]] \[[[multiple-crafted-switch-button-wiring]]\] \[[[sharing-a-ground-pin\]]]

**Astuce :** Si tu souhaites utiliser des composants que tu n'as pas utilisés auparavant, ou si tu as besoin d'en câbler d'autres, consulte notre guide [Présentation du Pico](https://projects.raspberrypi.org/en/projects/introduction-to-the-pico){:target="_blank"}.

--- /task ---

--- task ---

Crée une variable pour chaque composant d'entrée à l'aide du numéro de la broche à laquelle tu l'as connecté :

\[[[single-button-pins]]\] \[[[multiple-button-pins\]]] \[[[single-switch-pins]]\] \[[[multiple-switches-pins\]]] [[[potentiometer-pin]]]

--- /task ---

Maintenant, ajoute du code pour appeler tes fonctions musicales par rapport à l'entrée choisie.

--- task ---


--- collapse ---

---
title : Jouer un morceau différent lorsque tu appuies sur chaque bouton
---

Tu peux avoir plusieurs boutons qui appellent chacun une fonction différente lorsqu'ils sont enfoncés.

Assure-toi d'utiliser les bons noms de fonction de ton projet et utilise simplement le nom de la fonction. Ne l'appel pas en ajoutant des crochets.

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
title : Passer au morceau suivant lorsqu'un seul bouton est enfoncé
---

Utilise une variable `option` pour garder une trace de la mélodie actuelle afin que tu puisses décider ensuite quelle fonction à appeler.

Assure-toi que les noms de fonction correspondent bien aux fonctions musicales que tu as définies à l'étape précédente :

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
title : Modifier la vitesse d'un morceau à l'aide d'un potentiomètre
---

Si tu utilises un potentiomètre pour contrôler la vitesse de la mélodie, tu devras utiliser le code suivant :

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

**Test :** Exécute ton script et assure-toi que tu peux contrôler tes morceaux.

Tes boutons changent-ils les morceaux ? Peux-tu contrôler la vitesse avec ton potentiomètre ?

--- /task ---

--- task ---

**Débogage :** Il est possible que tu trouves des bogues dans ton projet que tu dois corriger. Voici quelques bogues assez courants.

\[[[debug-pico-code]]\] \[[[debug-pico-hardware\]]] [[[pico-debug-led]]]

Si tu trouves un bogue qui n'est pas répertorié ici. Peux-tu trouver comment y remédier ?

Nous aimons avoir des nouvelles de tes bogues et de la façon dont tu les as corrigés. Utilise le bouton **Envoyer des commentaires** en bas de cette page et dis-nous si tu as trouvé un bogue différent dans ton projet.

--- /task ---

