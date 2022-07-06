import time
from math import floor
from pyfirmata import Arduino, util

class ArduinoNano:
        def __init__(self,usb):
                self.board = Arduino(usb,baudrate=57600)
                self.pumps = []

        def add_pump(self,pump_name,pump_pin,ms_pin,ms_highest_value,ms_lowest_value):
                self.pumps.append({
                        "pump_name":pump_name,
                        "pump_pin":pump_pin,
                        "ms_pin":ms_pin,
                        "ms_highest_value":ms_highest_value,
                        "ms_lowest_value":ms_lowest_value
                        })
        
        def turn_on_pump(self,pump_name,t):
                pin_on = 2
                for pump in self.pumps:
                        if pump["pump_name"] == pump_name:
                                pin_on = pump["pump_pin"]
                                self.board.digital[pin_on].write(0)
                                time.sleep(t)
                                self.board.digital[pin_on].write(1)

        def turn_on_off_pump_using_sensors(self,t):
                pump = self.pumps[0]
                pin = self.board.get_pin('a:'+ pump["ms_pin"] +':i')
                it = util.Iterator(self.board)
                it.start()
                
                if 30 > floor(-((((pin.read-pump["ms_lowest_value"])/(pump["ms_highest_value"]-pump["ms_lowest_value"]))*100)-100)):
                        self.board.digital[pump["pump_pin"]].write(0)
                        time.sleep(t)
                        self.board.digital[pump["pump_pin"]].write(1)

        def turn_all_off(self):
                for pump in self.pumps:
                        print("here")
                        self.board.digital[pump["pump_pin"]].write(1)

        def turn_all_on(self):
                for pump in self.pumps:
                        self.board.digital[pump["pump_pin"]].write(0)

