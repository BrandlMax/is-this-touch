# MFramework for my future projects, for faster Serial Plotting
from MFramework import Serial


def main():
    print('ArduinoPlotting')
    SERIAL = Serial.CONNECTION('/dev/cu.SLAB_USBtoUART', 115200)
    while(SERIAL.isReading):
        print(SERIAL.LINE)


if __name__ == '__main__':
    main()
