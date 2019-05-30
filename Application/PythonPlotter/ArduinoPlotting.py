# MFramework for my future projects, for faster Serial Plotting
from MFramework import Plotter


def main():
    print('ArduinoPlotting')

    # Init
    PLOTTER = Plotter.HARRY_PLOTTER()
    # Start Plotting Loop
    PLOTTER.render()

    PLOTTER.close()


if __name__ == '__main__':
    main()
