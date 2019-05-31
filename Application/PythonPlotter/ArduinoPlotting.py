# MFramework for my future projects, for faster Serial Plotting
from MFramework import Plotter


def main():
    print('ArduinoPlotting')
    # Init

    # ESP
    #PLOTTER = Plotter.HARRY_PLOTTER('/dev/cu.SLAB_USBtoUART', 115200)
    # UNO
    PLOTTER = Plotter.HARRY_PLOTTER('/dev/cu.usbmodem1413301', 115200)

    # Start Plotting Loop
    PLOTTER.render()
    # On End
    PLOTTER.close()


if __name__ == '__main__':
    main()
