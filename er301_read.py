#!/usr/bin/pyhton
from yhy523u import YHY523U

if __name__ == '__main__':
    nfc = ER301('COM5', 115200)
    nfc.select()
    i = 0
    outdata = ''
    while (15 > i):
        outdata += nfc.read_sector(i+1)
        i += 1
    outfile = open('readdata', 'wb')
    outfile.write(outdata)
    outfile.close()
