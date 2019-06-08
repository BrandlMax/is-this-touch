# HARRY PLOTTER
from MFramework import Serial
import numpy as np
# For Plotting
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# For GUI
from matplotlib import colors as mcolors
from matplotlib.widgets import Button
matplotlib.rcParams['toolbar'] = 'None'
colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)


class HARRY_PLOTTER:
    def __init__(self, Mode, Scale, Port, Baud, BufferLength='1', Divider='0'):
        print('HARRY PLOTTER')

        # Plot
        self.Mode = Mode
        self.Scale = Scale
        self.fig = plt.figure(num='m˚ Signal Plotter', figsize=(5, 6))
        self.ax = plt.subplot()
        plt.subplots_adjust(bottom=0.2)

        # Dummy Data
        self.xs = self.zero(self.Scale)
        self.ys = self.zero(self.Scale)

        # Labels
        self.ax.set_title('Arduino Signal Plotter')

        if(self.Mode == 'freq'):
            self.ax.set_xlabel('Frequencies')
        else:
            self.ax.set_xlabel('Time')

        self.ax.set_ylabel('Data')
        # GUI

        # L, B, W, H
        self.axStart = plt.axes([0.01, 0.01, 0.2, 0.05])
        self.startButton = Button(self.axStart, 'Start Session')
        self.startButton.on_clicked(self.startSession)

        self.axEnd = plt.axes([0.22, 0.01, 0.2, 0.05])
        self.endButton = Button(self.axEnd, 'End Session')
        self.endButton.on_clicked(self.endSession)

        # START SERIAL CONNECTION
        self.SERIAL = Serial.CONNECTION(Port, Baud, BufferLength, Divider)

    def plot(self, i, xs, ys):
        if(self.SERIAL.ready):

            if(self.Mode == 'stream'):
                for i in range(len(self.SERIAL.doneBUFFER)):
                    # print('PLOT: ' + str(self.SERIAL.doneBUFFER[i]))
                    self.ys.append(int(self.SERIAL.doneBUFFER[i]))
                self.xs = range(len(self.ys))
                self.xs = self.xs[-500:]
                self.ys = self.ys[-500:]
            elif(self.Mode == 'freq'):
                self.ys = self.SERIAL.doneBUFFER.copy()
                self.xs = range(len(self.ys))
            else:
                print('No Mode Selected')

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
