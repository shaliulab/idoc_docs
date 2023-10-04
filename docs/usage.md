Usage
# **Running an IDOC experiment**

This section will provide you with the necessary steps for running an IDOC experiment. There are a variety of experiment designs that can be used, of which the main 3 will be covered here. However, many of these steps can be modified to accommodate other protocols or added steps, should you wish to customize certain parameters.

**Odour preparation**


**IDOC Start-up protocol**
This section will guide you through the first set-up steps required to make sure the machine is running properly. Ideally follow this section first, as most possible issues with your experiment can already be identified here.

* Power on the machine and verify that all the PSUs are providing the expected voltages

* Verify camera and IR light functionality
    * Activate the IR light via the switch on the relay control box
    * Use the Basler camera software on your PC to connect to the camera and activate a live feed. You should see a grayscale image with all the IDOC ROIs and the 3 tracking dots clearly illuminated. Make sure there is no image tearing or any artefacts. 
        * If image tearing/artefacts show up, you will need to plug-and-unplug the camera from the PC. Pay special attention to how stable the USB connection is (connector not wobbling in socket).

* Verify proper functionality of air/odour delivery system
    * Check whether the water level in the air washing and warming section is sufficient. The air washing bottle should have roughly 600ml of water, and the water bath should have enough to submerge most of the washing bottle in.
    * IMPORTANT! Check that the 3-way stopcock is positioned to allow for air/odour delivery and that the passive airflow is blocked
    * Connect your mineral oil and odour bottles to their respective in-/out-flow tubes. Make sure the air inflow into the bottles is directed into the oil (air needs to bubble through the oil). If done wrong, you can end up pumping oils into the airflow system of the IDOC!
    * Activate both the main air supply and the vacuum pumps from the relay control panel, and check the following:
        * Air inflow rates for both left and right side should be matching. Make any necessary adjustments at the inflow manifold
        * Air inflow and vacuumed outflow rates should be matching
        * Flow rates for odour and clean air should be equal. To check this, activate odour flow from the relay control panel for just one of the sides (left/right) and see if the flow rates match for both channels. Repeat this process for both channels. If flow rates become unequal when switching to odour, you will have to check the flow path for leaks or blockages.
            * Make sure all luers and bottle caps are tight
            * Verify the state of the tubing. Make sure there are no points of blockage (tight bends, debris, weight on tubing) or leakage. You can check for the latter by squeezing the tube shut. If the inflow rate does not go to 0 when you do this, then there is a leak between the odour bottle and crimp point.
    * Finish up by turning off the airflow and vacuum from the relay control panel

* Start up the IDOC logs on your control PC and make sure there are no error messages in the logs.

**Experimental protocol**
The first part of this section will highlight the basics of running an experiment. The end of this section will also demonstrate an example training protocol we have used to establish long term memory in flies.

* Transfer your flies into their respective IDOC chambers and close it with the L-shaped plug. Note that if you don't have enough flies to fill out all 20 chambers/ROIs, you should still set up chambers for those empty slots, as otherwise the empty slots will leak odour into the enclosure.

* Load the chambers into the enclosure. If you are using ITO chambers for experiments with electroshock training, then pay special attention when slotting the connector pins into the clamps

* Connect all the inflow and outflow tubes to the chambers. Pay attention to 2 key things here:
    * Prevent the outflow tubes from blocking the chamber window, loop the tube around the neigbouring chambers outflow tube before connecting it to the outflow port. (Picture needed for this section)
    * Do not mix up left and right side inflow tubes. This is mainly just a risk in the middle of the enclosure, as there the L/R inflows can get crossed up

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
    * To be sure the stimuli are being provided as necessary, you should keep monitoring the video feed throughout the paradigms execution. Whenever a stimulus (odour or electroshock) is being applied, a corresponding light should switch on in the enclosure and show up on the video feed.

* Once the paradigm has finished running, you should see the timer stop and hear the airflow end. Remove your chambers from the enclosure and follow up with any steps your experimental design has intended for the flies.

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

----------------

## Testing
--------------

If you wish to test if your hardware is operative, we provide a convenience script available with the entrypoint `idoc_batch`
You can use this script to turn on any pin of the Arduino board interactively and watch whether it actually drives the equipment or not

```
idoc_batch --port /dev/ttyACM0 --pins 37 38 --value 1
```

will turn on pins 37 and 38 ON until the user kills the program (with Control-C)


```
idoc_batch --port /dev/ttyACM0 --pins 3 2 --value 0.5 --hertz 1
```

will turn on pins 10 and 11 with half intensity and 1 hertz of frequency


## Execution online

idoc consists of two modules: a server and a client.

* The server operates the hardware. It records the behavior of the animals and delivers the stimuli as commanded by the user's paradigm.
* The client interfaces the user and the server. It receives instructions from the user such as:

   * selection of a paradigm
   * turning on the camera for warm-up
   * starting the experiment
   * stopping the experiment

   and sends these instructions to the server

You can spawn the server as follows:

```
    (idoc) idoc-server --control --recognize --adaptation-time 0
```

this command launches the idoc server:

   * with the ``--control`` module active, so stimuli can be delivered to the animals during the recording
   * with the ``--recognize`` module active, so the behavioral response of the animal is registered by a video camera
   * ``--adaptation-time`` set to 0 means idoc will start the experiment right after the user presses start. Otherwise, it would wait that amount in seconds.


You can spawn the client as follows:

```
    (idoc) idoc-cli
```

You should always spawn the server first and then the client, because the latter attempts to connect to the former.
The idoc cli provides the following menu:

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
    11: QUIT
    Enter number: 
```


## Execution offline

If you wish to reanalyze a video, you can do so as follows:

1. Edit your config file in these places:

   * ``default_class.camera`` must be set to ``OpenCVCamera``
   * ``default_class.board`` must be set to ``ArduinoDummy``
   * ``io.camera.kwargs.video_path`` must be an absolute path pointing to your video

If your experiment cannot be analyzed because the targets are not found, please create a .yaml file with this format

```
    top_right: [981, 41]
    bottom_left: [262, 1000]
    bottom_right: [978, 997]
```
where the numbers are the X and Y coordinates of the 3 dots in any of the frames of the video
You can quickly extract them by opening one of the snapshots with GIMP and hovering the cursor over the target
GIMP will report the coordinates of the mouse.

Save and provide the absolute path to this file under
   
   * ``roi_builder.target_coord_file``


2. Restart the idoc program and run it as usual

