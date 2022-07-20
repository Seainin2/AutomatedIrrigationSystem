from curses import baudrate
import serial.tools.list_ports
import _curses
ports = serial.tools.list_ports.comports()

for port, desc, hwid in sorted(ports):
    print("{}: {} [{}]".format(port. desc. hwid))

import serial
port = serial.Serial("COM6", baudrate=57600)