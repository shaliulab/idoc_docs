# Assembly of chambers in Learning Memory Setup

The IDOC chambers are the key to delivering stimuli to isolated flies while also being able to visually monitor them. Their core design revolves around having controlled points of air in-/out-flow and transparent windows to allow for tracking. Other stimuli such as electric shocks, heat and light (for optogenetic stimulation) can be incorporated as well, via modifications to the chambers or the rest of the machine.

For our IDOC system, we have 2 main chamber variants:
1. "Normal" IDOC chambers which only have air/odor as the in/outputs
2. Electroshock chambers, which have the basic air/odor functionality but also incorporate a conductive glass to deliver currents to the flies

The following sections should elucidate how to build and test either of the chamber types. Since both of these are made from a combination of 3D printed and bought parts, a printing and shopping list will be linked for each. Overlapping components will be highlighted where relevant.

![IDOC-Chamber.PNG](/assets/Images/IDOC-Chamber.PNG)


## **Fabricating the normal IDOC chambers**


[List of files to print](../src/3D_printed_parts/Recording_chambers/)


**1. Cleaning and Adjusting printed parts**:

* 1.1 - Make sure to remove any remaining material from the **support** or **adhesion** of your 3D printed parts. Use warm water to dissolve PVA Material.

* 1.2 - Remove any excess material in the 8 screw holes using a **[2 mm drill bit](https://www.amazon.de/-/en/FOCCTS-0-5-3-0-Rotating-Jewellery-Beeswax/dp/B07DXLFRQ8)**.

* 1.3 - Ensure that the needle holes are clean by removing any excess material in them with a **[0.8 mm drill bit](https://www.amazon.de/-/en/FOCCTS-0-5-3-0-Rotating-Jewellery-Beeswax/dp/B07DXLFRQ8)**. Check all 3 needle holes (top, left and right).





**2. Screws and Needles Insertion**:

* 2.1 - Insert the 8x long-screws **(2M -12 mm, RS , [482-9114](https://benl.rs-online.com/web/p/machine-screws/4829114))** from the bottom side,and check that everything is centered and vertical. Then, using flat screwdriver bit **(RS, [668-5723](https://benl.rs-online.com/web/p/screwdriver-bit-sets/6685727); amazon, ([B01M7PPJI7](https://www.amazon.co.uk/Precision-Screwdriver-Magnetic-Macbook-Electronics/dp/B01M7PPJI7)))**, screw them as far into the chamber as possible. You want the heads of the screws to be flush with the holes they're resting in.

* 2.2 - Center left and right green 0.8mm needles **(BD, [304423](https://www.farmaline.be/apotheek/bestellen/bd-microlance-3-naald-21g-1-12-rb-08x40-mm-groen-1/))**, with 6 mm rubber ring **(VWR, [228-0709](https://be.vwr.com/store/product/nl/577021/slangen-silicone))**, in either side of chamber. Introduce them gently inside enough to be seen from the other side. ??? Same as the step 4.5 - 4.6 later ???

* 2.3 The needle and 6-mm rubber ring are custom cut to a specific length. To shorten the needle, cut it in a way that leaves you roughly 5 mm of extra material, and then sand down that last section. This is necessary to ensure you don't leave behind a "crimped" opening on the needle after cutting it.


**3. Bottom Glass insertion**:

3.1 - Fix **[a rubber gasket](https://benl.rs-online.com/web/p/silicone-rubber-sheets/8405541/)**  to the bottom of the chamber.  The rubber must stand out and fit in its place. Note that the bottom rubber is custom cut to a specific size from translucent silicone rubber sheet **(RS Components, 840-5541)**

3.2 - Add one **ITO/glass slide** to the bottom of the chamber. Keep them horizontal on the bench. 

**4. Inner Chamber Insertion**:

4.1 - Center the middle rubber piece on the top of the glass. Make sure that it is placed correctly in its holder, then insert right and left needles into the rubber.   
note: the middle rubber that hold the inner chamber is custom made to a specific size, and both needle holes are drilled.
  

4.2 - Place the **window-like template** in the top of chamber to create  a room for the inner chamber by cutting out a rectangle inside the rubber. Use a **sharp blade** and the guides of the template. Make it as vertical as possible. Ideally, each side should be done in one stroke

4.3 - Carefully remove the cut part of the rubber. use sharp blade and forceps if needed, then remove the window template.

4.4 - Place one inner chamber in the center of the rubber  

4.5 - Prepare the inner chamber **0.8 mm** holes. Use 0.8 mm drill bit and a very sharp 0.8 mm needle to adjust the three holes. Check the quality of **fish-shape**. ??? 

4.6 - Insert the green needles from step 2.2, until their tip comes out inside the triangular cavities in the inner chamber. Make sure the needles are not blocked or closed. Pressing air through with a syringe can help.

4.7 - Insert and center the **middle needle** to the inner chamber from direction of the inner chamber. Be sure that needle is **not blocked or closed**. Cut the outer part of the needle. 



**5. Connecting outflow tubing and fly gate rubber**:

5.1 - Attach small piece (~5 cm) of tubing **(Silicon Tubing ID 1.5mm x 3 mm OD (VWR, [228-1450](https://be.vwr.com/store/catalog/product.jsp?catalog_number=228-1450)) with WPI lure, [13160-100](https://www.wpiinc.com/13160-100-male-luer-fitting-for-1-16-id-tubing))** to the outer tip of middle needle.

5.2 - Place a 6 mm tubing in the side opening to create an O-ring Rubber in the place where the fly is loaded (gate to provide no leak). Cut it to be aligned with the outer side of the chamber. 



**6. Cleaning, top Glass insertion and Closing**:

6.1 - Add a second **glass-slide** on the top of the inner chamber; Keep them horizontal on the bench. The slide must stand out and fit into its place 

6.2 - Add the top rubber above the glass-slide 

6.3 - Add the **window** to the chamber, then attach 8x nuts **(RS, [248-4551](https://benl.rs-online.com/web/p/hex-nuts/2484551/))** to the screws. Balance and twist them using 4 mm Hexagon Nut Driver **(RS, [323-2581](https://benl.rs-online.com/web/p/nut-drivers/3232581))**. **Do not add much force** Only more squeezing, when they have leakage during testing the chamber.




## **Fabricating the electroshock chambers**

**Indium Tin Oxide coated patterned glass slides** 

For aversive electric shock learning conditioning, we used patterned coated indium tin oxide (ITO) transparent glass slides. ITO is a conductive transparent substance. A grid was laser-cut and -etched onto the ITO glass in order to insulate the positive and negative electrodes. Our ITO slides were designed with the following specifications: 69.0 mm length x 14.0 mm width x 1.1 mm Thicknesses [0.5 mm ITO electrodes (100 electrodes) – 0.1 mm inter electrode-spacing ]. The two halves of the grid can be independently controlled. 



![ITO-slide-design.PNG](/assets/Images/ITO-slide-design.PNG)


| **Indium Tin Oxide coated patterned glass slides ** |
| ---------------------------------------- |
| **- [Design_ITO_glass_Slide](../src/ElectricShock)** CAD DXF drawing |
| 69.0 mm length x 14.0 mm width x 1.1 mm Thicknesses [0.5 mm ITO electrodes (100 electrodes) – 0.1 mm inter electrode-spacing ] |
| **Prepared for the  laboratory of**      |
| **Sha Liu**                              |
| Principle Investigator                   |
| **Email:  [sha.liu@kuleuven.be](mailto:sha.liu@kuleuven.be)** |
| Laboratory of Sleep and Synaptic Plasticity |
| VIB-KU Leuven, Center for Brain and Disease Research, Herestraat 49 - Box 602 B-3000 Leuven - Belgium |
|                                          |
| **Contact Scientist**                    |
| **El-Sayed Baz**                         |
| Postdoctoral Scientist                   |
| **Emails: [elsayed.baz@kuleuven.be](mailto:elsayed.baz@kuleuven.be)      &   [e.baz@science.suez.edu.eg](mailto:e.baz@science.suez.edu.eg)** |
| Laboratory of Sleep and Synaptic Plasticity |
| VIB-KU Leuven, Center for Brain and Disease Research, Herestraat 49 - Box 602 B-3000 Leuven - Belgium |
|                                          |
| **Production laser etching**             |
| **Visiontek systems ltd**                |
| 1 The Acorns, Upton,  Chester,  Cheshire CH2 1JL - United Kingdom. |
| **Email:   **  [visiontek.sales@gmail.com](mailto:visiontek.sales@gmail.com)               & http://www.visionteksystems.co.uk/ito-glass.htm |
|                                          |

**Reorder Details:** 

**15ohm/sq ITOGLASS 15p SODA LIME**

**surface: polished**

**pattern: ZY0423**

**size : 14mm x 69mm x 1.1mm**


**Electrical connections in the chamber**

Each chamber is designed to have four custom-made electrodes that create a connection between the interior and exterior of the IDOC chambers. Inside the chambers, each electrode pin is connected to a long metal strip that connects the left and right side of the chambers. Also, to ensure that the entire ITO slide is subjected to the current, 2 of these metal strips are needed - one for the top and another for the bottom half of the chamber. The ITO slides themselves will rest in contact with these metal strips.

![IDOC-Chamber.PNG](/assets/Images/IDOC-Chamber.PNG)

Both the pins and the connecting metal strip are made in-house from standard electrical components. The metal strips are made from the flat section that crimp sockets are usually delivered with (Farnell, [1593529](https://be.farnell.com/multicomp/2226tg/crimp-terminal-24-28awg/dp/1593529?ost=1593529)). The pins that connect the interior and exterior of the chambers are also simply taken from fairly standard pin headers ([548-7171](https://benl.rs-online.com/web/p/pcb-headers/5487171) or  [548-7222](https://benl.rs-online.com/web/p/pcb-headers/5487222)). To establish a connection between the pins and metal strips, you will simply have to solder them together.



## **Quality control for chambers**

**How to check chambers once assembled**

* Test the chamber by connecting it to the flowmeter. Max 500 ml per litre.  Inflow must equal outflow.
* Test right and left sides independently  
* Use a waterbath to identify the source of any leak. Submerge the chamber in it and pay attention to any bubbles exiting the chamber