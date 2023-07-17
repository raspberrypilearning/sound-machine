## Fabrique ton appareil

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Fabrique les parties physiques de ta nouvelle machine à sons.
</div>
<div>
![Cette carte à sons a été fabriquée à partir de carton avec un certain nombre de boutons en aluminium qui produisent des effets sonores lorsqu'ils sont activés.](images/sound-board.png){:width="300px"}
</div>
</div>

--- task ---

**Réfléchis :** Voici quelques questions à te poser lors de la conception du boîtier et de l'interface de ta machine à sons :

+ Quels matériaux vas-tu utiliser ? Qu'as-tu à disposition ?
+ Si tu fabriques des boutons ou des interrupteurs, quel type feras-tu ? Comment fonctionneront-ils ?
+ Comment vas-tu monter tes commandes pour qu'elles soient solides et faciles d'accès ?

--- /task ---

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
<span style="color: #0faeb0">Les ingénieurs acoustiques</span> étudient la science du son et prennent des décisions pour offrir la meilleure expérience au public. Comment t'assureras-tu que la conception de ta machine à sons, offre une bonne qualité sonore ? 
</p>

--- task ---

**Astuce :** Assure-toi que ton code est **enregistré** et que ta console Thonny est minimisée. Cela t'aidera à éviter d'appuyer accidentellement sur ton clavier et d'éditer ton code pendant que tu crées ta machine à sons.

--- /task ---

--- task ---

**Trouve** les matériaux que tu utiliseras pour créer les parties physiques de ta machine à sons.

Tu peux utiliser :
+ Boîtes en carton
+ Articles en plastique recyclé
+ Vieux jouets
+ Lego
+ Du ruban adhésif
+ De la colle chaude (demande l'aide d'un adulte !)
+ Ciseaux (demande l'aide d'un adulte !)
+ Couteau de bricolage (demande l'aide d'un adulte !)
+ Imprimante 3D (si tu es très chanceux !)

--- /task ---

--- task ---

Si tu as choisi de fabriquer des boutons ou des interrupteurs, il est maintenant temps de les fabriquer.

Il existe de nombreuses façons de créer des boutons et des interrupteurs que tu peux connecter au Raspberry Pi Pico.

Tu dois utiliser un matériau conducteur tel que du papier d'aluminium et établir une connexion entre une broche **GND** et une broche **GP**. Le Raspberry Pi Pico pourra ainsi détecter si les broches GND et GP sont connectés.

Voici quelques exemples :

[[[drop-switch]]]

[[[pull-switch]]]

Soit prudent si tu utilises des outils tranchants ou chauds et obtient la permission et la supervision d'un adulte avant de commencer.

[[[using-craft-knife]]]

--- /task ---

--- task ---

Note les broches qui ont été utilisées pour chaque composant. Cela t'aidera à reconnecter tes fils sur ton Raspberry Pi Pico.

**Astuce**: Les broches sont listées en haut de ton code.

--- /task ---

--- task ---

Assemble ta machine à sons. Essaye de ne pas coller ton boîtier de manière permanente car tu pourrais vouloir remplacer des fils ou des composants ultérieurement.

**Astuce :** Utilise du ruban adhésif pour fixer tes fils car ton câblage pourrait se détacher pendant que tu assembles ta machine à sons.

[[[joining-jumper-wires]]]

[[[mount-components]]]

[[[taping-components]]]

--- /task ---

--- task ---

**Teste** ta machine à sons. Maintenant qu'elle est assemblée, vérifie que tes composants fonctionnent toujours comme prévu.

--- /task ---

--- task ---

**Déboguer:**

Ton code fonctionnait avant que tu n'aies assemblé ta machine à sons. Il est peu probable que ton code soit cassé à ce stade. La majorité des bogues proviendront du câblage et des composants.

[[[debug-pico-hardware]]]

--- collapse ---
---
title : Mes fils ne sont plus assez longs maintenant qu'ils sont dans ma machine à sons
---

Maintenant que tu as conçu ta machine à sons, tu auras peut-être besoin de fils plus longs pour attacher ton composant aux broches de ton Raspberry Pi. Regarde les instructions ci-dessus pour "joindre les fils de connexion pour les étendre".

--- /collapse ---

--- collapse ---
---
title : Mes fils ou mes composants ne tiennent pas en place
---

Certaines connexions sont plus solides que d'autres, tu devras donc peut-être utiliser du ruban adhésif pour maintenir tes fils connectés à tes composants ou pour maintenir tes composants en place sur ta machine. Consulte les instructions ci-dessus pour "fixer les fils et les composants à l'aide de ruban adhésif".

--- /collapse ---

--- /task ---


