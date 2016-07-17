#!/usr/bin/env python
from _thread import start_new_thread
import sys
import termios
import contextlib
import time
import gpioModule

@contextlib.contextmanager
def raw_mode(file):
    old_attrs = termios.tcgetattr(file.fileno())
    new_attrs = old_attrs[:]
    new_attrs[3] = new_attrs[3] & ~(termios.ECHO | termios.ICANON)
    try:
        termios.tcsetattr(file.fileno(), termios.TCSADRAIN, new_attrs)
        yield
    finally:
        termios.tcsetattr(file.fileno(), termios.TCSADRAIN, old_attrs)

def printStatus( motionStatus, ledStatus):
        print(' Motion: ', end=' ')
        print(motionStatus[0],end='; ')
        print('LED: ', end=' ')
        print(ledStatus[0], end='\r')

def statusResettingThread(threadStatus, motionStatus):
    #resets the motion status to 0 after .3 seconds without input
    while threadStatus[0] == 1:
        time.sleep(.3)
        if motionStatus[1] == 0:
            motionStatus[0] = 0
        motionStatus[1] = 0

def input2motionStatus(input):
    if input == 119:
        return 2
    elif input == 97:
        return 1
    elif input == 115:
        return 4
    elif input == 100:
        return 3
    else:
        return -1

def input2ledStatus(input):
    if input == 111:
        return 1
    elif input == 108:
        return 0
    else:
        return -1

def inputHandler(motionStatusIs, ledStatusIs, input):
    #handle motion inputs
    motionStatusCmd = input2motionStatus(input)
    #if input was no motionStatus command, -1 is returned
    if motionStatusCmd != -1:
        motionStatusIs[0] = motionStatusCmd
        motionStatusIs[1] = 1
    #handle LED inputs
    ledStatusCmd = input2ledStatus(input)
    if ledStatusCmd != -1:
        ledStatusIs[0] = ledStatusCmd

def update(threadStatus, motionStatus, ledStatus):
    while threadStatus[0] == 1:
        time.sleep(0.1)
        gpioModule.updateMotor(motionStatus)
        gpioModule.updateLED(ledStatus)
        printStatus(motionStatus, ledStatus)

def main():
    print("exit with ^C or ^D")
    #dictates status of the threads: 1-continue, 0-stop
    threadStatus = [1]
    #status[0]: 0-do nothing, 1-left, 2-forw, 3-right, -4backw 
    #status[1]: has changed flag. 1-has changed, 0-hasnt changed
    motionStatus = [0,0]
    #status of LED
    ledStatus = [0]
    #threads (use only if not possible otherwise):
    #Motion status resetting
    start_new_thread(statusResettingThread, (threadStatus, motionStatus,) )
    #Update
    start_new_thread(update, ( threadStatus,  motionStatus, ledStatus, ) )
    with raw_mode(sys.stdin):
        try:
            while True:
                #abtastfrequenz
                key = sys.stdin.read(1)
                if not key or key == chr(4):
                    break
                #print(ord(key))
                inputHandler(motionStatus, ledStatus,  ord(key))
        except (KeyboardInterrupt, EOFError):
            threadStatus[0] = 0
            pass


if __name__ == '__main__':
    main()

