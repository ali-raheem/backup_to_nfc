#!/usr/bin/pyhton
from yhy523u import YHY523U

class ER301 (YHY523U):
    def write_data_sector(self, sector, value='\x00'*48):
        ''' Writes to blocks 0-2 Not trailing blocks '''
        blocks = [value[:16], value[16:32], value[32:48]]
        i = 0
        while (3 > i):
            self.write_block(sector, '\xff'*6, i, blocks[i])
            i += 1
    def write_data(self, data='\x00'*720):
        ''' Write 720 bytes to card EEPROM '''
        i = 0
        while (15 > i):
            value = data[i*48:(i+1)*48]
            self.write_data_sector(i+1, value)
            i += 1
if __name__ == '__main__':
    datafile = open('datafile', 'rb')
    data = datafile.read()
    datafile.close()
    padding = 720 - len(data)
    if(0 > padding):
        print "Error split data at 720 bytes"
        exit()
    data += '\x24'*padding
    nfc = ER301('COM5', 115200)
    nfc.select()
    nfc.write_data(data)
    #nfc.dump()
    i = 0
    outdata = ''
    while (15 > i):
        outdata += nfc.read_sector(i+1)
        i += 1
    outfile = open('readdata', 'wb')
    outfile.write(outdata[:-padding])
    outfile.close()
