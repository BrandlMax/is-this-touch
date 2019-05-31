# MFramework for my future projects, for faster Serial Plotting
from MFramework import Serial
from time import sleep


def main():
    print('ArduinoPlotting')

    # ESP
    # SERIAL = Serial.CONNECTION('/dev/cu.SLAB_USBtoUART', 115200)

    # UNO
    SERIAL = Serial.CONNECTION('/dev/cu.usbmodem1413301', 115200, 4, '7')

    while(SERIAL.isReading):
        for i in range(len(SERIAL.doneBUFFER)):
            print('LOG: ' + str(SERIAL.doneBUFFER[i]))


if __name__ == '__main__':
    main()
