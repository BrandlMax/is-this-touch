# SERIAL
# Inspired from https://www.thepoorengineer.com/en/arduino-python-plot/
import serial


class CONNECTION:
    def __init__(self, Port, Baud, BufferLength='1', Divider='0'):
        self.PORT = Port
        self.BAUD = Baud
        self.ready = False
        self.isReading = False
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
            self.ready = True

        except:
            self.ready = False
            print("Failed to connect with " + str(self.PORT) +
                  ' at ' + str(self.BAUD) + ' BAUD.')

    def READ(self):
        if(self.isReading != True):
            self.isReading = True
            while(self.isReading):
                self.LINE = self.tryRead()

                if(self.LINE == self.Divider):
                    if(len(self.doneBUFFER) < self.BufferLength):
                        self.doneBUFFER = self.zero(self.BufferLength)
                    else:
                        self.doneBUFFER = self.wipBUFFER.copy()
                    self.wipBUFFER = []
                    self.isReading = False
                else:
                    value = self.toInt(self.LINE)
                    if(len(self.wipBUFFER) <= self.BufferLength and value):
                        self.wipBUFFER.append(value)

                # print("Done Buffer", self.doneBUFFER)

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
        self.SERIAL.close()
        print('Disconnected...')
