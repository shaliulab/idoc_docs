# Main Enclosure

![Enclosure.png](/assets/Images/enclosure_annotated_trimmed.png)

## Table of Contents

1. [Overview](#overview)
2. [List of components](#list-of-components)
3. [Building the enclosure](#building-the-enclosure)
    1. [Get the hardboard](#1-get-the-hardboard)
    2. [Join the rails and build the walls](#2-join-the-rails-and-build-the-walls)
    3. [Build the enclosure roof](#3-build-the-enclosure-roof)
    4. [Visualization window](#4-visualization-window)
    5. [Blue light LED strip](#5-blue-light-led-strip)
    6. [Roof exhaust vent](#6-roof-exhaust-vent)
    7. [Enclosure door](#7-enclosure-door)
    8. [Tubing and power holes](#8-tubing-and-power-holes)
4. [Baseplate](#baseplate)
  
##  Overview

The IDOC setup is enclosed in a custom enclosure that isolates the behavioral chambers from the experiment room. When the enclosure is closed, no light from the outside can arrive to the animals, which ensures consistency and reproducibility. Moreover, the enclosure protects the setup components from dust, noise, thermal gradients, etc.

The enclosure is mounted on a Thor labs breadboard. The front face of the enclosure has a sliding door panel, which can easily be removed to open the enclosure and have easy access to the components and behavioral chambers. Its baseplate allows fixing and centering the IDOC system via mounting brackets. It can be mounted on a table or bench. You may construct the enclosure according to the desired size. However, it should be large enough to hold all your setup components. This section details how to construct an enclosure to provide space for the setup, tracking camera, powering, airflow system, and illumination.

Building the IDOC enclosure involves several steps:

1. Build the enclosure proper and the 3D parts to fit the IDOC system.
2. Install a breadboard to mount the enclosure, which provides a platform for mounting and connecting electronic components.
3. Install and wire any necessary electronic, lighting, air/odor components.

The enclosure has three main sections: The breadboard, enclosure itself, and the camera enclosure. In this page we will explain how to build the first two, see the [camera enclosure](/how-to-build/Camera-Enclosure) section for the last one.

The enclosure is made from [25 mm rails](https://www.thorlabs.de/newgrouppage9.cfm?objectgroup_id=194) and [black hardboard](https://www.thorlabs.de/newgrouppage9.cfm?objectgroup_id=190#2535) panels. The panels are placed between the rail channels. The enclosure is designed with the following inner dimensions 500mm x 500mm x 700 mm (L x W x H).


<!-- 
## List of commercial parts

The parts needed are provided in a separate [table](/docs/List-of-Commercial-Parts-Tools.md) and may be downloaded as a [CSV](../src/Commercial_Parts/List-of-Commercial-Parts-Tools.csv) file
-->

## Building the enclosure

### 1. Fabricate the board

**For this step, you will need:**

* Black hardboard (Thorlabs, [TB4](https://www.thorlabs.de/thorproduct.cfm?partnumber=TB4))
* Black hardboard (Thorlabs, [TB5](https://www.thorlabs.de/thorproduct.cfm?partnumber=TB5))
* Adhesive double-sided tape (RS Components, [273-598](https://benl.rs-online.com/web/p/double-sided-tapes/0273598))
* aluminum flat bar (RS Components, [681-104](https://ie.rs-online.com/web/p/metal-bars-metal-rods/0681104))
* Pencil
* Cutter
* Tape measure or ruler


Make sure to order the black board of the right size, or alternatively, you will have to trim it in-house, to fit the dimensions of the setup. We combined two black hardboards together ([TB4](https://www.thorlabs.de/thorproduct.cfm?partnumber=TB4) + [TB5](https://www.thorlabs.de/thorproduct.cfm?partnumber=TB5)) to make it extra robust (~5 mm thick).
The final size of the panels:

* Vertical panels that form the walls of the enclosure: 710 mm x 510 mm (L x W)
* The top panel that forms the roof of the enclosure: 510 mm x 450 mm (L x W)

![Black-board-setup-enclosure.PNG](/assets/Images/Black-board-setup-enclosure.PNG)

**Procedure**

1. Use a tape to mark a line by pencil on the face of the board. The final size should be ~ 5 mm longer and wider than the rail length to fit in the walls and the roof.
2. Cut all the way through the board following the pencil lines. The board is soft, so proceed carefully, an aluminum flat bar can be used to maintain a straight cut.
3. Remove the cuts and trim the rough edges of the board.
4. Attach and align the adhesive double-sided tape within the inside face/ edge of the TB5 board.
5. Simply peel off the tape backing and assemble one TB4 and one TB5 boards together, the adhesive double-sided tape should not be visible on the board when done.
6. Make sure to press firmly on the assembled boards.

### 2. Join the rails and build the walls

**For this step, you will need:**

* Low-Profile Channel Screw (Q: 12x)
* Construction Cube with Slotted Corners (Q: 4x)
* 25 mm square construction rail 500 mm length (Q: 4x)
* 25 mm square construction rail 700 mm length (Q: 4x)
* Customized (710 mm x 510 mm) black hardboard (Q: 3x, see step 1)
* 4 mm balldriver or hex key

![Setup-enclosure.PNG](/assets/Images/Setup-enclosure.PNG)

**Procedure**

1. Attach a low-profile channel screw to the construction cube. The low-profile screw has a shortened cap height that prevents neighboring screws from interfering with each other.
2. Insert 2 screws in perpendicular directions through the cube into the end of each rail and tighten both screws with the balldriver to connect the two rails.
3. Repeat the above step for the other corners to finish the horizontal bottom square frame.
4. Place another channel screw into the third hole of the construction cube, then insert it into the threaded hole in the end of the vertical rail and tighten screws down with the balldriver to create a three-way connection
5. Repeat above step for connecting the other vertical rails.
6. Slide the double board into the channel of the frame rails to form the back, left and right side. Keep the foam core outside of the enclosure, and the darkest board inside the box.

### 3. Build the enclosure roof

The roof is special because you need to cut a window through which the camera can image the behavioral chambers. You can also optionally install ventilation valves that improve the evacuation of odor.

![Top-roof.PNG](/assets/Images/Top-roof.PNG)

**For this step, you will need:**

* Low-Profile Channel Screws (Q:10x)
* Low-Profile T-Nut (Q: 14x)
* 25 mm square construction rail 500mm length (Q: 4x)
* Construction cube with slotted corners (Q: 2x)
* Construction-cube-with-slotted-channel-door-connection, [3D designed](https://github.com/shaliulab/idoc_docs/blob/master/docs/assets/src/3D_printed_parts/Enclosure%26Powering/25-mm_mounting_constructions/Construction_cube_with_slotted_channel_door_connection_universal.stl) (Q: 2x)
* Elbow-L-Connection to connect two rails at a 90° Elbow, [3D designed](https://github.com/shaliulab/idoc_docs/blob/master/docs/assets/src/3D_printed_parts/Enclosure%26Powering/25-mm_mounting_constructions/Elbow_L-shape_door_connection.stl) (Q: 2x)
* Customized (510 mm x 450 mm) black hard board (Q: 1x).
* 4 mm balldriver or hex key


Since the construction cube provided by Thorlabs ([RM1S - 1](https://www.thorlabs.de/thorproduct.cfm?partnumber=RM1S#ad-image-0)) only has slotted corners, we modified the later and printed this [3D design](https://github.com/shaliulab/idoc_docs/blob/master/docs/assets/src/3D_printed_parts/Enclosure%26Powering/25-mm_mounting_constructions/Construction_cube_with_slotted_channel_door_connection_universal.stl) This cube is connected at each top of the front rails and so creates a parallel channel with front rails (see step: Build the enclosure roof). The modified cube creates a slider that allows us to insert the door.

**Procedure**

1. Attach low-profile channel screw to the construction cube.
2. Insert the screw into the threaded hole in the end of each rail and tighten both screws with the balldriver to connect the two rails.
3. Repeat the above step for the other corner to have a U-shaped frame formed by three rails.
4. Slide the blackboard into the channels of the U-shaped frame rails.
5. To mount other parts on the top roof, insert about six-low-profile nuts in each unobstructed end of the rails of the U-shaped frame. Be sure that you inserted the T-Nut before going to the next step, since nuts only can be inserted and removed from the unblocked end of a rail.
6. Attach the 3D printed door construction cube at each end of the U-shaped frame, so that the door slots are vertically in front of each other.
7. Insert the screw into the threaded hole in the end of U-shaped frame and tighten both screws with the balldriver.
8. Use 3D printed elbow L-Connection to connect the fourth rail from each corner by inserting low-Profile T-Nut.
9. Attach low-profile channel screw to the elbow L-Connection.
10. Insert screws into corner low-profile T-nuts in the end of each rail and tighten them down with the balldriver to connect the two rails. Be sure that the elbow L-Connection is not blocking the sliding panel of the door at the 3D-construction cube at each side.

### 4. Visualization window:

A window (112 mm x 112 mm) is made in the center of the roof to allow the visualization of chambers via a camera top-view. This window hosts a 3D-printed box which holds a [polyester infra-red (IR) sheet](https://www.leefilters.com/index.php/camera-directory/camera-dir-list/category/infrared) (100 mm x 100 mm) which has two uses. 1) to prevent unwanted visible light to transmit inside the enclosure and 2) only IR light can be visualized by the camera. Also, the inside face of 3D-printed box can hold a light source (e.g. white LED strip) that might be needed to illuminate the setup while cleaning or during maintenance work.

![IR-window-top-roof.PNG](/assets/Images/IR-window-top-roof.PNG)
![IR-window-top-roof-mount.PNG](/assets/Images/IR-window-top-roof-mount.PNG)

For installation of the IR-Filter and white LED light source you will need the following:

* IR_sheet_holder_roof_fixation_LED_light_stripe_inside_part_1_of_2 [3D-designed](https://github.com/shaliulab/idoc_docs/blob/master/docs/assets/src/3D_printed_parts/Enclosure%26Powering/Roof_IR_Sheet_holder/IR_sheet_holder_roof_fixation_LED_light_stripe_inside_part_1_of_2.stl) (Q:1x)
* IR_sheet_holder_roof_fixation_LEE_filter_ouside_part_2_of_2 [3D-designed](https://github.com/shaliulab/idoc_docs/blob/master/docs/assets/src/3D_printed_parts/Enclosure%26Powering/Roof_IR_Sheet_holder/IR_sheet_holder_roof_fixation_LEE_filter_ouside_part_2_of_2.stl)  (Q:1x)
* Cut_guide_template 3D-designed (Q:1x) - file missing
* LEE Polyester 87 Infrared 100mm filter ([LEEB10087C ](https://www.robertwhite.co.uk/lee-filters-100mm-system-polyester-87c-infrared-filter.html)) (Q:1x)
* Soldering station ([Amazon](https://www.amazon.de/-/en/Soldering-Desoldering-Temperature-Adjustable-Conversion/dp/B08C51QRH5/ref=sr_1_17?keywords=alpha+metals+om338+pastelötmittel&qid=1639747374&sr=8-17)) (RS components, [122-7917](https://benl.rs-online.com/web/p/soldering-stations/1227917))
* 22 AWG wire (RS components: red wire [168-1571](https://benl.rs-online.com/web/p/harsh-environment-wire/1681571) & black wire [168-1559](https://benl.rs-online.com/web/p/harsh-environment-wire/1681559))
* 60 cm white LED Strips (ledlightsworld, [F5050PW30-NW](https://ledlightsworld.com/products/dc-12v-dimmable-smd5050-300-flexible-led-strips-60-leds-per-meter-10mm-width-900lm-per-meter-1?variant=17867978080346)) (Q:4x cut 15 cm each)
* Cutter/scalpel

**Procedure (Build)**

1. Fasten the four LED strips (15 cm each) in place with their adhesive side tape.
2. Solder and connect all LED strips in the square box, the powering wire should be long enough to be connected to a PSU outside the enclosure. Select the wire with red (+V) and black (-V) colors for easy maintenance.
3. Insert the IR filter in the recessed area, then fix it with a drop of fast glue on each corner.
4. This step can be delayed until the complete assembly of the enclosure to avoid scratching of the black IR sheet.
5. In case you decide to attach the IR filter, cover its surface with masking tape or paper, so you don't scratch it while building the other parts of the enclosure.

**Procedure (Installation)**

The position of the window in the roof is key to make sure all chambers are visible. Follow this step to cut the window and install the box with the IR filter.

1. Insert the template at the center of the black board
2. Add a M6 screw in the middle of the template, push the screw through the soft blackboard until it appears on the other face.
3. Use a sharp cutter to cut all the way through the black board following the border of the template. The blackboard is soft, so proceed carefully.
4. Remove the template with the cut and trim the edge of window made by the cutter.
5. Insert 3D printed box with LED strip from the inside part.
6. Make a hole in the blackboard to insert the powering cables outside of the enclosure to be connected to the power supply.
7. Insert the other 3D printed IR sheet holder from the top side.
8. Connect both parts by inserting a screw in each corner of the box.


### 5. Blue light LED strip

You may carry experiments with animals expressing an optogenetic tool that might be sensitive to red light. To be able to see and handle the chambers in IDOC, while also avoiding the undesired activation that could be produced by turning on standard white light, we installed a dim blue light LED strip that allows the experimenter to see while keeping the optogenetic activation at a minimum.

From our *in vivo* patch clamp electrophysiology data, we see that only high intensity blue light can cause problems.Therefore, we illuminate the setup enclosure with a very dim blue light (less than 1µW/mm2). Skip this step if you don't need light.

![Blue-light-installation.PNG](/assets/Images/Blue-light-installation.PNG)


**For this step, you will need:**

* 100 cm Blue LED Strips (ledlightsworld, [F3528Blue60-NW](https://ledlightsworld.com/products/colorful-dc-12v-dimmable-smd3528-600-flexible-led-strips-120-leds-per-meter-8mm-width-600lm-per-meter?variant=17870690320474)) (Q:2x cut 50 cm each)
* Soldering station ([Amazon](https://www.amazon.de/-/en/Soldering-Desoldering-Temperature-Adjustable-Conversion/dp/B08C51QRH5/ref=sr_1_17?keywords=alpha+metals+om338+pastelötmittel&qid=1639747374&sr=8-17)) (RS components, [122-7917](https://benl.rs-online.com/web/p/soldering-stations/1227917))
* Soldering Arm Stand (RS Components, [208-3892](https://benl.rs-online.com/web/p/soldering-accessories/2083892)
* Heat shrink tubing (amazon.de, [ET1002](https://www.amazon.de/Eventronic-ET1002-Schrumpfschlauch-Farben-560-tlg/dp/B071D7LJ31))
* Lead Free Solder (RS Components, [756-8884](https://benl.rs-online.com/web/p/solder/7568884) ; [625-8233](https://benl.rs-online.com/web/p/solder/6258233))
* JST PH 2 pin cable male Header (Digi-Key, [1528-2617-ND](https://www.digikey.be/product-detail/en/adafruit-industries-llc/3814/1528-2617-ND/9380221))


**Procedure (build)**

1. Clamp the end of the LED strip using a soldering arm stand.
2. Since LED light coppers pads have only two terminals, we choose to connect with a 2-bin JST cable with female plug which has two wires one with red color, while the other is black color.
3. Heat your soldering iron station to 350-400 degrees Celsius.
4. Add a small part of soldering material to the surface the copper pads of the LED strips
5. Solder the 2bin JST wires to copper pads in the LED strip. The red wires must be solder to the positive copper cups and the black to the negative ones.
6. Once you have attached the two wires, wait for at least 30 seconds for it to cool down.
7. Use hot air gun to place a shrink tube over the exposed soldered part at the end of each LED strips
8. With scissor cut two of 50 cm LED strips.

**Procedure (installation)**

1. Once everything in the enclosure is set, you can peel off the tape backing expose the adhesive side
2. Place the blue LED strip of tape at the black aluminum rail on the roof.
3. Make sure to press firmly on the LED strips to prevent it from peeling it off.
4. Connect the female JST wire to the male JST power supply plug on the top powering platform at the backside of the enclosure. While the opposite side of the plug can then be connected to a power supply and dimmer switch.


### 6. Roof exhaust vent

Proper ventilation inside the enclosure will preserve its ambient temperature and remove excess odorants. To achieve it, we added two roof vents on the roof. A **Vacuum pump** is used to remove the exhaust air outside of the room, because the smell can severely affect the quality of the experiments.

![Suction_vent.PNG](/assets/Images/Suction_vent.PNG)

**You will need the following:**

* Cap_GL45_vacuum_succion - internal [3D Designed](https://github.com/shaliulab/idoc_docs/blob/master/docs/assets/src/3D_printed_parts/Enclosure%26Powering/Exhaust_vents/Threaded_neck_internal_vacuum_succion_size_GL45_part_2_of_2.stl) (Q: 2x)
* Cap_GL45_vacuum_succion - external [3D Designed](https://github.com/shaliulab/idoc_docs/blob/master/docs/assets/src/3D_printed_parts/Enclosure%26Powering/Exhaust_vents/Threaded_cap_top_external_vacuum_succion_size_GL45_part_1_of_2.stl) (Q: 2x)
* Push in 6 mm fitting Straight adaptor G 1/8 Male (RS Components, [121-6009](https://benl.rs-online.com/web/p/pneumatic-fittings/1216009)) (Q:2x)
* 13 mm Fork ring wrench or spanner (amazon.de, [M19652](https://www.amazon.de/-/en/Brothers-Mannesmann-M19652-wrench-pieces/dp/B000ET7G0E?th=1) ; [B001ILAFRI](https://www.amazon.de/-/en/171198-Combination-Spanner-Set-SW/dp/B001ILAFRI/))
* Pencil
* Cutter
* Tape measure or ruler

**Procedure**

1. Connect the fitting Straight adaptor to the middle hole of the vent cap, tighten the adaptor using 13 mm spanner.
2. Make two holes in the roof of the enclosure so the two exhaust caps can be inserted. A pencil or other sharp tool can be used to mark the holes. A cutter or a 44 mm hole saw drill can be useful to get smooth hole.
3. Insert the threaded neck part from the inside, attach the screw cap part from outside, and then tighten the cap until the assembly is held firmly to the roof to provide proper exhaust vents.

### 7. Enclosure door

**The following parts are needed:**

* [Black hardboard](https://www.thorlabs.de/newgrouppage9.cfm?objectgroup_id=190#2535)  510mmx762mm (L x W) (Thorlabs, [TB5](https://www.thorlabs.de/thorproduct.cfm?partnumber=TB5)) (Q: 2x)
* Aluminum Sandwich Panel Black 510x762 mm (Plexikopen, [Black RAL 9005 3 mm](https://www.plexikopen.be/aluminum-sandwichpaneel-kleur))
* Adhesive double-sided tape (RS Components, [273-598](https://benl.rs-online.com/web/p/double-sided-tapes/0273598))


To close the front side of the enclosure during an experiment, we combined one of [TB5](https://www.thorlabs.de/thorproduct.cfm?partnumber=TB5) black hardboards together with a black aluminum [sandwich panel](https://www.plexikopen.be/aluminum-sandwichpaneel-kleur) to provide more hardness, thickness and to eliminate the passage of light or air through the corners or edges. Be sure that the correct size of the black board has been ordered to fit the dimensions of the door area. There is no need to cut the board.



**Procedure**

1. Use Adhesive double-sided tape to combine one of [TB5](https://www.thorlabs.de/thorproduct.cfm?partnumber=TB5) black hardboard together with a black aluminum [sandwich panel](https://www.plexikopen.be/aluminum-sandwichpaneel-kleur).
2. To close the enclosure, slide the door board from the top into the top parallel channels of the cube-rail-constructions.
3. To remove the door, push the bottom of the board up until it completely comes out from the parallel guide of the front rails.

### 8. Tubing and power holes

To fully automate the control of the setup, lighting, odor/air delivery tubing and powering the optogenetic LEDs, some holes are needed to hold the powering platforms, cable connections and tubing.

![Holes_on_back_side_enclosure.PNG](/assets/Images/Holes_on_back_side_enclosure.PNG)
![Holes-on-back-side-enclosure-2.PNG](/assets/Images/Enclosure-back-side.PNG)

**The followings items are needed:**

* Open_screw_thread_neck_size_GL45_tubing_insertion_part_1of_2 [3D-Design](https://github.com/shaliulab/idoc_docs/blob/master/docs/assets/src/3D_printed_parts/Enclosure%26Powering/Holes_backside_enclosure/Tubing_hole/Open_screw_thread_neck_size_GL45_tubing_insertion_part_1of_2.stl)
* Open_topped_screw_cap_size_GL45_tubing_insertion_part_2_of_2 [3D-Design](https://github.com/shaliulab/idoc_docs/blob/master/docs/assets/src/3D_printed_parts/Enclosure%26Powering/Holes_backside_enclosure/Tubing_hole/Open_topped_screw_cap_size_GL45_tubing_insertion_part_2_of_2.stl)

* IDC_connector_RED_BLUE_LEDs+Indicators_LEFT_powering_panel_part_1_of_3 [3D-Design](https://github.com/shaliulab/idoc_docs/blob/master/docs/assets/src/3D_printed_parts/Enclosure%26Powering/Holes_backside_enclosure/Powering_panels/Bottom_left_panel/IDC_RED_BLUE_LEDs_IIndicators_LEFT_powering_panel_part_1_of_3.stl)
* Ouside_fixation_box_bottom_powering_panel_part_2_of_3 [3D-Design](https://github.com/shaliulab/idoc_docs/blob/master/docs/assets/src/3D_printed_parts/Enclosure%26Powering/Holes_backside_enclosure/Powering_panels/Bottom_left_panel/Ouside_fixation_box_bottom_powering_panel_part_2_of_3.stl)
* Outside_box_cover_bottom_powering_panel_part_3_of_3 [3D-Design](https://github.com/shaliulab/idoc_docs/blob/master/docs/assets/src/3D_printed_parts/Enclosure%26Powering/Holes_backside_enclosure/Powering_panels/Bottom_left_panel/Outside_box_cover_bottom_powering_panel_part_3_of_3.stl)

* IDC_connector_RED_BLUE_LEDs+setup_RIGHT_powering_panel_part_1_of_3 [3D-Design](https://github.com/shaliulab/idoc_docs/blob/master/docs/assets/src/3D_printed_parts/Enclosure%26Powering/Holes_backside_enclosure/Powering_panels/Bottom_right_panel/IDC_connector_RED_BLUE_LEDs%2Bsetup_RIGHT_powering_panel_part_1_of_3.stl)
* Ouside_fixation_box_bottom_powering_panel_part_2_of_3 [3D-Design](https://github.com/shaliulab/idoc_docs/blob/master/docs/assets/src/3D_printed_parts/Enclosure%26Powering/Holes_backside_enclosure/Powering_panels/Bottom_right_panel/Ouside_fixation_box_bottom_powering_panel_part_2_of_3.stl)
* Outside_box_cover_bottom_powering_panel_part_3_of_3 [3D-Design](https://github.com/shaliulab/idoc_docs/blob/master/docs/assets/src/3D_printed_parts/Enclosure%26Powering/Holes_backside_enclosure/Powering_panels/Bottom_right_panel/Outside_box_cover_bottom_powering_panel_part_3_of_3.stl)

* IDC_CONNECTOR_GREEN_LEDs_top_powering_panel_part_1_of_3 [3D-Design](https://github.com/shaliulab/idoc_docs/blob/master/docs/assets/src/3D_printed_parts/Enclosure%26Powering/Holes_backside_enclosure/Powering_panels/Top_right_and_left_panel/IDC_CONNECTOR_GREEN_LEDs_top_powering_panel_part_1_of_3.stl)
* Ouside_fixation_box_top_powering_panel_part_2_of_3 [3D-Design](https://github.com/shaliulab/idoc_docs/blob/master/docs/assets/src/3D_printed_parts/Enclosure%26Powering/Holes_backside_enclosure/Powering_panels/Top_right_and_left_panel/Ouside_fixation_box_top_powering_panel_part_2_of_3.stl)
* Outside_box_cover_top_powering_panel__part_1_of_3 [3D-Design](https://github.com/shaliulab/idoc_docs/blob/master/docs/assets/src/3D_printed_parts/Enclosure%26Powering/Holes_backside_enclosure/Powering_panels/Top_right_and_left_panel/Outside_box_cover_top_powering_panel__part_1_of_3.stl)

* Black female banana connector (RS Component, [787-2338](https://benl.rs-online.com/web/p/banana-connectors/7872338) ; [738-474](https://benl.rs-online.com/web/p/banana-connectors/0738474/))
* Red 4mm Socket (RS Components; [738-480](https://benl.rs-online.com/web/p/banana-connectors/0738480/) ; [787-2332](https://benl.rs-online.com/web/p/banana-connectors/7872332/))
* Pencil
* Cutter
* Tape measure or ruler

**Tubing holes**

Tubes for odor delivery and suction access the setup through two holes in the bottom back of the enclosure. The holes are drilled carefully and a custom 3D-designed neck is fixed to protect the edges and prevent bendings.

![Tubing-holes.PNG](/assets/Images/Tubing-holes.PNG)
![tubing-insertion-assembly.PNG](/assets/Images/tubing-insertion-assembly.PNG)

**Procedure**

1. Use a pencil and a round ring to precisely mark two holes in each side of the bottom of the back wall so the tubing can be inserted inside the enclosure.
2. Cut all the way through the board following the pencil lines. The blackboard is soft, so proceed carefully. A 44 mm hole saw drill can be useful. Be careful not to injure your fingers.
3. Remove the cuts and trim the rough edges of the black hardboard.
4. Insert the threaded neck part (3D printed) from the inside, attach the open cap part from outside, and then tighten the cap until the assembly is held firmly to the board.

**Power holes**

We also need to connect the LED drivers for optogenetics manipulation; and the Arduino controller to power the setup and deliver the electric shocks and IR illumination. We achieved this by designing a custom 3D-printed panel that bridges connections with male and female IDC wires.

![Bottom-powering-window.PNG](/assets/Images/Bottom-powering-window.PNG)
![Ouside_wire_box_cover_bottom.PNG](/assets/Images/Ouside_fixation_frame_bottom.PNG)

**Procedure**

1. Use a pencil and 3D-printed square to precisely mark two windows in each side of the bottom of the back wall so the IDC connectors of the setup and optogenetic panel can be powered.
2. The two windows are approximately 5 cm from the bottom of the enclosure. Space these holes about 6 cm apart.
3. Cut all the way through the board following the pencil lines.
4. Remove the cuts and trim the rough edges of the black hardboard.
5. Insert the left and the right powering platform from the inside into the cut area. Attach the fixation wall from outside.
6. Use screwdriver to fasten the panel with M2 screw, tighten the screw until the assembly is held firmly to the board. The powering stages should fit exactly so that they have no light or air leakage.

## [Baseplate](https://reiserlab.github.io/Component-Designs/miscellaneous/baseplate)

A solid black aluminum baseplate with threaded mounting holes provides a convenient platform for mounting the setup enclosure and other components. The plate should be bigger than the setup base, i.e, larger in both length and width. To isolate the setup from the light and airflow coming from the threaded mounting holes in the baseplate, attach a [black hardboard](https://www.thorlabs.de/newgrouppage9.cfm?objectgroup_id=190#2535) panel to the bottom of the baseplate. You can mount it with four Sorbothane feet (Thorlabs, [AV5/M](https://www.thorlabs.com/thorproduct.cfm?partnumber=AV5/M)). These Sorbothane mounting feet also offer excellent isolation from vibration and possible acoustic noise. The parts needed are provided in the figure below:

![Baseplate-rubber-feet.PNG](/assets/Images/Baseplate-rubber-feet.PNG)
![Baseplate.PNG](/assets/Images/Baseplate.PNG)


### Baseplate assembly procedure

**Construct the baseplate in the following manner:**

1. Insert a [black hardboard](https://www.thorlabs.de/newgrouppage9.cfm?objectgroup_id=190#2535) panel below the aluminum breadboard at the bottom side,

2. Inset four (M6) cap screws in the counterbored holes at each corner of the breadboard,

3. Press the (M6) screw to create holes into the [black hardboard](https://www.thorlabs.de/newgrouppage9.cfm?objectgroup_id=190#2535). If necessary, hand drill may be useful at this step.

4. Attach the threaded hole of [vibration isolation feet](https://www.thorlabs.de/newgrouppage9.cfm?objectgroup_ID=6421) to each screw at the corner of the breadboard.

5. Tighten each screw down with the [balldriver or hex key](https://www.thorlabs.de/newgrouppage9.cfm?objectgroup_id=1407).

6. Trim the extra edges of the [black hardboard](https://www.thorlabs.de/newgrouppage9.cfm?objectgroup_id=190#2535) to be exactly aligned to the breadboard. When cutting, be careful not to injury your fingers.

7. Place the baseplate horizontally on the rubber feet to be ready when connecting the assembled enclosure.

### Enclosure mount procedure

The enclosure is attached directly to the baseplate using the [XE25CL2 Clamp](https://www.thorlabs.com/thorproduct.cfm?partnumber=XE25CL2) to mount a 25 mm rail horizontally to a M6 tapped surface by using a side-located rail channel.

![Baseplate-enclosure-mount.PNG](/assets/Images/Baseplate-enclosure-mount.PNG)
![IDOC-baseplate-brackets-connection.PNG](/assets/Images/IDOC-baseplate-brackets-connection.PNG)
![IDOC-baseplate-brackets-connection-cut.PNG](/assets/Images/IDOC-baseplate-brackets-connection-cut.PNG)

1. Put the assembled enclosure on top of the assembled baseplate
2. Align and center the enclosure on the baseplate by mount bottom rails horizontally on breadboard
3. Slot the [XE25CL2 clamp](https://www.thorlabs.com/thorproduct.cfm?partnumber=XE25CL2) into the horizontal rail channel to secure it parallel to the bbaseplate surface,
4. Inset M6 screw in the clamp's long clearance slot
5. Move the clamps to the corners of the enclosure and tighten down with the [balldriver or hex key](https://www.thorlabs.de/newgrouppage9.cfm?objectgroup_id=1407).