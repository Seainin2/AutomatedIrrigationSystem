import flask
from flask import request, jsonify
from arduino import ArduinoNano
import pyfirmata
import time

app = flask.Flask(__name__)
app.config["DEBUG"] = True

nano = ArduinoNano()
nano.add_pump('one',  2,  0,0.7,0.24)
nano.add_pump('two',  3,  1,0.7,0.24)
nano.add_pump('three',4,  2,0.7,0.24)
nano.add_pump('four', 5,  3,0.7,0.24)

nano.turn_all_pumps_off()

it = pyfirmata.util.Iterator(nano.board)
it.start()
time.sleep(5)

@app.route('/', methods=['GET'])
def home():
    
    return "<h1>Hello World</h1>"
    #return nano.turn_on_off_pump_using_sensors(2)


app.run()

