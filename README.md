# Software for TESEQ CSP 9160A high frequency current probe set dedicated to cooperation with Rigol DG2041A spectrum analyser
This project is a tool for loading data measured by Rigol DG2041A
spectrum analyser and converting it to give accurate measurment of
current.

## Launching
To launch this program you'll need:
*  Python 3
*  Libraries: tkinter, xlsxwriter, pubsub, matplotlib
*  Data files from Rigol DG2041A

Clone this repository and run *controller.py* file.

## Principle
This setup uses Ampere's Law. Changing current in primary winding
creates changing magnetic field. It is then concetrated in ferrite core.
This chaninging magnetic field induces voltage in secondary winding
which is then measured by spectrum analyser.

![Image](https://i.imgur.com/eews8dV.png)

This can be also shown in this simplified circut:

![Image](https://i.imgur.com/TJXij65.png)

Thanks to transfer impedance graph given by the producer of the probe we
can calculate current for each frequency in spectrum.

![Image](https://i.imgur.com/U58Oidk.png)

[Source](https://www.teseq.com/products/CSP-9160.php)

![Image](https://i.imgur.com/tN8A8i2.png)

[Source](http://www.interferencetechnology.com/wp-content/uploads/2012/04/Wyatt_NA_DDG12.pdf)

Typical practice is to put probe on one or more wires and connecting it
to spectrum analyser or other voltage measuring device as shown below.

![Image](https://i.imgur.com/LTMleiW.png)

Rigol DG2041A will show measured voltage on it's screen and allow user
to save it as .dat file. Extracting information from that file can be a
little bit clunky and cumbersome, especially when you have to take many
measurments with different ranges.

For more information and theory please visit [The HF Current Probe:
Theory and Application by Kenneth Wyatt](http://www.interferencetechnology.com/wp-content/uploads/2012/04/Wyatt_NA_DDG12.pdf),
[Current probes, more useful than you think](https://ieeexplore.ieee.org/document/750102)
or documentation for both Rigol DG2041A spectrum analyser and TESEQ CSP
9160A high frequency current probe.



## Interface
![Image](https://i.imgur.com/VfjE1mR.png9)

* New: Resets program for new input
* Import: Imports data from .dat file
* Export: Exports loaded files to xlsx
* Exit: Closes program

Graphs are both shown in logaritmic y scale. On the upper graph is
voltage measured by spectrum analyser, on the lower graph is calculated
current flowing through a primary winding.

## Use example: measuring common mode current in circuit
Let's say we want to check for common mode current in a given circuit.
We clamp our current probe on the right cable and begin measurment.

![Image](https://i.imgur.com/WQT2jrX.png)

After taking measurments and saving them to your computer run
controller.py. Press *File* -> *Import*. Select file to load. If you
measured more than one range, repeat this step for other files.

![Image](https://i.imgur.com/qfa9cUZ.png)

Your measurment and calculated current should display on your window.

![Image](https://i.imgur.com/w9JISm0.png)

To further calculations or molding the data export your files by
pressing *File* -> *Import* and chose your filename and location, press
*Save*

![Image](https://i.imgur.com/07RCwlq.png)

This should export your data to xlsx file as shown below:

![Image](https://i.imgur.com/wBlr6cp.png)


**Warning!** This program will not overwrite existing file if the file
is in use. It will give error window to warn the user whenever they'll
try.
