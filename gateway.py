import serial

ser = serial.Serial('/dev/ttyACM0',9600,timeout=10)

is_first = True
while True:
    lux = ser.readline().decode('utf-8')
    if is_first:
        is_first = False
    else:
        print(lux)

ser.close()