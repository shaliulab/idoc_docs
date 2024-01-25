# Usage and video tutorial

A run-through of a typical IDOC experiment can be seen in the following video.

<!-- Embed YouTube Video -->
<iframe width="560" height="315" src="https://www.youtube.com/embed/KCPsX5z7BI0?si=_qtdwb09p_fjraX_" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

This section will provide you with the necessary steps for running an IDOC experiment. The core principle for carrying out an IDOC run will remain the same, regardless of your experimental design. Variations between experimental plans will mainly depend on which paradigm you subject the flies to, and how you treat the flies between IDOC sessions.

## Odor preparation


## IDOC Start-up protocol


This section will guide you through the first set-up steps required to make sure the machine is running properly. Ideally follow this section first, as most possible issues with your experiment can already be identified here.

* Power on the machine and verify that all the PSUs are providing the expected voltages.

* Verify camera and IR light functionality
    * Activate the IR light via the switch on the relay control box 
    *Picture highlighting where the switch is*
    * Use the Pylon camera software on your PC to connect to the camera and activate a live feed. You should see a grayscale image with all the IDOC ROIs and the 3 tracking dots clearly illuminated. Make sure there is no image tearing or any artefacts. 
    *2 pictures - 1 for how to interpret the buttons in the Pylon software, 1 for an image of what to look for in the video feed, highlighting the dots*
        * If image tearing/artefacts show up, you will need to plug-and-unplug the camera from the PC. Pay special attention to how stable the USB connection is (connector not wobbling in socket).
* Verify proper functionality of air/odour delivery system
    * Check whether the water level in the air washing and warming section is sufficient. The air washing bottle should have roughly 600ml of water, and the water bath should have enough to submerge most of the washing bottle in.

    * IMPORTANT! Inside the enclosure, check that the 3-way stopcock is positioned to allow for air/odour delivery and that the passive airflow is blocked.
    * Connect your mineral oil and odour bottles to their respective in-/out-flow tubes. Make sure the air inflow into the bottles is directed into the oil (air needs to bubble through the oil). If done wrong, you can end up pumping oils into the airflow system of the IDOC!
    * IMPORTANT! Check that the 3-way stopcock is positioned to allow for air/odour delivery and that the passive airflow is blocked
    * Connect your mineral oil and odour bottles to their respective in-/out-flow tubes. Make sure the air inflow into the bottles is directed into the oil (air needs to bubble through the oil). If done wrong, you can end up pumping oil into the airflow system of IDOC!

    * Activate both the main air supply and the vacuum pumps from the relay control panel, and check the following:
        * Air inflow rates for both left and right side should be matching. Make any necessary adjustments at the inflow manifold
        * Air inflow and vacuumed outflow rates should be matching.
        * Flow rates for odour and clean air should be equal. To check this, activate odour flow from the relay control panel for just one of the sides (left/right) and see if the flow rates match for both channels. Repeat this process for both channels. If flow rates become unequal when switching to odour, you will have to check the flow path for leaks or blockages.

            * Make sure all luers and bottle caps are tight
            * Verify the state of the tubing. Make sure there are no points of blockage (tight bends, debris, weight on tubing) or leakage. You can check for leaks by squeezing the tube shut. If the inflow rate does not go to 0 when you do this, then there is a leak between the odour bottle and your crimp point.
    * Finish up by turning off the airflow and vacuum from the relay control panel
    
*Video - First scene checking the air washing stage: look at temp and water levels. Second scene to highlight us turning the valve inside the enclosure and pointing out which way it needs to be with edits. Third scene to point out us switching on the relevant valves, followed by us pointing out the matching levels on the flowmeters*


<!-- Embed YouTube Video -->
<iframe width="560" height="315" src="https://www.youtube.com/embed/VIDEOID" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


* Start up the IDOC logs on your control PC and make sure there are no error messages in the logs.

## Experimental protocol

The first part of this section will highlight the basics of running an experiment. The end of this section will also demonstrate an example training protocol we have used to establish long-term memory in flies.

