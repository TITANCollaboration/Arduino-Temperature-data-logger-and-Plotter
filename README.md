# Arduino-Temperature-data-logger-and-Plotter
Code for an Arduino Thermocouple Temperature monitoring system

This setup was originally made for monitoring the temperature of the power supply for PB5 but was then upgraded to a permanent EPICS viewable system

This setup can be used for monitoring any temperature related applications
The Arduino code was originally written to use a K- type thermocouple but this can be changed easily within the Arduino code if needed

The Data logger and Plotter are both written in Python and were originally intended to collect days worth of data although they will work for any amount of data
The data logger also creates its own folder for the csv files it creates, the name of this folder can also be changed easily 

**Very important to know the Plotter script must also be within the folder the csv files are in **
