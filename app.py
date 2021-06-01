from flask import Flask,render_template

app = Flask(__name__)
@app.route("/")
def index():
    name = "kaan"
    numbers = [1,2,3,4,5]
    return render_template("index.html",numbers = numbers, name = name)

def dursun():
    import serial
    from firebase import firebase
    from datetime import datetime
    from datetime import date
    cisim_sayi = 0 #program her baslatildiginda sensörden yeni veriler alinir

    #Firebase burada ayarlandı
    try:

    firebase = firebase.FirebaseApplication("https://tasarimproject-c1d85-default-
    rtdb.firebaseio.com/", None)

    print("Firebase is On!!")
    except:
    print('Cant connect to Firebase')

    """Serial port açma işlemi burada yapiliyor."""
    try:
    arduino = serial.Serial(port="/dev/cu.usbserial-1420", baudrate=9600)
    print("Sensor is On!!")
    except:
    print('Please check the port')

    62

    while 1:
    sensor_name = "sensor-1"
    clean = str(arduino.readline())
    print(clean)
    cisim_sayi = cisim_sayi + 1
    veri = cisim_sayi
    veri = str(veri)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    #arduino verisi alindi
    data = {
    'Sensor_Name':sensor_name,
    'Sensor_Data':veri,
    'Current_Time':current_time,
    'Current_Date':d1
    }
    #veri duzene koyuldu
    result = firebase.post('/Sensor_Data', data)
    #veri gonderildi
    print(result)

if __name__ == "__main__":
    app.run(debug = True)