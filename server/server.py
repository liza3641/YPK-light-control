from flask import Flask, render_template, request
import json
#from flask_restful import Resource, Api
#from flask_restful import reqparse

import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600, timeout = 1)
time.sleep(1)

app = Flask(__name__)

@app.route('/', methods=['POST'])
def setLed():
    rgb = [] * 3
    r = int(request.form['R'])
    g = int(request.form['G'])
    b = int(request.form['B'])
    str = 'L{0:0>3}{1:0>3}{2:0>3}'.format(r,g,b)
    print(str)
    ser.write(bytes(str))
    return "Hello."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

str = 'L100000100'
ser.write(bytes(str))
