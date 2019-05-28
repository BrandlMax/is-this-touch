# SERIAL
import serial

# Time
import datetime as dt

# PLOTTING
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# GLOBAL SETTINGS
PORT = '/dev/cu.SLAB_USBtoUART'
BAUD = 115200
SERIAL = serial.Serial(PORT, BAUD)

# GLOBAL VARS
Frame = 0

# HARRY PLOTTER SETTINGS
xmin = 0
xmax = 100
ymin = -(1)
ymax = 1

fig = plt.figure()
ax = plt.axes(xlim=(xmin, xmax), ylim=(
    float(ymin - (ymax - ymin) / 10), float(ymax + (ymax - ymin) / 10)))
xs = []
ys = []

ax.set_title('Arduino Accelerometer')
ax.set_xlabel('Time')
ax.set_ylabel('Data')


def plotter(i, xs, ys):
    global Frame
    # Add data to axis lists
    Frame = Frame + 1
    xs.append(Frame)
    ys.append(SERIAL.readline().decode('utf-8'))

    # Amount of Entries
    xs = xs[-100:]
    ys = ys[-100:]

    # Plot it Baby
    ax.clear()
    ax.plot(xs, ys)


def main():
    print('Hello World')

    ani = animation.FuncAnimation(
        fig, plotter, fargs=(xs, ys), interval=10)
    plt.show()
    # while True:
    #     reading = SERIAL.readline().decode('utf-8')
    #     print(reading)


if __name__ == '__main__':
    main()
