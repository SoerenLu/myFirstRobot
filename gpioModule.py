import RPi.GPIO as GPIO

#Motor1A = 16
#Motor1B = 18
#Motor1E = 22

def initialize():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16,GPIO.OUT)
    GPIO.setup(18,GPIO.OUT)
    GPIO.setup(22,GPIO.OUT)

def cleanup():
    updateMotor([0])
    GPIO.cleanup()

def updateMotor(motionStatus):
    #drive forwards
    if motionStatus[0] == 2:
        #motor one
        GPIO.output(16,GPIO.HIGH)
        GPIO.output(18,GPIO.LOW)
        GPIO.output(22,GPIO.HIGH)
    #drive backwards
    elif motionStatus[0] == 4:
        #motor one
        GPIO.output(16,GPIO.LOW)
        GPIO.output(18,GPIO.HIGH)
        GPIO.output(22,GPIO.HIGH)
    #stop
    elif motionStatus[0] == 0:
        #diable motor one
        GPIO.output(22,GPIO.LOW)

def updateLED(ledStatus):
    #test implementation
    #print('LED updated')
    a = 3
