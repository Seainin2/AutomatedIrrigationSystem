from pyfirmata import Arduino
import time

board = Arduino("COM6")
flag = True
num = 1

while(flag):
  board.digital[13].write(num)
  time.sleep(1)
  if num == 1:
    num = 0
  if num == 0:
    num = 1
  