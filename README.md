# Is this touch?

![alt text](.readme/groupTouche.jpeg 'All Prototypes')
Sensor and application to generate training data for my [Signal Classifier](https://github.com/BrandlMax/Signal-Classifier 'Signal Classifier') to turn objects into touch-sensitive interfaces.

---

## Documentation

### Steps

- [x] Build the sensor prototype with Arduino Uno
- [x] Get clean data and test the sensor
- [ ] ~~Rewrite Code for ESP~~
- [x] Write an application to generate training data
  - [x] Realtime plotting
  - [x] Matching serial communication to the Arduino Touché sensor
  - [x] Start / Stop Sequence
  - [x] Save Dataset

#### Build the sensor prototype with Arduino Uno

![alt text](.readme/UnoTouche.jpeg 'Touché with Arduino Uno')
![alt text](.readme/dzl.jpg 'Touché with Arduino Uno')

As a starting point I took the [example of @damellis](https://github.com/damellis/ESP/wiki/%5BExample%5D-Touché-swept-frequency-capacitive-sensing 'Example Touché swept frequency capacitive sensing'), which is based on the schematic of [DZL](http://dzlsevilgeniuslair.blogspot.com/2012/05/arduino-do-touche-dance.html 'Arduino do the Touché dance') and the code of [madshobye](https://www.instructables.com/id/Touche-for-Arduino-Advanced-touch-sensing/ 'Touche for Arduino: Advanced Touch Sensing.').

##### Output

The madshobye code comes with a processing script that can plot the data from the Uno. The results looked very good and the experiment with the water interface could also be successfully reproduced.
![alt text](.readme/UnoData.png 'Result of Arduino Uno')

#### Rewrite Code for ESP

Because of the smaller size, Bluetooth and Wifi I wanted to rewrite the code to ESP. This way I wanted to understand the code better. After a few hours and trying to replace the Arduino "timer register" on the ESP or to find a working alternative or workaround, I put the attempt aside. The best result I could get was the differentiation between touch and no touch, but that was extremely noisy and no different from a normal capacitive sensor.

![alt text](.readme/ESPdata.png 'Result of rewriting the Code for ESP')

#### Write an application to generate training data

![alt text](.readme/testESP.jpeg 'Touché with Arduino Uno')
To better understand serial communication I built a small simple Capacitive Sensor with an ESP. With its data I built a first Python script to test the serial communication and to plot this data afterwards.

##### Understanding the Code and Serial

I like when my code is modular and therefore I wrote a small framework with two components to manage the serial communication and to plot the data.

Here I had to find out more about threads and threading so that I could read the serial data and then process it by the plotter at the same time.

Then I found out that it makes a difference if you map a stream of data or an array of data and so I had to add a switch for each case. I then tried to understand the technique how the Arduino Uno sends the array of data to Python to plot the data the same way.

##### GUI / Plotter

![alt text](.readme/UI.png 'Touché with Arduino Uno')
For plotting I use [matplotlib](https://matplotlib.org 'matplotlib for Python'). For time reasons I decided not to use tkinter or qt for the GUI. Matplotlib uses Tkinter under the hood but if you try to manually put the plot into a Tkinter window you may experience problems with plot updates and interactivity. But with matplotlib you can also add buttons and interaction elements to the window, this should be enough for the first version.

##### Matching serial communication to the Arduino Touché sensor

I have rewritten the "SendData" code so that I can see it in the Arduino plotter and display it in my Python version.

![alt text](.readme/PythonPlotterResults.png 'Results with Python Plotter')

![alt text](.readme/ArduinoPlotter.png 'Results with Arduino Plotter')

##### Sessions and CSV Data

You can now start sessions with the "Start Session" button and all data will be saved in a CSV file with session id. With "End Session" the session will be ended and no further data will be written to the file. Unfortunately I haven't found a solution yet how to make it visible that a session is running.

## ![alt text](.readme/CSV.png 'Results with Arduino Plotter')

### Inspirations and Papers

- https://www.youtube.com/watch?v=E4tYpXVTjxA
- https://pdfs.semanticscholar.org/d0bb/14033d11613c50958379e6825859c31c15ee.pdf
- https://github.com/damellis/ESP
- https://dl.acm.org/citation.cfm?id=3064735

---

### Info & Disclaimer

Submission for the 6th semester in Creative Coding, Interactive Media Design, supervised by Prof. Claudius Coenen (@ccoenen) and Prof. Garrit Schaap (@pixelkind)
