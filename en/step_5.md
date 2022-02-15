## Craft your device

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Make the physical parts of your new sound machine.
</div>
<div>
![](images/image.png){:width="300px"}
</div>
</div>

--- task ---

**Think:** Some questions to consider in the design of the casing and interface for your sound machine: 

+ What materials will you use? What do you have available?
+ What kind of switches will you make? How will they operate? (If you used them)
+ How will you mount your potentiometer so it is sturdy and easy to reach? (If you used one)
+ How will you ensure your sound machine has the best sound quality

--- /task ---

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
 <span style="color: #0faeb0"></span> 
</p>

--- task ---

Make sure that your code is **saved** and that your Thonny console is minimised. This will help to avoid you accidentally tapping your keyboard and editing your code whilst you make your sound machine. 

--- /task ---

--- task ---

**Find** the materials you will use to create the physical parts of your sound machine.

You could use:
+ Cardboard boxes
+ Recycled plastic items
+ Old toys
+ LEGO
+ Duct tape
+ Hot glue (ask an adult!)
+ Scissors (ask an adult!)
+ Craft knife (ask an adult!)
+ 3D printer (if you're very lucky!)

--- /task ---

--- task ---

If you have chosen to craft buttons or switches, now is the time to make them. 

There are lots of different ways to craft buttons and switches that you can connect to the Raspberry Pi Pico. 

You need to use conductive material such as kitchen foil and make a connection between a **GND** pin and a **GP** pin. The Raspberry Pi Pico will be able to read whether GND and the GP pin are connected.

Here are some examples:

drop-switch

card-push-buttons

pull-switch

conductive-tape-switch

Be careful if you are using any sharp or hot tools and get adult permission and supervision before you start!

--- /task ---

--- task ---

**Write down** which pins have been used for each component to help you connect your wires back onto your Raspberry Pi Pico. 

**Tip**: The pins are listed at the top of your code.

--- /task ---

--- task ---

**Assemble** your sound machine.

**Tip:** Your wiring might come loose as you assemble your sound machine. Use sticky tape to secure your wires. Also, try not to permanently glue your enclosure together to allow you to go back in and replace wires / components if needed. 

joining-jumper-wires   # how to extend the length of wires by joining jumper wires

mount-to-card-plastic  # how to mount components to plastic or card

using-sticky-tape-wires # how to use sticky tape to secure wires and components

using-craft-knife # tips and safety info on using a craft knife

--- /task ---

--- task ---

**Test:** your sound machine. Now that it has been assembled, check that your components still work as intended. 

--- /task ---

--- task ---

**Debug:** 

Your code was working before you assembled your sound machine. It is unlikely that your code will be broken at this stage. The majority of bugs will be from wiring and components. 

+ Check that your components are wired to the correct pins (you should have noted these down earlier, they are displayed at the top of your code)
+ Check that the **positive** leg of the buzzer is attached to the **GP** pin and not **GND**
+ If you are using a potentiometer, check that it is wired correctly
+ Look for any loose connections and secure with tape
+ Check that you haven't covered any conductive elements of your circuit with sticky tape or glue

[[[potentiometer-wiring]]]

--- /task ---



























--- collapse ---

---
title: Mount components in card or plastic
---

You may want to mount LEDs, buttons, buzzers and potentiometers in card or plastic. 

If your components have soldered jumper wires, make a hole in the card or plastic and then push the component through from the back.

![desc](images/path)

If you are using components with socket-socket jumper wires then remove the jumper wires and push the legs of the component through card. For plastic you will need make holes first by carefully using a tool with a sharp point. 

**Tip:** Remember which leg connects to which jumper wire. 

Then reconnect the jumper wires on the back of the card or plastic. 

If necessary you can use sticky tape or electrical tape to keep your components in place. 

![desc](images/path)

--- /collapse ---


--- collapse ---

---
title: Use tape to hold jumper wires in place
---

Use sticky tape or electrical tape to hold jumper wires in place so that your device stays together. 

You can remove the tape later if you want to reuse the components. 

--- /collapse ---

--- collapse ---
---
title: Using a craft or utility knife
---

Craft and utility knives are very useful when making models, but you must be very careful when using them, as they are extremely sharp and can easily cause an injury. If you are using a craft or utility knife, make sure you have a responsible adult with you, or ask them to do the cutting for you if you prefer. It's also a good idea to use a cutting mat to protect the surface you are working on. If you don't have a cutting mat, a kitchen chopping board is a great alternative.

![A box cutting knife.](https://upload.wikimedia.org/wikipedia/commons/c/cf/Box-cutter.jpg)

--- /collapse ---

--- collapse ---
---
title: Joining together jumper wires
---

You might need extra-long wires to attach your LED to your Raspberry Pi pins. You can do this by 'daisy chaining' wires together. For instance, to make an extra-long socket-socket wire, you can attach an pin-socket wire to a socket-socket wire.

![A pin-socket wire attached to a socket-socket wire.](images/daisy-chain.jpg)

The problem with this method is that often the wires will become detached from each other. You can use a small piece of tape to secure the connection.

![A pin-socket wire taped to a socket-socket wire.](images/tape-daisy-chain.jpg)

--- /collapse ---

--- /task ---


--- save ---

