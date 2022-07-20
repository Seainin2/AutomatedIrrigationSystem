import time
import arduino as ar
import pyfirmata

if __name__ == "__main__":

    nano = ar.ArduinoNano('COM9')

    nano.add_pump('one',  2,  0,0.7,0.24)
    nano.add_pump('two',  3,  1,0.7,0.24)
    nano.add_pump('three',4,  2,0.7,0.24)
    nano.add_pump('four', 5,  3,0.7,0.24)

    nano.turn_all_pumps_off()

    it = pyfirmata.util.Iterator(nano.board)
    it.start()
    time.sleep(5)

    count = 0

    print("Start")

    while count < 1000000:

        nano.turn_on_off_pump_using_sensors(5)
        #print("\nRequest")
        #print(nano.get_sensor_value('one'))
        #dix = nano.get_sensor_value()
        #for dic in dix:
            #print(dic["pump_name"]+": "+str(dic["sensor_value"]))
        print(count)
        count = count + 1


