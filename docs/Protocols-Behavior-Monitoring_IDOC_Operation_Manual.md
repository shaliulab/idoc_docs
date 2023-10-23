# **Behavior-Monitoring_IDOC_Operation**

** **


  ### **Start of an experiment in IDOC**

  ​

  1. Prepare the experimental flies as described above.

  ​

  ![Preparing_the_experimental_flies .PNG](assets/Images/Preparing_the_experimental_flies .PNG)


  ​                                                                  Suggested plan for long term memory experiment

  ​

  2. **Checklist** before  starting your experiments :

  - [ ] Turn on Main Power and Check the water level in water bath.

  - [ ] Balanced airflow (inflow & outflow) see photo, adjust flow regulators while no air connected to the manifolds of the setup before you connect the chambers, then double check after connecting chambers to the inflow and outflow system.

  - [ ] Mineral oil and Odor bottles are in the correct places and connected properly and  with no leakage. check That all leur all locked and connected correctly as mapped with color coded tubes.  [Blue marker --> odor A] &  [Red markers --> odor B] &  [black markers --> Air).

  - [ ] If you cleaned the setup be sure the there is no remaining water in the setup or odor delivery system (use air-gun to remove remaining water in all tubing).  this can lead to unbalance chambers

  - [ ] for spaced training; be sure to spray the cotton/yarn with water, and remove the excessive water to close the food tubes between training sessions.

  - [ ] Main Power supply of the solenoid valves and infrared is ON and connected to the controller board (12.00 VDC).

  - [ ] Electric shock power supply is ON and connected to the controller board (75.00 VDC). Switch to current mode mA Check that the current is (000), if you read any value that means that the circuit is ON. Check the relay board

  - [ ] Red LEDs (627 nm) power supply is ON and connected to the controller board  (this is critical step) be sure that the power supply set to the maximum voltage of the power supply all of the current limited and light intensity were  calibrated at the maximum power from the power supply. even minor change will change the total power delivered to the power supply.

        e.g. 

        $input.voltage = 31.3 V  $

        $Current.needed = 7 A$

        $Total.power =  VxA = 31.3x3.5 = 219.1W $

        if the input voltage changed to less amount for example 25V the total power then will be drifted to 175 watt  this power can change the light intensity few  micro watts which can affect the behavior of the fly.

        ​

  - [ ] Check Air/odor solenoid valves via test buttons or switch while no air is running from the main valve.   

  - [ ] Exhaust system is working properly to avoid pressure in the tubing and to remove any extra odor after stopping odor delivery.

  - [ ] Arduino is connected (ON LED on board)

  - [ ] Camera is connected, and you can see images in Pylon software

  - [ ] Paradigm is ready and pre tested especially for new protocols. The software is online communication 

  - [ ] When ready and all of the above list  checked , switch from continuous air flow of the air cleaning system to air/odor delivery system controlled by the Arduino   ---> must switch the manual valves [4-way Stopcock] to deliver air and odors to the IDOC setup. (see diagram) (critical step). if you forgot to change the valves first no odors will be delivered to the chambers when you run your protocol. Additionally the cleaned air is running with higher air flow than the inflow controlled by the  air/odor delivery system. accumulate the air in the pressure while no vacuum running to suck the air will generate a pressure on the vacuum system leading to reverse back of the water into the vacuum tubing. so it is necessary to switch to 




3. Use aspiration tubes to gently suck the fly to the inlet gate of the recording chamber. Loading female fly (ZT 2-4) into chamber. When Loading the fly, pick up the flies that can fly to the top of food vial.
4. Mount chambers to their recessed place in the chamber holders of the setup.
5. Secure the chambers and  check the connection of the electric shock electrodes 
6. Connect inflow tubing to the chambers, tubing with red rings are connected to the right side while the blue rings connected to the left side.
7. We use active vacuum: connect the outlet tubing to the fitting luers of the suction system. bend the tubing by the way not block the visualization of the ROI during tracking.
8. Double Check the electric connection to ITO chambers via the lead cable. Connect the tip of the test lead to the end of each electrodes. you will see that the blue light target on the top of the light box is ON when good connection established while blinking or OFF if poor connection exist. 
9. Do not forget to return the toggle switch back to the bottom after checking the ITO electrodes connections. 
10. Double check that the 4-way Stopcock is directed to the inflow coming only from the air delivery system
11. Start an experiment  (software) see  software section
12. Spaced training requires moving trained flies to food tube between training sessions. After each  electric shock session, relocate the fly from chamber to sucrose plus retina tube with wet cotton/yarn. (better to spray the cotton/yarn with water, and remove the excessive water). Just keep flies for few minutes in the food tubes. Then reload the flies into the recording chambers and replace  the chamber on IDOC system. Connect all the tubing.
13. After training (e.g. 6 times electric shock), place the conditioned fly into a fresh sucrose tube with retina.
14. Put the fly into ethoscope arena and track sleep for 24 hours for long term memory testing
