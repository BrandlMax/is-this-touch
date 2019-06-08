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
            self.LINE = self.tryRead()

            if(self.LINE == self.Divider):
                if(len(self.doneBUFFER) < self.BufferLength):
                    self.doneBUFFER = self.zero(self.BufferLength)
                else:
                    self.doneBUFFER = self.wipBUFFER.copy()

                self.wipBUFFER = []
            else:
                value = self.toInt(self.LINE)
                if(len(self.wipBUFFER) <= self.BufferLength and value):
                    self.wipBUFFER.append(value)

            # print(self.doneBUFFER)
            self.ready = True

    def toInt(self, value):
        # To Prevent Error
        try:
            return int(value)
        except ValueError:
            return False

    def tryRead(self):
        try:
            return self.SERIAL.readline().decode('utf8').strip()
        except UnicodeDecodeError:
            return '0'

    def zero(self, n):
        zeros = [0] * n
        return zeros

    def close(self):
        self.isReading = False
        self.READINGTHREAD.join()
        self.SERIAL.close()
        print('Disconnected...')
