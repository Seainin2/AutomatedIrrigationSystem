from pyfirmata import Arduino,util
import time

board = Arduino("COM6",baudrate=57600)

it = util.Iterator(board)
it.start()

pin = board.get_pin('a:0:i')

while True:
    print(pin.read())
    time.sleep(1)