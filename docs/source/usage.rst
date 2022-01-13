Usage
=====

.. _installation:

Installation
------------

To use idoc, first install it using conda:


1. Create a conda environoment
================================

.. code-block:: console

    conda create --name idoc python=3.7.4


2. Install pypylon
================================

Running `pip install pypylon` may install a version of the package which is buggy in conda environments.
We recommend to instead do the following

.. code-block:: console

    pip install git+https://github.com/basler/pypylon.git@1cbda303a0ab0d335c82f0460e71c0cc5c12bbeb


This will install from source the version of the module available under the git hash commit `1cbda303a0ab0d335c82f0460e71c0cc5c12bbeb`. This version was verified in Ubuntu 20.04.3

3. Install idoc
================================

.. code-block:: console

    pip install idoc


4. Set minimal configuration
================================

The configuration is by default installed to ``$HOME/idoc/idoc/config/idoc.conf`` in JSON format

You need to enter three fields under the ``"folders.results"`` entry

1. results: Path to a directory where the data from the new experiments will be saved
2. mappings: Path to a directory containing at least one mapping .csv file
3. paradigms: Path to a directory containing at least one paradigm .csv file

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


* We again have the hardware column, which should contain the same set of names you used in the hardware column of your mapping
* **start** and **end** show the moment when the hardware will start and end its duty, in minutes since experiment start
* **on** and **off** are the number of seconds the hardware should be on and off, if it should cycle during its duty. If no cycle is needed, leave NaN.
* **mode** must be either ``o``/``p`` where ``o`` is the default and ``p`` is if you want to use PWM, which allows you to modulate the output of the hardware (say light intensity).
    In that case, the hardware must be connected to a PWM supporting pin (see the board specs).
* **value** must be 1 everytime **mode** is ``o`` and between 0 and 1 if **mode** is set to ``p``.


5. Provide the default mapping and the default paradigm
================================================================

idoc needs the paradigm and mapping passed in the config to be available at boot.
Therefore, you need to make sure the file listed in the config under:


* ``controller.paradigm_path`` exists in the directory under ``folders.paradigms.path``.
* ``controller.mapping_path`` exists in the directory under ``folders.mappings.path``.
