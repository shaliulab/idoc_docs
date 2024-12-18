# Usage and video tutorial

A run-through of a typical IDOC experiment can be seen in the following video.

<!-- Embed YouTube Video -->
<iframe width="560" height="315" src="https://www.youtube.com/embed/FIiZQTC73KY?si=Kp8FnGSLXkYTT4S-" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

This section will provide you with the necessary steps for running an IDOC experiment. The core principle for carrying out an IDOC run will remain the same, regardless of your experimental design. Variations between experimental plans will mainly depend on which paradigm you subject the flies to, and how you treat the flies between IDOC sessions.

## Odor preparation

For odor based conditioning, you will most likely need to custom-make your own odors. This section will describe how we have made our odors for our experiments, however there is a lot of room to customize parameters as needed. Our main 2 odorants are MCH and OCT and both are mixed with neutral mineral oil. Note that the described protocol will be for 2 bottles of odor, since a typical experiment will need 2 bottles of odor and 2 bottles of clean mineral oil. This is to ensure that both the left and right sides of the chamber can be provided with clean air or odor.

* Measure out 60 ml of mineral oil into a bottle. Note that the mineral oil is quite heavy and thus the measured amount will need some extra time to fully drip out of the pippete.
* Add the odorant volume required to achieve the desired concentration. Concentrations can be determined with a calibration curve that shows the untrained preference at different concentrations (acuity test). You will typically choose the concentration that maximizes untrained neutrality. In our hands, OCT works well at 1:500, so 120 ul in 60 ml would produce that dilution.  
* Seal the bottle with a cap suitable for bubbling the mixture (has 2 air nozzles, with 1 that can be submerged in the oil-odor mixture). Connect the bottle to a bubbler and let it run for roughly 1-2 minutes to properly mix the solution.
* Once thoroughly mixed, divide the 60 ml of odorized mineral oil into 2x30 ml portions.
* Fill the mineral oil bottles with 30 ml each of oil.

## Writing a paradigm

