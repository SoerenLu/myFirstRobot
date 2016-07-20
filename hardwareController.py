import RPi.GPIO as GPIO

class hardwareController:

    def __init__(self): 
        GPIO.setmode(GPIO.BOARD)
        #Motor 1
        self.Motor1A = 16
        self.Motor1B = 18
        self.Motor1E = 22
        GPIO.setup(self.Motor1A ,GPIO.OUT)
        GPIO.setup(self.Motor1B ,GPIO.OUT)
        GPIO.setup(self.Motor1E ,GPIO.OUT)
        #Motor 2
        self.Motor2A = 19
        self.Motor2B = 21
        self.Motor2E = 23
        GPIO.setup(self.Motor2A ,GPIO.OUT)
        GPIO.setup(self.Motor2B ,GPIO.OUT)
        GPIO.setup(self.Motor2E ,GPIO.OUT)

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
            #motor two
            GPIO.output(self.Motor2A ,GPIO.HIGH)
            GPIO.output(self.Motor2B ,GPIO.LOW)
            GPIO.output(self.Motor2E ,GPIO.HIGH)
        #drive backwards
        elif motionStatus[0] == 4:
            #motor one
            GPIO.output(self.Motor1A ,GPIO.LOW)
            GPIO.output(self.Motor1B ,GPIO.HIGH)
            GPIO.output(self.Motor1E ,GPIO.HIGH)
            #motor two
            GPIO.output(self.Motor2A ,GPIO.LOW)
            GPIO.output(self.Motor2B ,GPIO.HIGH)
            GPIO.output(self.Motor2E ,GPIO.HIGH)
        #left turn
        elif motionStatus[0] == 1:
            #motor one
            GPIO.output(self.Motor1A ,GPIO.HIGH)
            GPIO.output(self.Motor1B ,GPIO.LOW)
            GPIO.output(self.Motor1E ,GPIO.HIGH)
            #motor two
            GPIO.output(self.Motor2A ,GPIO.LOW)
            GPIO.output(self.Motor2B ,GPIO.HIGH)
            GPIO.output(self.Motor2E ,GPIO.HIGH)
        #right turn
        elif motionStatus[0] == 3:
            #motor one
            GPIO.output(self.Motor1A ,GPIO.LOW)
            GPIO.output(self.Motor1B ,GPIO.HIGH)
            GPIO.output(self.Motor1E ,GPIO.HIGH)
            #motor two
            GPIO.output(self.Motor2A ,GPIO.HIGH)
            GPIO.output(self.Motor2B ,GPIO.LOW)
            GPIO.output(self.Motor2E ,GPIO.HIGH)            
        #stop
        elif motionStatus[0] == 0:
            #motor one
            GPIO.output(self.Motor1E ,GPIO.LOW)
            GPIO.output(self.Motor2E ,GPIO.LOW)

    def updateLED(self, ledStatus):
        #test implementation
        #print('LED updated')
        a = 3
