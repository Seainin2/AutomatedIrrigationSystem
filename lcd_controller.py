import time
import arduino as ar
import pyfirmata
import test_lcd as LCD

if __name__ == "__main__":

    nano = ar.ArduinoNano('/dev/ttyUSB0')

    nano.add_pump('one',  2,  0,0.7,0.24)
    nano.add_pump('two',  3,  1,0.7,0.24)
    nano.add_pump('three',4,  2,0.7,0.24)
    nano.add_pump('four', 5,  3,0.7,0.24)

    nano.turn_all_pumps_off()

    it = pyfirmata.util.Iterator(nano.board)
    it.start()
    time.sleep(5)

    lcd_class = LCD.LCDPython()
    print(type(lcd_class))
    lcd_class.lcd.message("Hello World!")
