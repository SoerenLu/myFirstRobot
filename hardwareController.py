import RPi.GPIO as GPIO

class hardwareController:

    def __init__(self): 
        self.Motor1A = 16
        self.Motor1B = 18
        self.Motor1E = 22
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.Motor1A ,GPIO.OUT)
        GPIO.setup(self.Motor1B ,GPIO.OUT)
        GPIO.setup(self.Motor1E ,GPIO.OUT)

    def __del__(self):
        self.updateMotor([0])
        GPIO.cleanup()

    def updateMotor(self, motionStatus):
        #drive forwards
        if motionStatus[0] == 2:
            #motor one
            GPIO.output(self.Motor1A ,GPIO.HIGH)
            GPIO.output(self.Motor1B ,GPIO.LOW)
            GPIO.output(self.Motor1E ,GPIO.HIGH)
        #drive backwards
        elif motionStatus[0] == 4:
            #motor one
            GPIO.output(self.Motor1A ,GPIO.LOW)
            GPIO.output(self.Motor1B ,GPIO.HIGH)
            GPIO.output(self.Motor1E ,GPIO.HIGH)
        #stop
        elif motionStatus[0] == 0:
            #motor one
            GPIO.output(self.Motor1E ,GPIO.LOW)

    def updateLED(self, ledStatus):
        #test implementation
        #print('LED updated')
        a = 3
