# **Electric Shocks Delivery Circuit**

Electric shocks are commonly used in *Drosophila* research to deliver a controlled electrical shock to the flies during aversive learning and memory experiments. The circuits typically consist of a power supply, and a set of electrodes that can be placed in contact with the flies. The intensity and duration of the electric shock can be controlled by adjusting the voltage and pulse duration of the circuit. However, the specific design and implementation of electric shock delivery circuits can vary widely depending on the specific experimental setup and research question.

The electric shock system consists of a series of components that are designed to regulate the delivery of electric shocks, including a programmable power source and custom glass slides coated with Indium Tin Oxide (ITO) to allow for current delivery through the glass. The circuit is also designed to be controlled by a computer, which can allow for precise control over the timing and intensity of the electric shocks delivered to individual flies, which can be important for controlling experimental variables and ensuring reproducibility of results.

The electric shock system in the IDOC can be grouped into 3 key sections.
1. Chambers designed to pass the electrical shock to the flies when needed, while also allowing for observation throughout the process
2. A control system where a computer can interface with an Arduino to accurately trigger electric shocks with the desired timing and intensity
3. A way to electrically connect all the chambers to the rest of the machine, to actually allow for current transfer to the flies


**Electrical connections for the chamber tray**

To deliver the current to the pins of the IDOC chambers, we embed connector sockets into the tray that holds the chambers. For each chamber, there is a set of 4 contact sockets, totalling to 80 sockets for the entire IDOC setup. The connectors are made by combining the "clamp-side" of a connector socket (Digi-Key, [962876-2](https://www.digikey.be/en/products/detail/te-connectivity-amp-connectors/962876-2/2332160)) with a basic pin header (RS Components, [681-2994](https://benl.rs-online.com/web/p/pcb-headers/6812994/)) soldered into its bottom half.

![ESock-socket.PNG](/assets/Images/ESock-socket.PNG)




Either side of the chamber has 2 sockets, one negative and one positive. The wiring design can be seen in the figure below.


![ESock-socket-connection.PNG](/assets/Images/ESock-socket-connection.PNG)




Once the wiring in the chamber tray is finalized, the whole system is properly covered and insulated with 3D printed covers

![ESock-socket-connection-cover.PNG](/assets/Images/ESock-socket-connection-cover.PNG)




Finally, the entire electroshock system is controlled by the Arduino relay switch unit. Here the shocks are sent into the rest of the circuit we have established in this section.

![ESock-Arduino-relay.PNG](/assets/Images/ESock-Arduino-relay.PNG)
