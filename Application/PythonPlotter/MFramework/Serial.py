# SERIAL
# Inspired from https://www.thepoorengineer.com/en/arduino-python-plot/
import serial
import threading
import datetime as dt

import time


class CONNECTION:
    def __init__(self, Port, Baud, BufferLength='1', Divider='0'):
        self.PORT = Port
        self.BAUD = Baud
        self.ready = False
        self.isReading = True
        self.LINE = 0
        self.BufferLength = BufferLength
        self.wipBUFFER = []
        self.doneBUFFER = []
        self.Divider = Divider

        print('Trying to connect to: ' + str(self.PORT) +
              ' at ' + str(self.BAUD) + ' BAUD.')
        try:
            self.SERIAL = serial.Serial(self.PORT, self.BAUD, timeout=1)
            print('Connected to ' + str(self.PORT) +
                  ' at ' + str(self.BAUD) + ' BAUD.')

            self.READINGTHREAD = threading.Thread(target=self.READ)
            self.READINGTHREAD.start()

        except:
            print("Failed to connect with " + str(self.PORT) +
                  ' at ' + str(self.BAUD) + ' BAUD.')

    def READ(self):
        while (self.isReading):
            self.LINE = self.SERIAL.readline().decode('utf8').strip()

            if(self.LINE == self.Divider):
                self.doneBUFFER = self.wipBUFFER.copy()
                self.wipBUFFER = []
            else:
                self.wipBUFFER.append(self.LINE)

            print(self.doneBUFFER)
            self.ready = True

    def close(self):
        self.isReading = False
        self.READINGTHREAD.join()
        self.SERIAL.close()
        print('Disconnected...')
