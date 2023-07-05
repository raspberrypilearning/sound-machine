## Compose tes sons

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
C'est une bonne pratique de construire ton projet progressivement. Dans cette étape, tu vas connecter et coder tes buzzers pour créer différents sons et tester leur bon fonctionnement.
</div>
<div>
![Un gros outil de préhension est collé avec du ruban adhésif sur le dessus d'un bocal en verre. Un interrupteur à tirette se trouve à l'intérieur de l'outil de préhension attendant d'être tiré pour créer un son.](images/sound-bomb.PNG){:width="300px"}
</div>
</div>

--- task ---

Connecte ton (tes) buzzer(s) au Raspberry Pi Pico :

\[[[single-buzzer-wire]]\] \[[[stereo-buzzer-wiring\]]] [[[earphones-wiring]]]

--- /task ---

--- task ---

Importe la classe Speaker depuis la bibliothèque picozero, puis définis les broches :

\[[[single-buzzer-pin]]\] \[[[multiple-buzzer-pins\]]]

--- /task ---

Il est maintenant temps de coder ton premier son.

--- task ---

**Définis** une fonction pour ton premier son. Pense à des noms sensés pour tes sons. Par exemple, une fonction qui jouera un son gênant pourrait s'appeler `son_genant`.

--- code ---
---
language: python filename: sound_machine.py line_numbers: false

---

def sound_1(): # Your sound name

--- /code ---


--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Une musique <span style="color: #0faeb0">**chiptune**</span>, ou 8 bits, est une mélodie créée en programmant les puces sonores des ordinateurs pour produire certaines fréquences sonores plutôt qu'en utilisant des instruments traditionnels, principalement dans les jeux vidéo rétro et les machines d'arcade. Même si le codage de la musique utilise désormais des techniques beaucoup plus avancées, les gens aiment toujours créer et écouter des chiptunes en raison de leur sensation rétro. Tu peux recréer n'importe quel morceau de musique que tu veux en utilisant chiptune !
</p>

--- task ---

Ajoute du code dans ta nouvelle fonction pour jouer une seule note, une mélodie ou créer un effet sonore :

### Informations utiles sur le son

[[[list-of-notes]]]

[[[note-length]]]

[[[frequency-numbers]]]

[[[sheet-to-notes]]]

### Exemples de code sonore

[[[play-single-note]]]

[[[play-a-tune]]]

[[[pico-sound-frequency]]]

[[[whitenoise-drum-beat]]]

[[[sharing-a-ground-pin]]]

[[[notes-in-loop]]]

[[[interrupt-tune]]]


--- collapse ---

---
title : Appeler une fonction
---

Assure-toi que tu as appelé les fonctions que tu as écrites.

--- code ---
---
language: python filename: sound_machine.py line_numbers: false line_number_start: 1
line_highlights: 4
---
def chirp(): # Bird chirp sound for _ in range(2): for i in range(5000, 2999, -100): speaker.play(i, 0.02) sleep(0.2)

chirp()

--- /code ---

--- /collapse ---

**Astuce :** Tu peux consulter le code des exemples de projets dans [l'Introduction](.) pour plus d'idées.

--- /task ---

--- task ---

Entre le code pour **appeler** ta première fonction musicale.

**Astuce :** Assure-toi que ton code pour appeler la fonction n'est pas indenté.

--- /task ---

--- task ---

**Test :** Exécute ton code pour tester que tes sons jouent comme prévu.

Si tu arrêtes manuellement ton code alors que le buzzer fait du bruit, le bruit peut continuer :

[[[buzzer-off-code-stopped]]]

--- /task ---

--- task ---

**Débogage :** Il est possible que tu trouves des bogues que tu doives corriger. Voici quelques bogues assez courants.

\[[[debug-pico-code]]\] \[[[debug-pico-hardware\]]] [[[pico-debug-led]]]

--- collapse ---

---
title : Ma mélodie ne sonne pas comme je m'y attendais
---

Vérifie bien ton code.

Tu devras peut-être expérimenter avec les notes et le timing pour obtenir la bonne mélodie.

--- /collapse ---

--- collapse ---

---
title : La mélodie principale est retardée lorsque j'appuie sur un bouton
---

Lorsque tu utilises un événement tel que `when_pressed` pour exécuter une fonction, cette fonction s'exécutera jusqu'à ce qu'elle soit terminée et empêchera l'exécution d'autres codes.

Si tu souhaites démarrer une mélodie à partir d'un événement, tu peux utiliser `play` avec `wait=False`. La fonction se terminera et la mélodie continuera à jouer sans retarder l'exécution du code dans ton code principal.

--- code ---
---
language: python line_numbers: true line_number_start:
line_highlights:
---

sound = [ [523, 0.1], [None, 0.1], [523, 0.4] ]

def annoying_sound(): speaker.play(sound, wait=False) # Don't delay the main code

button.when_pressed = annoying_sound

--- /code ---

--- /collapse ---

Si tu trouves un bogue qui n'est pas répertorié ici. Peux-tu trouver comment y remédier ?

Nous aimons avoir des nouvelles de tes bogues et de la façon dont tu les as corrigés. Utilise le bouton **Envoyer des commentaires** en bas de cette page et dis-nous si tu as trouvé un bogue différent dans ton projet.

--- /task ---

--- task ---

**Crée** et **teste** le reste des fonctions musicales que tu souhaites créer.

Souviens-toi:
+ Définis la fonction
+ Entre le code pour jouer ton morceau
+ Appelle la fonction
+ Teste la fonction

**Astuce :** N'oublie pas de commenter `#` ou de supprimer l'appel de fonction du morceau précédent afin de n'entendre que celui que tu souhaites tester.

--- /task ---
