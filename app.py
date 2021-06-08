from flask import Flask, render_template, url_for, request, redirect, make_response, Response
import serial
from datetime import datetime
from datetime import date
import app
import random
import json
import time

global app
app = Flask(__name__)

#sensorler
global inductive
global capasitive
global fotoelektrik
global ultrasonic

#kapilar
global kapiInductive
global kapiCapasitive
global kapiFotoelektrik
global kapiUltrasonic

#alt donus 
global donmeDolap

@app.route('/chart-data')
def ajax() :
    print("hello we are starting!")
    def ff():
        while True:
            motifs = random.randint(3, 19)
            time.sleep(1)
            json_data = json.dumps({'x': motifs})
            yield f"data:{json_data}\n\n"
    return Response(ff(), mimetype='text/event-stream')

@app.route("/")
def index():
     return render_template("index.html")

# def dursun():

#     cisim_sayi = 0 #program her baslatildiginda sensörden yeni veriler alinir



#     print("Firebase is On!!")
#     except:
#     print('Cant connect to Firebase')

#     """Serial port açma işlemi burada yapiliyor."""
#     try:
#     arduino = serial.Serial(port="/dev/cu.usbserial-1420", baudrate=9600)
#     print("Sensor is On!!")
#     except:
#     print('Please check the port')

#     62

#     while 1:
#     sensor_name = "sensor-1"
#     clean = str(arduino.readline())
#     print(clean)
#     cisim_sayi = cisim_sayi + 1
#     veri = cisim_sayi
#     veri = str(veri)
#     now = datetime.now()
#     current_time = now.strftime("%H:%M:%S")
#     today = date.today()
#     d1 = today.strftime("%d/%m/%Y")
#     #arduino verisi alindi
#     data = {
#     'Sensor_Name':sensor_name,
#     'Sensor_Data':veri,
#     'Current_Time':current_time,
#     'Current_Date':d1
#     }
#     #veri duzene koyuldu
#     result = firebase.post('/Sensor_Data', data)
#     #veri gonderildi
#     print(result)

if __name__ == "__main__":
    app.run(debug = True)