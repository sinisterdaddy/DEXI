import serial
ser = serial.Serial('COM3',9600)

while True:
    input_user = input("Y to turn ON and N to turn OFF ")
    if (input_user == 'A'):
        ser.write(b'A')
        
    if(input_user == 'a'):
        ser.write(b'a')
        
    if (input_user == 'Q'):
        ser.write(b'Q')

    if (input_user == 'W'):
        ser.write(b'W')

    if (input_user == 'E'):
        ser.write(b'E')

    if (input_user == 'R'):
        ser.write(b'R')

    if (input_user == 'T'):
        ser.write(b'T')

    if (input_user == 'Y'):
        ser.write(b'Y')

    if (input_user == 'U'):
        ser.write(b'U')

    if (input_user == 'I'):
        ser.write(b'I')
