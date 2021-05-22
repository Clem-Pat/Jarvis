import pyfirmata
import time

class Arduino_board():
    def __init__(self, jarvis, usb_port='COM7', analog_pins=[0, 1, 2], digital_pins=[3]):
        self.port, self.jarvis = usb_port, jarvis
        self.arduinoboard = None
        self.pin = {}
        self.analog_pins, self.digital_pins = analog_pins, digital_pins
        self.load_board()

    def load_board(self):
        try:
            self.arduinoboard = pyfirmata.Arduino(self.port)
            print(f'Arduino board plugged in port {self.port}')
            self.jarvis.log(f'Arduino board plugged in port {self.port}', type='arduino')
        except:
            self.arduinoboard = None
            print(f'No Arduino board plugged in port {self.port}')
            self.jarvis.log(f'No Arduino board plugged in port {self.port}', type='arduino')

        if self.arduinoboard != None:
            self.iterate = pyfirmata.util.Iterator(self.arduinoboard)
            self.iterate.start()
            time.sleep(1)

            for i in self.analog_pins:
                self.arduinoboard.analog[i].enable_reporting()
                self.pin["A" + str(i)] = self.arduinoboard.analog[i]
                self.pin["A" + str(i)].value = self.pin["A" + str(i)].read()
                time.sleep(0.5)

            for j in self.digital_pins:
                self.pin["d" + str(j)] = self.arduinoboard.get_pin('d:' + str(j) + ':i') #i comme input ou o comme output ?
                self.pin["d" + str(j)].value = None
        else:
            for i in self.analog_pins: self.pin["A" + str(i)] = None
            for i in self.digital_pins: self.pin["d" + str(i)] = None

    def exit(self):
        if self.arduinoboard != None:
            self.arduinoboard.exit()
