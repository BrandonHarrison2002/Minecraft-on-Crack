import  time, serial
class aurdino:
    def shock(self, duration=1):
        ser = serial.Serial('COM3', 9600, timeout=1)
        time.sleep(1)                      # wait 2 seconds
        ser.write(b'H')
        time.sleep(duration)
        ser.write(b'L')
        ser.close()

    def screech(self, duration=5, loud = 4):
        print('null')



