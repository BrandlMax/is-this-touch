# HARRY PLOTTER
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from MFramework import Serial


class HARRY_PLOTTER:
    def __init__(self):
        print('HARRY PLOTTER')

        self.xmin = 0
        self.xmax = 100
        self.ymin = 0
        self.ymax = 100

        self.fig = plt.figure()
        self.ax = plt.axes()
        self.xs = []
        self.ys = []

        self.ax.set_title('Arduino Accelerometer')
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Data')

        self.Frame = 0

        self.SERIAL = Serial.CONNECTION('/dev/cu.SLAB_USBtoUART', 115200)

    def plot(self, i, xs, ys):
        if(self.SERIAL.ready):
            # print('DATA: ' + str(self.SERIAL.LINE))
            # Add data to axis lists
            self.xs.append(self.Frame)
            self.ys.append(int(self.SERIAL.LINE))

            self.xs = self.xs[-100:]
            self.ys = self.ys[-100:]

            self.ax.clear()
            self.ax.plot(range(len(self.ys)), self.ys)

    def render(self):
        ani = animation.FuncAnimation(
            self.fig, self.plot, fargs=(self.xs, self.ys), interval=10)
        plt.show()

    def close(self):
        self.SERIAL.close()
