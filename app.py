from flask import Flask, render_template, url_for, request, redirect, make_response, Response
import serial
from datetime import datetime
from datetime import date
import app
import random
import json
import time
import re

global app
app = Flask(__name__)

#sensorler
global inductive
global capasitive
global fotoelektrik
global ultrasonic

#miktarlar
global metalMiktar
global plastikMiktar
global camMiktar
global kartonMiktar
global copMesafe
metalMiktar = 0
plastikMiktar = 0
camMiktar = 0
kartonMiktar = 0

#kapilar
global kapiInductive
global kapiCapasitive
global kapiFotoelektrik
global kapiUltrasonic

#alt donus 
global donmeDolap

global terminalText
terminalText = ""

"""Serial port açma işlemi burada yapiliyor."""
try:
    arduino = serial.Serial(port="/dev/cu.wchusbserial1410", baudrate=9600)

    print("Sensor is On!!")
except:
    print('Please check the port')

def termRefresh():
    global terminalText
    if(len(terminalText)>1000):
        terminalText = terminalText[-800:]

@app.route('/chart-data')
def ajax() :
    print("hello we are starting!")
    def ff():
        global terminalText
        global metalMiktar
        global plastikMiktar
        global kartonMiktar
        global camMiktar
        global copMesafe
        copMesafe = ""

        while True:
            try:
                time.sleep(2)
                data = arduino.readline().decode("utf-8").strip('\n').strip('\r') # remove newline and carriage return characters
                print(data)
                terminalText += str(data) + '\n'
            except:
                print("Hata1")

            txt = terminalText
            x = re.search("Trash space distance:", txt)
            if x:
                while True:
                    x = re.search("Trash space distance:", txt)
                    if x:
                        txt = txt[x.end()+1:]
                        x = re.search("cm", txt)
                        copMesafe = txt[:x.start()-1]
                    else:
                        break
            print(copMesafe)
            doluBos = ""
            if int(copMesafe) < 10:
                doluBos = "Dolu"
            else:
                doluBos = "Bos"
            x = re.search("Yon degistirildi:", terminalText)
            if x:
                while True:
                    try:
                        if x:
                            terminalText = terminalText[x.end():]
                            x = re.search(".\n", terminalText)
                            terminalText2 = terminalText[:x.start()]
                            print(terminalText2)

                            if terminalText2 == 'Metal':
                                metalMiktar +=1
                            elif terminalText2 == 'Plastik':
                                plastikMiktar +=1
                            elif terminalText2 == 'Karton':
                                kartonMiktar +=1
                            elif terminalText2 == 'Cam':
                                camMiktar +=1
                        else:
                            break
                    except:
                        print("Hata2")

            json_data = json.dumps({'terminalText': terminalText, 'camMiktar': camMiktar, 'kartonMiktar': kartonMiktar, 'metalMiktar': metalMiktar, 'plastikMiktar': plastikMiktar, 'doluBos': doluBos})
            yield f"data:{json_data}\n\n"
    return Response(ff(), mimetype='text/event-stream')

@app.route("/")
def index():
     return render_template("index.html")

# def dursun():

#     cisim_sayi = 0 #program her baslatildiginda sensörden yeni veriler alinir

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