* Transfer your flies into their respective IDOC chambers and close it with the L-shaped plug. Note that if you don't have enough flies to fill out all 20 chambers/ROIs, you should still set up chambers for those empty slots, as otherwise the empty slots will leak odour into the enclosure.
* Load the chambers into the enclosure. If you are using ITO chambers for experiments with electroshock training, then pay special attention when slotting the connector pins into the clamps
* Connect all the inflow and outflow tubes to the chambers. Pay attention to 2 key things here:
    * Prevent the outflow tubes from blocking the chamber window, loop the tube around the neigbouring chambers outflow tube before connecting it to the outflow port. (Picture needed for this section)
    * Do not mix up left and right side inflow tubes. This is mainly just a risk in the middle of the enclosure, as there the L/R inflows can get crossed up

<!-- Embed YouTube Video -->
<iframe width="560" height="315" src="https://www.youtube.com/embed/KCPsX5z7BI0?si=_qtdwb09p_fjraX_&start=165" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

*Video - Show us loading flies into chambers, and sealing the chamber shut with the plug. Show a stack of 10 chambers with loaded flies and how we would load them into the chamber slots in the machine. Emphasize in the video that since we only have 10 flies, we still need to fill out the other empty slots with empty chambers. Show us connecting the tubes, emphasize that you need to distinguish between left and right inflow, especially in the middle of the machine.*


* Cover up the front of the enclosure when done loading the chambers.

* Open up the IDOC client on your working PC, you should see the following menu:

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
* Select your desired experimental paradigm with "Load paradigm". Once locked in, follow up with "Warm up" and wait for a live feed of the enclosure to open. Make sure you give enough time for all the flies to be picked up by the tracking software. If the flies are not moving and not getting detected by the tracking software, then activate the vibrator module for short bursts until they move again.

* Select "Start" to start the paradigm. Make sure that the timer in the video feed actually starts, since sometimes the experiment can fail to start despite giving the command. If this happens then select "Stop", followed by "Restart". Then simply repeat the paradigm selection process and start the experiment again.
    * To be sure the stimuli are being provided as necessary, you should keep monitoring the video feed throughout the paradigm's execution. Whenever a stimulus (odour or electroshock) is being applied, a corresponding light should switch on in the enclosure and show up on the video feed.
* Once the paradigm has finished running, you should see the timer stop and hear the airflow end. Remove your chambers from the enclosure and follow up with any steps your experimental design has intended for the flies.

<!-- Embed YouTube Video -->
<iframe width="560" height="315" src="https://www.youtube.com/embed/KCPsX5z7BI0?si=_qtdwb09p_fjraX_&start=635" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

*Video - Scene where we go through selecting a paradigm and hitting "Start". Show the expected video feed.Emphasize us checking the timer in the video feed + looking for the EShock or odour LEDs (A or B indicators). Follow up with quick scene of chambers being disconnected from tubing and being removed from enclosure. Final scene of how to remove flies. For trying to preserve flies, show the sucking method + tube method where they walk out by themselves. For discarding flies, simply show the vacuum pump method.*



**Example training experiment**

* Pre-test to establish the flies baseline preference for odour vs. no odour
    * Load flies into non-ITO chambers and run them through a paradigm where they are exposed to odours from both left and right sides of their chambers separately
* Training sessions with electroshock
    * Transfer your flies from the non-ITO chambers into the ITO chambers and load them into the enclosure
    * Run a paradigm where the flies are exposed to odours from both sides of the chamber simultaneously while also receiving electroshocks
    * Once a single run of the paradigm ends, remove the flies from the chambers and place them in isolated tubes where they can have a short break with food
    * Repeat the process of loading, shocking and letting the flies rest for a total of 6 times
    * Remove your flies from the chambers and load them into an ethoscope to monitor (and possibly disturb) their sleep
* Post-test to assess extent of learning
    * Repeat the steps done for the pre-test. Now the flies should be avoiding the side of the chamber where an odour is presented
