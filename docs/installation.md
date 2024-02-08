Installation
--------------

To use idoc we recommend creating a conda environment. mamba may also work but we haven't tested it. Please install anaconda or miniconda and proceed as follows.

## 1. Create a conda environoment

```
    conda create --name idoc python=3.8.10
    conda activate idoc
```

This creates the conda environment with the desired python version,
which makes it easy to have any version of python packages
without conflicts with other pieces of software on the same computer

## 2. Install idoc

```
    pip install idoc
```

This will install the last version of the idoc package (2.1.8 as of February 2024) from https://pypi.org/ as well as all the dependencies


## 3. Set results folder, paradigms folder and mapping


The configuration is by default installed to `$HOME/.config/idoc/idoc.yaml` in YAML format.
Upon installation of idoc, this file is created automatically.
You need to update the following fields to make them match your system.

1. `folders.results.path`: Path to a directory where the data from the new experiments will be saved
2. `folders.paradigms.path`: Path to a directory containing at least one paradigm .csv file
3. `controller.mapping_path`: Path to a directory containing at least one mapping .csv file
4. `controller.paradigm_path`: Filename of a .csv file available under the `folders.paradigms.path` used as default paradigm


## 4. Provide a default mapping and default paradigm

### Mapping

A valid mapping is a .csv file with two columns called `hardware` and `pin_number`. It looks like this:

```
  hardware,pin_number
  IRLED,45
  LED_R_LEFT,3
  LED_R_RIGHT,2
```

* The pin number corresponds to the number written on the GPIO of the Arduino board you use.
* The hardware column should contain a user-friendly name you give to this hardware. No spaces are allowed!

[This](/assets/src/mega.csv) is the mapping we use in one of our idocs.


### Paradigm


A valid paradigm would look like this

```
  hardware,start,end,on,off,mode,value
  IRLED,0,5,NaN,NaN,o,1
  LED_R_LEFT,1,2,1,1,o,1
  LED_R_RIGHT,1,2,1,1,o,1
```

* The hardware column contains the same set of names you used in the hardware column of your mapping.
* **start** and **end** show the moment when the hardware will start and end its duty, in minutes since experiment start.
* **on** and **off** are the number of seconds the hardware should be on and off, if it should cycle during its duty. If no cycle is needed, leave NaN.
* **mode** must be either `o`/`p` where `o` is the default and `p` is if you want to use PWM, which allows you to modulate the output of the hardware (say light intensity). In that case, the hardware must be connected to a PWM supporting pin (see the board specs).
* **value** must be 1 everytime **mode** is `o` and between 0 and 1 if **mode** is set to `p`.

All these columns are **required** in your paradigms.

### Example of a paradigm: the warm_up

This paradigm will turn on the IR light and activate a clean air flow through the chambers, but will deliver no other stimuli the animals

```
    hardware,start,end,on,off,mode,value
    MAIN_VALVE,0,5,NaN,NaN,o,1  # inflow
    VACUUM,0,5,NaN,NaN,o,1      # outflow
    IRLED,0,5,NaN,NaN,o,1       # IR light
    TARGETS,0,.2,NaN,NaN,o,1    # targets for the detection of the arena
    ONBOARD_LED,0,5,500,500,o,1 # just the LED on the Arduino flashing at 1 Hz for 5 minutes.
```
[Link](/assets/warm_up.csv)

**Please note:**

idoc needs the paradigm and mapping passed in the config to be available at boot.
Therefore, you need to make sure the file listed in the config under:

* `controller.paradigm_path` exists in the directory under `folders.paradigms.path`.
* `controller.mapping_path` exists in the directory under `folders.mappings.path`.

Additionally, your other paradigms should be saved in .csv format wherever `folders.paradigms.path` points to.


## 5. Create  machine-name

Linux users need to make sure the contents of `/$HOME/.config/idoc/machine-name` have the name they want their machine to have, for example `IDOC_001`.
If this file does not exist, it must be created as a plain text file with no extensions.
This will set the name of the folder under which all experiments will be saved.

## 6. Configure logs

You must have a file called `$HOME/.config/idoc/logging.yaml` with the following content:

```
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
```


You can optionally adjust the logging level of the idoc modules by adding more loggers, like so

```
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
```

## 7. Install systemd service


We recommend running the idoc_server as a service that is always spawned in the background.
This is achieved with a systemd service file, which must be placed under `/etc/system/systemd/idoc_server.service`

```
    [Unit]
    Description=IDOC Server
    Wants=ntpd.service
    After=ntpd.service


    [Service]
    Type=simple
    Environment="HOME=/root"
    ExecStart=/home/vibflysleep/miniconda3/envs/idoc/bin/python  /home/vibflysleep/anaconda3/envs/idoc/lib/python3.8/site-packages/idoc/server/bin/server.py --control --recognize --adaptation-time 0
    RestartSec=5
    Restart=always

    [Install]
    WantedBy=multi-user.target
```

#### 1. Copy this code into a txt file

#### 2. Edit the `ExecStart` line so:


   * the first token (`/home/vibflysleep/miniconda3/envs/idoc/bin/python`) points to the python binary of your conda environment
   * the second token (`/home/vibflysleep/anaconda3/envs/idoc/lib/python3.8/site-packages/idoc/server/bin/server.py`) points to the `server.py` script. It should have the same prefix as your python binary (if you installed using conda)

#### 3. Place the file under `/etc/system/systemd/idoc_server.service` (you will need sudo permissions)


#### 4. Link the configuration (installed under the normal user namespace) to the root user

```
    sudo mkdir -p /root/.config/idoc/
    sudo ln -sf ${HOME}/.config/idoc/idoc.yaml /root/.config/idoc/idoc.yaml
    sudo ln -sf ${HOME}/.config/idoc/machine-name /root/.config/idoc/machine-name
```

#### 5. Refresh systemd and start the service like so

```
    systemctl daemon-reload
    systemctl enable --now idoc_server
```

#### 6. You can check the logs by running

```
    journalctl -fu idoc_server
```

NOTE. In order to view the logs produced by a program run by the root user,
your user needs to belong to the adm group. You can get that done by

```
    sudo su # become superuser
    usermod -aG your_user adm
```

and logout or reboot the pc


## 8. Install gooogle chrome and extension to refresh page or sxiv

Install a program that can open a png file and refresh it every few seconds. We recommend:

1) Simply installing google chrome and any extension that refreshes the open page every second or so.

2) We recently found [sxiv](https://manpages.ubuntu.com/manpages/xenial/man1/sxiv.1.html) can also render a .png that is frequently updated to generate a pseudofeed. You can install it with `sudo apt install sxiv`.


## 9. Udev rule (Linux, OPTIONAL).

Linux users can write a udev rule so the file under `/dev` that represents the Arduino board is always the same,
regardless of how many boards are plugged or the order in which they were plugged.
Then, in the config file, update `controller.arduino_port` to match the file created by the udev rule.
Otherwise, set `controller.arduino_port` to `"/dev/ttyACM0"` in Linux and `"/dev/USB0"` in Windows

## 10. Test connection between computer and Arduino

TODO


PS The IDOC software draws heavy inspiration from the ethoscope, a platform developed in [the lab of Giorgio Gilestro](https://github.com/gilestrolab) to quantify fly behavior in high-throughput in isolated flies. 