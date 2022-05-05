
.. _installation:

Installation
--------------

To use idoc we recommend creating a conda environment. Please install anaconda or miniconda and proceed as follows.


1. Create a conda environoment
================================

.. code-block:: console

    conda create --name idoc python=3.8.10



This will install from source the version of the module available under the git hash commit ``1cbda303a0ab0d335c82f0460e71c0cc5c12bbeb``. This version was verified in Ubuntu 20.04.3 with Python 3.7.4

2. Install idoc
================================

.. code-block:: console

    pip install idoc


3. Set minimal configuration
================================

The configuration is by default installed to ``$HOME/.config/idoc/idoc.yaml`` in YAML format.
Once idoc is installed, this file should be created. You need to update the following fields


1. `folders.results.path`: Path to a directory where the data from the new experiments will be saved
2. `folders.paradigms.path`: Path to a directory containing at least one paradigm .csv file
3. `controller.mapping_path`: Path to a directory containing at least one mapping .csv file
4. `controller.paradigm_path`: Filename of a .csv file available under the `folders.paradigms.path`

A valid mapping would look like this:

::

  hardware,pin_number
  IRLED,45
  LED_R_LEFT,3
  LED_R_RIGHT,2

so there are two columns called **hardware** and **pin_number**.

* The pin number corresponds to the number written on the GPIO of the Arduino board you use.
* The hardware column should contain a user-friendly name you give to this hardware. No spaces are allowed!

A valid paradigm would look like this

::

  hardware,start,end,on,off,mode,value
  IRLED,0,5,NaN,NaN,o,1
  LED_R_LEFT,1,2,1,1,o,1
  LED_R_RIGHT,1,2,1,1,o,1


* We again have the hardware column, which should contain the same set of names you used in the hardware column of your mapping.
* **start** and **end** show the moment when the hardware will start and end its duty, in minutes since experiment start.
* **on** and **off** are the number of seconds the hardware should be on and off, if it should cycle during its duty. If no cycle is needed, leave NaN.
* **mode** must be either ``o``/``p`` where ``o`` is the default and ``p`` is if you want to use PWM, which allows you to modulate the output of the hardware (say light intensity).
    In that case, the hardware must be connected to a PWM supporting pin (see the board specs).
* **value** must be 1 everytime **mode** is ``o`` and between 0 and 1 if **mode** is set to ``p``.

### Example of a paradigm: the warm_up

This is the paradigm selected by default upon installation of idoc

::

    hardware,start,end,on,off,mode,value
    MAIN_VALVE,0,5,NaN,NaN,o,1
    VACUUM,0,5,NaN,NaN,o,1
    IRLED,0,5,NaN,NaN,o,1
    TARGETS,0,.2,NaN,NaN,o,1
    ONBOARD_LED,0,5,500,500,o,1


**Please note:**

idoc needs the paradigm and mapping passed in the config to be available at boot.
Therefore, you need to make sure the file listed in the config under:


* ``controller.paradigm_path`` exists in the directory under ``folders.paradigms.path``.
* ``controller.mapping_path`` exists in the directory under ``folders.mappings.path``.

5. Create  machine_name
============================

Linux users need to make sure the contents of `$HOME/.config/idoc/machine_name` have the name they want their machine to have, for example `IDOC_001`.
If this file does not exist, it must be created as plain text file with no extensions.
This will set the name of the folder under which all experiments will be saved.


6. Configure logs
========================

You must have a file called `$HOME/.config/idoc/logging.yaml` with the following content:

::

    version: 1
    disable_existing_loggers: true
    formatters:
    simple:
        format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    handlers:
    console:
        class: logging.StreamHandler
        level: DEBUG
        formatter: simple
        stream: ext://sys.stdout
    loggers:
    idoc:
        level: WARNING 
        handlers: [console]
        propagate: no


You can optionally adjust the logging level of the idoc modules by adding more loggers, like so

::

    version: 1
    disable_existing_loggers: true
    formatters:
    simple:
        format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    handlers:
    console:
        class: logging.StreamHandler
        level: DEBUG
        formatter: simple
        stream: ext://sys.stdout
    loggers:
    idoc:
        level: WARNING 
        handlers: [console]
        propagate: no
    idoc.server.core.recognizer:
        level: INFO 
        handlers: [console]
        propagate: no
    idoc.server.controllers.controllers:
        level: INFO 
        handlers: [console]
        propagate: no
    idoc.server.roi_builders.target_roi_builder:
        level: INFO 
        handlers: [console]
        propagate: no



6. Install systemd service
=====================================

We recommend running the idoc_server as a service that is always spawned in the background.
This is achieved with a systemd service file, which must be placed under `/etc/system/systemd/idoc_server.service`

::

    [Unit]
    Description=IDOC Server
    Wants=ntpd.service
    After=ntpd.service


    [Service]
    Type=simple
    Environment="HOME=/root"
    ExecStart=/home/vibflysleep/miniconda3/envs/idoc/bin/python  /home/vibflysleep/opt/idoc/idoc/server/bin/server.py --control --recognize --adaptation-time 0
    RestartSec=5
    Restart=always

    [Install]
    WantedBy=multi-user.target

1. Copy this code into a txt file
2. Edit the `ExecStart` line so:
   * the first token points to the python binary of your conda environment
   * the second token points to the `server.py` script

3. Place the file under `/etc/system/systemd/idoc_server.service` (you will need sudo permissions)
4. Link the configuration (installed under the normal user namespace) to the root user

::

    sudo mkdir -p /root/.config/idoc/
    sudo ln -sf ${HOME}/.config/idoc/idoc.yaml /root/.config/idoc/idoc.yaml
    sudo ln -sf ${HOME}/.config/idoc/machine-name /root/.config/idoc/machine-name

5. Refresh systemd and start the service like so

::

    systemctl daemon-reload
    systemctl enable --now idoc_server

6. You can check the logs by running

::

    journalctl -fu idoc_server



6. Install gooogle chrome and extension to refresh page
=============================================================

Install a program that can open a png file and refresh it every few seconds. We recommend simply installing google chrome and any extension that refreshes the open page every second or so.


7. Udev rule (Linux, OPTIONAL).
======================================

Linux users can write a udev rule so the file under `/dev` that represents the Arduino board is always the same,
regardless of how many boards are plugged or the order in which they were plugged.
Then, in the config file, update `controller.arduino_port` to match the file created by the udev rule.
Otherwise, set `controller.arduino_port` to `"/dev/ttyACM0"` in Linux and `"/dev/USB0"` in Windows 

8. Test connection between