# HARRY PLOTTER
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from MFramework import Serial


class HARRY_PLOTTER:
    def __init__(self):
        print('HARRY PLOTTER')

        self.fig = plt.figure()
        self.ax = plt.axes()

        self.xs = self.zero(500)
        self.ys = self.zero(500)

        self.ax.set_title('Arduino Signal Plotter')
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Data')

        self.SERIAL = Serial.CONNECTION('/dev/cu.SLAB_USBtoUART', 115200)

    def plot(self, i, xs, ys):
        if(self.SERIAL.ready):
            self.xs = range(len(self.ys))
            self.ys.append(int(self.SERIAL.LINE))

            self.xs = self.xs[-500:]
            self.ys = self.ys[-500:]

            self.ax.clear()
            self.ax.plot(self.xs, self.ys, linewidth=1)

    def render(self):
        ani = animation.FuncAnimation(
            self.fig, self.plot, fargs=(self.xs, self.ys), interval=10)
        plt.show()

    def zero(self, n):
        zeros = [0] * n
        return zeros

    def close(self):
        self.SERIAL.close()
