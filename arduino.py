import time
from math import floor
from pyfirmata import Arduino, util

class ArduinoNano:
        def __init__(self,usb):
                self.board = Arduino(usb,baudrate=57600)
                self.pumps = []

        def add_pump(self,pump_name,pump_pin,ms_pin,ms_highest_value,ms_lowest_value):
                
                threshold = ((ms_highest_value - ms_lowest_value)/100)*70 + ms_lowest_value

                self.pumps.append({
                        "pump_name":pump_name,
                        "pump_pin":self.board.digital[pump_pin],
                        "ms_pin":self.board.get_pin('a:'+str(ms_pin)+':i'),
                        "ms_threshold":threshold,
                        "ms_highest_value":ms_highest_value,
                        "ms_lowest_value":ms_lowest_value
                        })
                
        
        def turn_on_pump(self,pump_name,t):
                pin_on = 2
                for pump in self.pumps:
                        if pump["pump_name"] == pump_name:
                                
                                pump["pump_pin"].write(0)
                                time.sleep(t)
                                pump["pump_pin"].write(1)

        def turn_on_off_pump_using_sensors(self,t):
                for pump in self.pumps:

                        if pump["ms_pin"].read() > pump["ms_threshold"]:
                                pump["pump_pin"].write(0)
                                time.sleep(t)
                                pump["pump_pin"].write(1)

        def turn_all_pumps_off(self):
                for pump in self.pumps:
                        pump["pump_pin"].write(1)

        def turn_all_pumps_on(self):
                for pump in self.pumps:
                        pump["pump_pin"].write(0)
        
        def get_all_sensor_value(self):
                sensor_values = []
                
                for pump in self.pumps:
                        sensor_values.append({
                                "pump_name":pump["pump_name"],
                                "sensor_value":pump["ms_pin"].read()
                                })
                
                return sensor_values
        
        def get_sensor_value(self,pump_name):
                for pump in self.pumps:
                        if pump["pump_name"] == pump_name:
                                return {
                                        "pump_name" : pump_name,
                                        "sensor_value" : pump["ms_pin"].read()
                                        }