See [the section](/installation/#paradigm) in the installation page.

## IDOC Start-up protocol

This section will guide you through the first set-up steps required to make sure the machine is running properly. Ideally follow this section first, as most possible issues with your experiment can already be identified here.

* Power on the machine and verify that all the PSUs are providing the expected voltages.

* Verify camera and IR light functionality.
    * Activate the IR light via the switch on the relay control box.
    * Use the Pylon camera software on your PC to connect to the camera and activate a live feed. You should see a grayscale image with all the IDOC ROIs and the 3 tracking dots clearly illuminated. Make sure there is no image tearing or any artefacts.
        * If image tearing/artefacts show up, you will need to plug-and-unplug the camera from the PC. Pay special attention to how stable the USB connection is (connector not wobbling in socket).
* Verify proper functionality of air/odor delivery system.
    * Check whether the water level in the air washing and warming section is sufficient. The air washing bottle should have roughly 600ml of water, and the water bath should have enough to submerge most of the washing bottle in.

    * IMPORTANT! Inside the enclosure, check that the 3-way stopcock is positioned to allow for air/odor delivery and that the passive airflow is blocked. The figure below shows how the stopcock should be positioned (red paths denote air/odor flow, blue denotes passive airflow).

    ![odor_flow_annotated.png](./assets/Images/odor_flow_annotated.png)

    * Connect your mineral oil and odor bottles to their respective in-/out-flow tubes. Make sure the air inflow into the bottles is directed into the oil (air needs to bubble through the oil). If done wrong, you can end up pumping oils into the airflow system of the IDOC!
    * Activate both the main air supply and the vacuum pumps from the relay control panel, and check the following:
        * Air inflow rates for both left and right side should be matching and similar to the outflow rate. Make any necessary adjustments at the inflow manifold.
        * Flow rates for odor and clean air should be equal. To check this, activate odor flow from the relay control panel for just one of the sides (left/right) and see if the flow rates match for both channels. Repeat this process for both channels. If flow rates become unequal when switching to odor, you will have to check the flow path for leaks or blockages.
            * Make sure all luers and bottle caps are tight.
            * Verify the state of the tubing. Make sure there are no points of blockage (tight bends, debris, weight on tubing) or leakage. You can check for leaks by squeezing the tube shut. If the inflow rate does not go to 0 when you do this, then there is a leak between the odor bottle and your crimp point.
    * Finish up by turning off the airflow and vacuum from the relay control panel.
* Start up the IDOC logs on your control PC and make sure there are no error messages in the logs.

## Experimental protocol

The first part of this section will highlight the basics of running an experiment. The end of this section will also demonstrate an example training protocol we have used to establish long-term memory in flies.

* Transfer your flies into their respective IDOC chambers and close it with the L-shaped plug. Note that if you don't have enough flies to fill out all 20 chambers/ROIs, you should still set up chambers for those empty slots, as otherwise the empty slots will leak odor into the enclosure. Not only that, since the path of least resistance would then be through the unoccupied slots, the delivery of odor to the loaded chambers will be irregular or unpredictable.
* Load the chambers into the enclosure. If you are using ITO chambers for experiments with electroshock training, then pay special attention when slotting the connector pins into the clamps
* Connect all the inflow and outflow tubes to the chambers. Pay attention to 2 key things here:
    * Prevent the outflow tubes from blocking the chamber window, loop the tube around the neigbouring chambers outflow tube before connecting it to the outflow port. (Picture needed for this section)
    * Do not mix up left and right side inflow tubes. This is mainly just a risk in the middle of the enclosure, as there the right inflows of the left side can get crossed up with the left inflows of the right side.

<!-- Embed YouTube Video -->
<iframe width="560" height="315" src="https://www.youtube.com/embed/FIiZQTC73KY?si=Kp8FnGSLXkYTT4S-&start=165" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

*The above video should highlight the process of loading the flies into their respective chambers, and how those in turn get loaded into the IDOC system. In case the video doesn't jump to the correct timestamps, the fly loading can be seen at 2:45 and the chamber loading seen at 6:53.*


* Cover up the front of the enclosure when done loading the chambers.

* Open up the IDOC client on your working PC by running

```
idoc_cli
```

![](./assets/Images/idoc_cli.jpg)

NOTE: In the image above we have split the terminal, so the right half shows the logs of idoc. You can read them too by running

```
journalctl -fu idoc_server
```

You should see the following menu:

```
    Connecting to IDOC device in machine 74f75f830109411ba67f74ecb268f9ef
    Please choose:
    1: LOAD PARADIGM
    2: CHANGE CONFIGURATION
    3: WARM UP
    4: CHECK
    5: START
    6: STOP
    7: CLEAR
    8: PROMPT
    9: EXPORT
    10: RESTART
    Enter number:
```

* Select your desired experimental paradigm with "Load paradigm" by pressing `1`.

![](./assets/Images/idoc_cli-menu-1.jpg)


Select your desired paradigm, in the video we selected number `7`, so we enter 7 in the interface.


![](./assets/Images/idoc_cli-menu-7.jpg)


follow with "Warm up" by pressing `3` and wait for a live feed of the enclosure to open
 
![](./assets/Images/idoc_cli-menu-3.jpg)


![](./assets/Images/idoc-live-feed.jpg)


Make sure you give enough time for all the flies to be picked up by the tracking software. If the flies are not moving and not getting detected by the tracking software, then activate the vibrator for short bursts until they move again. You should also verify that the 3 reference dots for tracking are clearly visible in the video feed. Refer to the figure below to see where they should be visible


* Select "Start" to start the paradigm by pressing `5`.

![](./assets/Images/idoc_cli-menu-5.jpg)


Make sure that the timer in the video feed actually starts, since sometimes the experiment can fail to start despite giving the command.  If this happens then select "Stop", followed by "Restart". Then simply repeat the paradigm selection process and start the experiment again.

![](./assets/Images/idoc_cli-started.jpg)

* To be sure the stimuli are being provided as necessary, you should keep monitoring the video feed throughout the paradigm's execution. Whenever a stimulus (odor or electroshock) is being applied, a corresponding light should switch on in the enclosure and show up on the video feed (which is also useful when you later playback the recording so that you can temporally match the behavior recorded in the video with the stimuli delivered).
* Once the paradigm has finished running, you should see the timer stop and hear the airflow end. Remove your chambers from the enclosure and follow up with any steps your experimental design has intended for the flies.
* Remove the flies from their chambers ASAP, since they are constantly making the chambers dirtier, leading to you needing more frequent cleaning sessions.

<!-- Embed YouTube Video -->
<iframe width="560" height="315" src="https://www.youtube.com/embed/FIiZQTC73KY?si=Kp8FnGSLXkYTT4S-&start=609" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

*The above video should illustrate the steps needed to start the experiment once all your chambers have been loaded into the IDOC system. All the relevant markers that you can use to verify that the system is working as intended are also shown. In case the video doesn't jump to the correct timestamps, the process of choosing and activating the paradigms starts at 10:08 in the video*



**Example training experiment**

* Pre-test to establish the flies baseline preference for odor vs. no odor
    * Load flies into non-ITO chambers and run them through a paradigm where they are exposed to odors from both left and right sides of their chambers separately
* Training sessions with electroshock
    * Transfer your flies from the non-ITO chambers into the ITO chambers and load them into the enclosure
    * Run a paradigm where the flies are exposed to odors from both sides of the chamber simultaneously while also receiving electroshocks
    * Once a single run of the paradigm ends, remove the flies from the chambers and place them in isolated tubes where they can have a short break with food
    * Repeat the process of loading, shocking and letting the flies rest for a total of 6 times
    * Remove your flies from the chambers and load them into an ethoscope to monitor (and possibly disturb) their sleep
* Post-test to assess extent of learning
    * Repeat the steps done for the pre-test. Now the flies should be avoiding the side of the chamber where an odor is presented
