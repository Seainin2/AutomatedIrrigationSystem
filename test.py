import arduino as ar

if __name__ == "__main__":

    nano = ar.ArduinoNano('COM5')

    nano.add_pump('one',2,0,0.7,0.24)

    nano.turn_all_off()

    nano.turn_on_pump('one',20)
