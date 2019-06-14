import csv


class LUKE_CSVWRITER:
    def __init__(self, BufferLength):
        print('LUKE_CSVWRITER')
        self.BufferLength = BufferLength
        self.header = self.createHeader()

    def start(self, filename):
        with open('export/' + filename, mode='w') as dataFile:
            fileWriter = csv.writer(
                dataFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            fileWriter.writerow(self.header)

    def writeFreq(self, filename, dataArray):
        with open('export/' + filename, mode='a') as dataFile:
            fileWriter = csv.writer(
                dataFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            fileWriter.writerow(dataArray)

    def createHeader(self):
        headerArray = []
        for x in range(self.BufferLength):
            headerArray.append(x)
        return headerArray
