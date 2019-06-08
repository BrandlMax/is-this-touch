# HARRY PLOTTER
from MFramework import Serial
from MFramework import CSV
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
    def __init__(self, Mode, Port, Baud, BufferLength=1, Divider='0'):
        print('HARRY PLOTTER')

        # PLOT
        self.Mode = Mode
        self.BufferLength = BufferLength
        self.fig = plt.figure(num='m˚ Signal Plotter', figsize=(6, 6))
        self.ax = plt.subplot()
        plt.subplots_adjust(bottom=0.2)

        # DUMMY DATA
        self.xs = self.zero(self.BufferLength)
        self.ys = self.zero(self.BufferLength)

        # LABELS
        self.setLabels()

        # GUI
        # L, B, W, H
        self.axStart = plt.axes([0.01, 0.01, 0.2, 0.05])
        self.startButton = Button(self.axStart, 'Start Session')
        self.startButton.on_clicked(self.startSession)

        self.axEnd = plt.axes([0.22, 0.01, 0.2, 0.05])
        self.endButton = Button(self.axEnd, 'End Session')
        self.endButton.on_clicked(self.endSession)

        # SESSION
        self.isSession = False
        self.sessionId = 0

        # START SERIAL CONNECTION
        self.CSV = CSV.LUKE_CSVWRITER(self.BufferLength)
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
                if(self.isSession):
                    self.CSV.writeStream(
                        'Session_' + str(self.sessionId) + '.csv', self.SERIAL.doneBUFFER)
            else:
                print('No Mode Selected')

            self.ax.clear()
            self.setLabels()
            self.ax.plot(self.xs, self.ys, linewidth=1)

    def render(self):
        ani = animation.FuncAnimation(
            self.fig, self.plot, fargs=(self.xs, self.ys), interval=1)
        plt.show()

    def startSession(self, e):
        print('Session Started')
        if(self.isSession != True):
            self.isSession = True
            self.sessionId = self.sessionId + 1
            self.CSV.start('Session_' + str(self.sessionId) + '.csv')

    def endSession(self, e):
        print('Session closed')
        self.isSession = False

    def zero(self, n):
        zeros = [0] * n
        return zeros

    def setLabels(self):
        # Set Labels
        self.ax.set_title('Arduino Signal Plotter')

        if(self.Mode == 'freq'):
            self.ax.set_xlabel('Frequencies')
        else:
            self.ax.set_xlabel('Time')

        self.ax.set_ylabel('Data')

    def close(self):
        self.SERIAL.close()
