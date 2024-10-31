# Camera enclosure

## Table of Contents

1. [Overview](#overview)
2. [Select the camera](#select-the-camera)
3. [Installation of base at the top of the enclosure](#installation-of-base-at-the-top-of-the-enclosure)
4. [Installation of mounting stage](#installation-of-mounting-stage)
5. [Attaching camera to the mounting stage](#attaching-the-camera-to-the-mounting-stage)
6. [Positioning and fixing the camera mounting stage](#positioning-and-fixing-the-camera-mounting-stage)
7. [Making the camera enclosure](#camera-enclosure-1)
    1. [Customizing the black harboard](#customize-the-black-hardboard)
    2. [Joining the rails and walls](#join-the-rails--build-the-walls-and-roof)
    3. [Mounting the camera enclosure](#mount-the-camera-enclosure)

## Overview

The IDOC system consists of a custom-built enclosure that holds a camera and allows it to be positioned in a precise location at the top of the IDOC chamber. After building the camera enclosure and mounting it, you must make sure it is  properly aligned for optimal monitoring of *Drosophila* behavior.

Building the IDOC enclosure camera mounting system involves several steps:

1.    Select a suitable camera for video tracking (ideally moderate framerate, monocolor, and connected via USB).
2.    Install a camera mounting bracket inside the enclosure, which allows the camera to be securely attached and positioned in the desired location.
3.    Install a camera onto the mounting bracket, ensuring that it is securely fastened and properly aligned.
4.    Connect the camera to the computer to enable live monitoring and recording of *Drosophila* behavior during experiments.
5.    Build the custom enclosure, which is typically made of optical posts, metal rails and hardboard, and is designed to be placed on the top of the setup enclosure to provide camera protection.

## Select the camera

We use two camera models from Basler to record the preference choices of the fly in two different setups. We recommend sticking to Basler, however, you can modify the code to support other providers (Flir, etc). Below you can find the specs of each camera and how we mounted them in our setups.

Please note, the oldest of the two cameras was discontinued by Basler at the time we built the second setup (2022).



**First setup model:**

|                 | Item                                     | Vendor                              |                                          |
| --------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| Camera model:   | [acA1280-60gm -  Basler ace](https://www.baslerweb.com/en/shop/aca1280-60gm)             | Basler | ![Basler_camera](/assets/Images/Commercial_Parts_Suppliers_Stock_Images/Basler_106486.jpg) |
| Lens:           | [Computar Lens M0814-MP2 F1.4 f8mm 2/3" - Lens](https://www.baslerweb.com/en/products/vision-components/lenses/computar-lens-m0814-mp2-f1-4-f8mm-2-3/#tab=specs) |  Basler | ![Basler_lens](/assets/Images/Commercial_Parts_Suppliers_Stock_Images/Basler-000034697.jpg) |
| Cable:          | [Basler Cable GigE,  Cat 6, RJ45 sl hor/RJ45, DrC, P, 5 m - Data Cable](https://www.baslerweb.com/en/products/vision-components/cable/basler-cable-gige-cat-6-rj45-sl-hor-rj45-drc-p-5-m/) | Basler | ![Basler_cable](/assets/Images/Commercial_Parts_Suppliers_Stock_Images/Basler-2000027038.jpg) |
| Mounting plate: | [Tripod Mount ace -  Camera Mount Adapter](https://www.baslerweb.com/en/products/vision-components/accessories-and-bundles/tripod-mount-ace/) | Basler | ![Basler_plate](/assets/Images/Commercial_Parts_Suppliers_Stock_Images/Basler-2000029679.jpg) |
| Power supply:   | [Power Supply  12V/18W, Hirose 6-pin - Power Supply](https://www.baslerweb.com/en/products/vision-components/network-and-peripheral-devices/power-supply-12v-18w-hirose-6-pin/) | Basler | ![Basler_power_supply](/assets/Images/Commercial_Parts_Suppliers_Stock_Images/Basler-2200000167.jpg) |


**Second setup model:**

|                 | Item                                     | Vendor                              |                                          |
| --------------- | ---------------------------------------- | ----------------------------------- | ---------------------------------------- |
| Camera model:   | [a2A2590-60umBAS -  Basler ace 2](https://www.baslerweb.com/en/products/cameras/area-scan-cameras/ace2/a2a2590-60umbas/) | Basler | ![Basler_camera2](/assets/Images/Commercial_Parts_Suppliers_Stock_Images/Basler-108028.jpg) |
| Lens:           | [Computar Lens M0814-MP2 F1.4 f8mm  2/3" - Lens](https://www.baslerweb.com/en/products/vision-components/lenses/computar-lens-m0814-mp2-f1-4-f8mm-2-3/) | Basler | ![Basler_lens](/assets/Images/Commercial_Parts_Suppliers_Stock_Images/Basler-000034697.jpg) |
| Cable:          | [Basler Cable USB  3.0, Micro B 90° A1 sl/A (ace downwards), P, 5 m - Data Cable](https://www.baslerweb.com/en/products/vision-components/cable/basler-cable-usb-3-0-micro-b-90-a1-sl-a-ace-downwards-p-5-m/)  | Basler | ![Basler_usb_cable](/assets/Images/Commercial_Parts_Suppliers_Stock_Images/Basler-2000035995.jpg) |
| Mounting plate: | [Tripod Mount ace2 -  Camera Mount Adapter](https://www.baslerweb.com/en/products/vision-components/accessories-and-bundles/tripod-mount-ace2/)  | Basler | ![Basler_plate](/assets/Images/Commercial_Parts_Suppliers_Stock_Images/Basler-2200000314.jpg) |
| Power supply:   | Via USB 3.0  interface  2.8 W            | Basler | |


The fly chambers are viewed from above by a camera equipped with a C-mount lens. The camera is placed on the top of the setup enclosure assembly to avoid [camera overheating](https://www.baslerweb.com/fp-1629376268/media/downloads/documents/application_notes/AW00171101000_How_Excessive_Temperatures_Affect_ace_2_Cameras_AppNote.pdf). Optical clamps, mounting base and metal posts from Thorlabs were used to fix the camera.

## Installation of base at the top of the enclosure

The post holder base is used for positioning and fastening the camera mount at the top of the enclosure. The post holders include a spring-loaded thumbscrew that holds posts in place before tightening

![Camera-mounting-base.PNG](/assets/Images/Camera-mounting-base.PNG)

The following parts are needed to create a base for the above camera mount construction:

- Ø12.7 mm Post Holder, Spring-Loaded Hex-Locking Thumbscrew, L=75 mm (Thorlabs, [PH75/M](https://www.thorlabs.com/thorproduct.cfm?partnumber=PH75/M)) (Q: 2x)

- M6 x 1.0 stainless steel cap screw, 10 mm Long (Thorlabs, [SH6MS10](https://www.thorlabs.com/thorproduct.cfm?partnumber=SH6MS10)) (Q: 2x)

- M6 x 1.0 stainless steel cap screw, 16 mm Long (Thorlabs, [SH6MS16](https://www.thorlabs.com/thorproduct.cfm?partnumber=SH6MS16)) (Q: 2x)

- Mounting Base, 25 mm x 58 mm x 10 mm (Thorlabs, [BA1S/M](https://www.thorlabs.com/thorproduct.cfm?partnumber=BA1S/M)) (Q: 2x)

- 5-mm balldriver or hex key.

### Procedure

1. Connect the post holder to a mounting base by inserting a 10-mm M6 screw through the bottom-located counterbores in the base.

2. Screw and tighten the M6 screw at the middle hole of the post holder using a 5-mm hex key, be sure the direction of the thumbscrew is in the outside face to facilitate and stabilize post mounting.

3. Attach one the assembled base post holder to the right 25-mm rail at the top of the setup enclosure.

4. Use 16-mm M6 screw and pre-slotted Low-Profile T-Nut (see step: [Build the enclosure roof](./Breadboard-Enclosure.md#3-build-the-enclosure-roof)) to establish and tighten base connection to the right rail.

5. Attach the other assembled base post holder to the left 25-mm rail at the top of the setup enclosure.

6. Use 16-mm M6 screw and pre-slotted Low-Profile T-Nut to establish and tighten the base connection to the left rail. Make sure that both right and left holders are aligned to the end of the IR-filter window.

## Installation of mounting stage

![Camera-mounting-base_2.PNG](/assets/Images/Camera-mounting-base_2.PNG)


**The following parts are needed to construct the camera mount:**

  * Ø12.7 mm Optical Post, SS, M4 Setscrew, M6 Tap, L = 300 mm (Thorlabs, [TR300/M](https://www.thorlabs.com/thorproduct.cfm?partnumber=TR300/M)) (Q: 2x)

 * Ø12.7 mm Optical Post, SS, M4 Setscrew, M6 Tap, L = 250 mm (Thorlabs, [TR250/M](https://www.thorlabs.com/thorproduct.cfm?partnumber=TR250/M)) (Q: 2x)

 * Ø12.7 mm Optical Post, SS, M4 Setscrew, M6 Tap, L = 100 mm (Thorlabs, [TR100/M-P5](https://www.thorlabs.com/thorproduct.cfm?partnumber=TR100/M-P5)). (Q: 3x)

 * Parallel Clamp for Ø1/2" Posts, M4 Counterbore and 5 mm Hex (Thorlabs, [RA360/M](https://www.thorlabs.com/thorproduct.cfm?partnumber=RA360/M)) (Q: 2x)

 * Right-Angle Clamp for Ø1/2" Posts, 5 mm Hex (Thorlabs, [RA90/M-P5](https://www.thorlabs.com/thorproduct.cfm?partnumber=RA90/M-P5)) (Q: 2x)

 * M4 x 0.7 stainless steel cap screw, 10 mm Long (Thorlabs, [SH4MS10](https://www.thorlabs.de/thorproduct.cfm?partnumber=sh4ms10)) (Q: 2x)

 * 2-mm balldriver or hex key.

 * 3-mm balldriver or hex key



**Procedure**

1.    Remove the M4 setscrew at the end of 100-mm posts using a 2-mm hex key.

2.    Connect the parallel clamp to 100-mm post by inserting a M4 screw at the middle hole of the clamp, screw it to the 100-mm post end.

3.    Connect 250-mm and 300-mm posts together to form one single long post, to do that add one M-6 setscrew at the end of the 250-mm, then attach the 300-mm post to the setscrew. Rotate both posts in different directions until they are well tightened.

4. Insert one right-angle clamp in each combined long post, move to the center.

5. connect each end of the combined post to the end of the parallel clamp.

6. Add 100-mm post in the middle of the combined posts to be clamped by the two right-angle clamps. This post is needed to fix the camera using M6- Setscrew at the base of the mounting plate of the camera.

7.    The mounting stage is ready to be mounted through the base at the top of the setup enclosure (see step), to do that; place the vertical 100-mm post of the above assembled stage at each post holder. The post holders include a spring-loaded thumbscrew that holds posts in the correct place before tightening.


## Attaching the camera to the mounting stage:

![Camera-mounting.PNG](/assets/Images/Camera-mounting.PNG)


**The following parts are needed to create a base for the above camera mount construction:**

 * Ø12.7 mm Optical Post, SS, M4 Setscrew, M6 Tap, L = 100 mm (Thorlabs, [TR100/M](https://www.thorlabs.com/thorproduct.cfm?partnumber=TR100/M)). (Q: 1x)

 * M6 x 1.0 Stainless Steel Setscrew, 10 mm Long (Thorlabs, [SS6MS10](https://www.thorlabs.com/thorproduct.cfm?partnumber=SS6MS10)). (Q: 1x)

 * Tripod Mount ace2 - Camera Mount Adapter (Mouser, [2200000314](https://www.mouser.be/ProductDetail/Basler/2200000314?qs=vmHwEFxEFR99K%252BV3Q%252B8cxw%3D%3D)) (Q: 1x)

 * M3 Stainless Steel screw, 10 mm Long (supplied with camera mount adaptor). (Q: 3x)

 * 2-mm balldriver or hex key.

 * 3-mm balldriver or hex key



**Procedure**

1.    Use a 2-mm hex key to secure three screws supplied with the camera mount to attach the camera to the mounting plate

2.    Insert M6 stainless steel setscrew into the middle hole of the camera mounting plate, screw it using a 3-mm hex key.

3.   Connect 100-mm optical post to the M6 setscrew at the middle of the mounting plate, rotate the post until establish a stable connection.

4.   Fix the assembled camera optical post to the middle parallel clamps of the assembled camera mounting stage.

5.   Be sure that the camera connection is stable and the lens facing the IR-sheet at the visualization window at the roof of the enclosure.

​
## Positioning and fixing the camera mounting stage

One of the challenges is finding the right camera position relative to the distance and the area that the camera will see. For that reason, a specific lens is needed to obtain optimum quality from the camera. Depending on our camera model and the recording setup, width (350 mm), length (400 mm), and working distance (700mm). For our purpose, a camera lens with about 8 focal length was selected. Since the focal length is determined by the distance between the lens and the inspected object, it is recommended to check what kind of lens is compatible with your camera using [Basler camera lens selector]( https://www.baslerweb.com/en/products/vision-components/lenses/)

Irregular installation position or improper angle of camera will result in tracking problems. So, as mentioned above camera position is important, so the mounting stage was designed in the way that provide XYZ axis translation movement when positioning the camera via optical components. After finding the proper height, use 5-mm hex key to full tighten all the screws of clamps and angles.


## Camera Enclosure


The camera enclosure placed on the top of the setup enclosure to provide minimum light exposure to the camera, because its sensor is so sensitive to the light and thereby can affect or stop the running experiments.

### Customize the [black hardboard](https://www.thorlabs.de/newgrouppage9.cfm?objectgroup_id=190#2535)

**The following supplies are needed:**

 * Black hardboard (Thorlabs, [TB4](https://www.thorlabs.de/newgrouppage9.cfm?objectgroup_id=190#2535))

 * Pencil

 * Cutter

 * Tape measure or ruler

 * Aluminum flat bar

Be sure that the correct size of the black board has been ordered or in house customized to fit the dimensions of the camera enclosure. Only TB4 blackboard is  used. The camera enclosure is not fully closed, the left and right walls are free.

Here is the final size:

· Vertical panels that form the front and back walls: 510-mm x 255-mm (L x W)

· The top panel that forms the roof of the enclosure: 510-mm to 255-mm (L x W)

![Black-board-camera-enclosure.PNG](/assets/Images/Black-board-camera-enclosure.PNG)



**Procedure**

1.   Using a tape measure mark a line by pencil on the face of black board to the correct size. Be sure that the final size is about 5 mm longer and 5 mm wider than the rail length to fit in the walls and the roof.

2.   Cut all the way through the board following the pencil lines. The blackboard is soft, so proceed carefully, aluminum flat bar can be used to keep straight cut. Be careful not to injury your fingers.

3.   Remove the cuts and trim the rough edges of the black hardboard.



##  Join the rails & build the walls and roof

**For this step, you will need:**

* Low-Profile Channel Screw (Q: 16x)

* Construction Cube with Slotted Corners (Q: 4x)

* 25-mm square construction rail 250-mm length (Q: 6x)

* 25-mm square construction rail 500-mm length (Q: 2x)

* Customized (510-mm x 255-mm) black hardboard (Q: 3x)

* Mounting base T-brackets; to connect camera enclosure to setup enclosure, [3D designed](https://github.com/shaliulab/idoc_docs/blob/master/docs/assets/src/3D_printed_parts/Enclosure%26Powering/25-mm_mounting_constructions/Mounting_base_T-brackets-vertical-rails-connecter.stl) (Q: 4x)

* 4-mm balldriver or hex key

![Camera-enclosure.PNG](/assets/Images/Camera-enclosure.PNG)



**Procedure**

1.   Attach low-profile channel screw to a construction cube. Then, push the screw into the threaded hole in the end of each 500-mm rail and tighten both screws down with the balldriver to connect the two rails.

2.   Repeat the above step for the other corner to connect a second construction cube from the other end.

3.   Connect 250-mm rail to each construction cube, by inserting the screw into the threaded hole in the end of each rail and tighten both screws down with the balldriver to connect the 500-mm rail

4.   Repeat the above step for the other corner to connect the other 250-mm rail and form U-Shaped-frame.

5.   Slide the black hardboard (255-mm x 510-mm) into the channel of the U-shaped frame rails.

6.   Connect the fourth rail by placing another channel screw into the hole of construction cube, then insert it into the threaded hole in the end of the rail and tighten screws down with the balldriver to form the horizontal top rectangle.

7.   Attach low-profile channel screw to the third hole of each construction cube to connect the vertical rails. Push the screw into the threaded hole in the end of each rail and tighten screws down with the balldriver to connect the four rails.

8.   Slide the black hardboard (255-mm x 510-mm) into the channels of the front and back rails.

9.   Attach the 3D-printed elbow T-bracket at each end of the vertical rails, by the way the counterbored holes of the connectors are outside of the enclosure then fasten the vertical 25 mm rails to brackets using a T-Nut and low-profile channel screw.



## Mount the camera enclosure

 ![Camera-mounting-base.PNG](/assets/Images/Camera-mounting-base.PNG)


**Procedure**

1.   After installation, mounting and adjust the camera. Move the camera enclosure to the top of the setup enclosure to protect the camera.

2.   Attach a low-profile channel screw to the outside part of each corner bracket.

3.   To assemble both enclosures, insert the screws into the brackets and loosely thread them into preinserted T-nuts on rail channels. Then tighten them down with the balldriver to create a stable connection.