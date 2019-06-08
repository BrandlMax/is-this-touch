# MFramework for my future projects, for faster Serial Plotting
from MFramework import Plotter


def main():
    print('ArduinoPlotting')
    # ESP
    #PLOTTER = Plotter.HARRY_PLOTTER('/dev/cu.SLAB_USBtoUART', 115200, 1, '')
    # UNO
    PLOTTER = Plotter.HARRY_PLOTTER(
        'freq', '/dev/cu.usbmodem141401', 115200, 160, '999')

    # Start Plotting Loop
    PLOTTER.render()
    # On End
    PLOTTER.close()


if __name__ == '__main__':
    main()
