# HARRY PLOTTER
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Button

from MFramework import Serial


class HARRY_PLOTTER:
    def __init__(self, Port, Baud, BufferLength='1', Divider='0'):
        print('HARRY PLOTTER')

        # Plot
        self.fig = plt.figure(num='m˚ Signal Plotter')
        self.ax = plt.axes()

        # Dummy Data
        self.xs = self.zero(500)
        self.ys = self.zero(500)

        # Labels
        self.ax.set_title('Arduino Signal Plotter')
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Data')

        # GUI
        # L, B, W, H
        self.axStart = plt.axes([0, 0, 0.2, 0.05])
        self.startButton = Button(self.axStart, 'Start Session')
        self.startButton.on_clicked(self.startSession)

        self.axEnd = plt.axes([0.21, 0, 0.2, 0.05])
        self.endButton = Button(self.axEnd, 'End Session')
        self.endButton.on_clicked(self.endSession)

        self.SERIAL = Serial.CONNECTION(Port, Baud, BufferLength, Divider)

    def plot(self, i, xs, ys):
        if(self.SERIAL.ready):
            self.xs = range(len(self.ys))
            print(self.SERIAL.doneBUFFER)
            for i in range(len(self.SERIAL.doneBUFFER)):
                print('PLOT: ' + str(self.SERIAL.doneBUFFER[i]))
                self.ys.append(int(self.SERIAL.doneBUFFER[i]))

            self.xs = self.xs[-500:]
            self.ys = self.ys[-500:]

            self.ax.clear()
            self.ax.plot(self.xs, self.ys, linewidth=1)

    def render(self):
        ani = animation.FuncAnimation(
            self.fig, self.plot, fargs=(self.xs, self.ys), interval=1)
        plt.show()

    def startSession(self, e):
        print('Session Started')

    def endSession(self, e):
        print('Session closed')

    def zero(self, n):
        zeros = [0] * n
        return zeros

    def close(self):
        self.SERIAL.close()
