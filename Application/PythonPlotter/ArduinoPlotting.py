# MFramework for my future projects, for faster Serial Plotting
from MFramework import Plotter


def main():
    print('ArduinoPlotting')

    # Plotter.HARRY_PLOTTER(
    # Mode, // String 'frequency' or 'stream' as Display-Type
    # Port, // Serial Port
    # Baud, // Baudrate from Arduino
    # BufferLength=1, // Number of related values for Plotting
    # Divider='0' // start value (kind of start bit)
    # )
    PLOTTER = Plotter.HARRY_PLOTTER(
        'frequency', '/dev/cu.usbmodem143201', 115200, 160, '999')

    # Start Plotting Loop
    PLOTTER.render()
    # On End
    PLOTTER.close()


if __name__ == '__main__':
    main()
