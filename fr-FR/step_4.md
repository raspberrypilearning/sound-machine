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

[[[single-button-wiring]]]
[[[multiple-button-wiring]]]
[[[potentiometer-wiring]]]
[[[crafted-switch-button-wiring]]]
[[[multiple-crafted-switch-button-wiring]]]
[[[sharing-a-ground-pin]]]

**Astuce :** Si tu souhaites utiliser des composants que tu n'as pas utilisés auparavant, ou si tu as besoin d'en câbler d'autres, consulte notre guide [Présentation du Pico](https://projects.raspberrypi.org/fr-FR/projects/introduction-to-the-pico){:target="_blank"}.

--- /task ---

--- task ---

Crée une variable pour chaque composant d'entrée à l'aide du numéro de la broche à laquelle tu l'as connecté :

[[[single-button-pins]]]
[[[multiple-button-pins]]]
[[[single-switch-pins]]]
[[[multiple-switches-pins]]]
[[[potentiometer-pin]]]

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
language: python
filename: sound_machine.py
line_numbers: false
---

bouton_ennuyeux.when_pressed = son_ennuyeux
bouton_calmant.when_pressed = son_calmant
bouton_heureux.when_pressed = son_heureux

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
language: python
filename: sound_machine.py
line_numbers: false
---
option = 0 # Mémoriser l'option actuelle

def choix(): # Appelle la fonction suivante et met à jour l'option
    global option
    if option == 0:
        son_ennuyeux() # Ton premier morceau
    elif option == 1:
        son_calmant() # Ton deuxième morceau
    elif option == 2:
        son_heureux() # Ton troisième morceau
    elif option == 3:    
        rgb.off()
    
    # Passe à l'option suivante
    if option == 3:
        option = 0
    else:
        option = option + 1
    
bouton.when_pressed = choix # Appelle la fonction de choix lorsque le bouton est enfoncé

--- /code ---

--- /collapse ---

--- collapse ---

---
title : Modifier la vitesse d'un morceau à l'aide d'un potentiomètre
---

Si tu utilises un potentiomètre pour contrôler la vitesse de la mélodie, tu devras utiliser le code suivant :

--- code ---
---
language: python
filename: sound_machine.py
line_numbers: false
line_number_start: 1
line_highlights: 15
---
RYTHME = 0.4

liten_mus = [ ['d5', RYTHME / 2], ['d#5', RYTHME / 2], ['f5', RYTHME], ['d6', RYTHME], ['a#5', RYTHME], ['d5', RYTHME],  
              ['f5', RYTHME], ['d#5', RYTHME], ['d#5', RYTHME], ['c5', RYTHME / 2],['d5', RYTHME / 2], ['d#5', RYTHME], 
              ['c6', RYTHME], ['a5', RYTHME], ['d5', RYTHME], ['g5', RYTHME], ['f5', RYTHME], ['f5', RYTHME], ['d5', RYTHME / 2],
              ['d#5', RYTHME / 2], ['f5', RYTHME], ['g5', RYTHME], ['a5', RYTHME], ['a#5', RYTHME], ['a5', RYTHME], ['g5', RYTHME],
              ['g5', RYTHME], ['', RYTHME / 2], ['a#5', RYTHME / 2], ['c6', RYTHME / 2], ['d6', RYTHME / 2], ['c6', RYTHME / 2],
              ['a#5', RYTHME / 2], ['a5', RYTHME / 2], ['g5', RYTHME / 2], ['a5', RYTHME / 2], ['a#5', RYTHME / 2], ['c6', RYTHME],
              ['f5', RYTHME], ['f5', RYTHME], ['f5', RYTHME / 2], ['d#5', RYTHME / 2], ['d5', RYTHME], ['f5', RYTHME], ['d6', RYTHME],
              ['d6', RYTHME / 2], ['c6', RYTHME / 2], ['b5', RYTHME], ['g5', RYTHME], ['g5', RYTHME], ['c6', RYTHME / 2],
              ['a#5', RYTHME / 2], ['a5', RYTHME], ['f5', RYTHME], ['d6', RYTHME], ['a5', RYTHME], ['a#5', RYTHME * 1.5]]

for note in liten_mus:
        haut_parleur.play(note) 
        sleep(cadran.value) # Laisse un espace entre les notes en fonction de la valeur du potentiomètre

--- /code ---

--- /collapse ---

--- /task ---


--- task ---

**Test :** Exécute ton script et assure-toi que tu peux contrôler tes morceaux.

Tes boutons changent-ils les morceaux ? Peux-tu contrôler la vitesse avec ton potentiomètre ?

--- /task ---

--- task ---

**Débogage :** Il est possible que tu trouves des bogues dans ton projet que tu dois corriger. Voici quelques bogues assez courants.

[[[debug-pico-code]]] 
[[[debug-pico-hardware]]]
[[[pico-debug-led]]]

Si tu trouves un bogue qui n'est pas répertorié ici. Peux-tu trouver comment y remédier ?

Nous aimons avoir des nouvelles de tes bogues et de la façon dont tu les as corrigés. Utilise le bouton **Envoyer des commentaires** en bas de cette page et dis-nous si tu as trouvé un bogue différent dans ton projet.

--- /task ---

