from pyfirmata import Arduino

board = Arduino("COM5")

loopTimes = input('How many times would you like the LED to blink: ')
print("Blinking " + loopTimes + " times.")

for x in range(int(loopTimes)):
        pin13 = board.get_pin('d:13:p')
        pin13.write(1)
