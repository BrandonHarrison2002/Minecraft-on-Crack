import  time, serial,json

SettingsName = 'Settings.json'
class aurdino:
    def __init__(self):
        with open(SettingsName, 'r') as file:
            data = json.load(file)
        self.ser = serial.Serial( "COM" + str(data['com']), 9600, timeout=1)

    def shock(self, duration=1):
        time.sleep(1)                      # wait 2 seconds
        self.ser.write(b'H')
        time.sleep(duration)
        self.ser.write(b'L')
        self.ser.close()

    def screech(self, duration=5, loud = 4):
        print('null')




