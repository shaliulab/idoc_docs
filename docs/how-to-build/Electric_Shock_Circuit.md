# **Electric Shocks Delivery Circuit**

## Overview

Electric shocks (ES) are commonly used in *Drosophila* research to deliver a controlled punishment to the flies during aversive learning and memory experiments. ES circuits typically consist of a power supply, and a set of electrodes that can be placed in contact with the flies. The intensity and duration of the electric shock can be controlled by adjusting the voltage and pulse duration of the circuit. However, the specific design and implementation of ES delivery circuits can vary widely depending on the specific experimental setup and research question.

The system consists of a series of components that are designed to regulate the delivery of ES, including a programmable power source and custom glass slides coated with Indium Tin Oxide (ITO) to allow for current delivery through the glass. The circuit is also designed to be controlled by a computer, which can allow for precise control over the timing and intensity of the electric shocks delivered to individual flies, which can be important for controlling experimental variables and ensuring reproducibility of results.

The electric shock system in the IDOC can be grouped into 3 key sections.

1. [Chambers](../IDOC-Chamber_Assembly) designed to pass the electrical shock to the flies when needed, while also allowing for observation throughout the process

2. A control system where a computer can interface with an Arduino to accurately trigger electric shocks with the desired timing and intensity

3. A way to electrically connect all the chambers to the rest of the machine, to actually allow for current transfer to the flies

**Electrical connections for the chamber tray**

To deliver the current to the pins of the IDOC chambers, we embed connector sockets into the tray that holds the chambers. For each chamber, there is a set of 4 contact sockets, totalling to 80 sockets for the entire IDOC setup. The connectors are made by combining the "clamp-side" of a connector socket (Digi-Key, [962876-2](https://www.digikey.be/en/products/detail/te-connectivity-amp-connectors/962876-2/2332160)) with a basic pin header (RS Components, [681-2994](https://benl.rs-online.com/web/p/pcb-headers/6812994/)) soldered into its bottom half. These can easily be inserted into their designated slots in the chamber tray. However, to ensure that they stay in place, you might need to apply some glue, or heat the clamp with a soldering iron as you are pressing them in (so as to have it melt into the surrounding plastic). If you decide to use the melting method, then remember to take extra precautions regarding the fumes from the melting plastic!

![ESock-socket.PNG](/assets/Images/ESock-socket.PNG)

Both sides of an electroshock chamber have 2 terminals, one negative and one positive. To match this, the chamber tray also needs to have 2 clamps on either side of every chamber slot. To ensure that each clamp can deliver the desired voltage and polarity, we need to connect each pin in an interwoven pattern. The design can be seen in the figure below. All pins of the same polarity are connected in series with each other.

![ESock-socket-connection.PNG](/assets/Images/ESock-socket-connection.PNG)

Once the wiring in the chamber tray is finalized, the whole system is properly covered and insulated with 3D printed covers

![ESock-socket-connection-cover.PNG](/assets/Images/ESock-socket-connection-cover.PNG)

Finally, the entire electroshock system is controlled by the Arduino relay switch unit. Here the shocks are sent into the rest of the circuit we have established in this section.

![ESock-Arduino-relay.PNG](/assets/Images/ESock-Arduino-relay.PNG)

**Power Supply Specifications**

The electrical shock PSU is the most demanding out of the 3 IDOC needs, as it needs to reliably output 75 V at repeated but short intervals. We chose this one [Consort E143](https://www.labmakelaar.com/product/consort-e143-power-supply-2/), which is typically used to run electrophoresis gels.