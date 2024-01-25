
## Testing

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
