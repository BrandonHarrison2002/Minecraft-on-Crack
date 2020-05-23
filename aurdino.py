import  time, serial,json

SettingsName = 'Settings.json'
class aurdino:
    def __init__(self, com="COM3"):
        self.com = com
        self.ser = serial.Serial(com, 9600, timeout=1)

    def shock(self, duration=1):
        time.sleep(1)                      # wait 2 seconds
        self.ser.write(b'H')
        time.sleep(duration)
        self.ser.write(b'L')
        self.ser.close()

    def screech(self, duration=5, loud = 4):
        print('null')




