import serial

bytecnt = 0 #Byte count string

hb2 = 0
lb2 = 0
hb10 = 0
lb10 = 0

with open('data.csv', 'w') as myCSV:
    with serial.Serial('COM10', 9600) as ser:
        while True:
            if bytecnt == 10:
                bytecnt = 0
                ugm2 = ((int.from_bytes(hb2, 'little')*256) + (int.from_bytes(lb2, 'little'))/10)
                print(ugm2)
                ugm10 = ((int.from_bytes(hb10, 'little')*256) + (int.from_bytes(lb10, 'little'))/10)
                print(ugm10)
                myCSV.write(str(ugm10)+ ',' + str(ugm2) + '\n')
     
            
            
            x = ser.read()          # read one byte
            bytecnt += 1

            if bytecnt == 3:
                lb2 = x
            if bytecnt == 4:
                hb2 = x
            if bytecnt == 5:
                lb10 = x
            if bytecnt == 6:
                hb10 = x

        
         
