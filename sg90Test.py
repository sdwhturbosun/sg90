import RPi.GPIO as g
import sg90
import time
s=sg90.sg(17)
print("roll three seconds later")
time.sleep(3)
s.setdirection(90)
time.sleep(3)
s.setdirection(0)
time.sleep(3)
s.setdirection(90)
time.sleep(3)
s.setdirection(180)
time.sleep(3)
s.stop()
'''
g.setmode(g.BCM) ## Use board pin numbering

#pins are pulled up because the reed switches are ON by default.


g.setup(17, g.OUT)
p25=g.PWM(17, 50)  # pin 18, and 50 Hz

p25.start(7.5) # set to neutral position - 7.5% duty cycle
#p.ChangeFrequency
#p.stop
time.sleep(2)
p25.ChangeDutyCycle(25/2)
time.sleep(0.04)
p25.stop()

try:
    #while True:
        for i in range(1, 26):
            p25.ChangeDutyCycle(i/2)
            time.sleep(0.04)
           
        for i in range(1, 26):
            p25.ChangeDutyCycle(14.5-(i/2))
            time.sleep(0.04)
            
    
except KeyboardInterrupt:
    p25.ChangeDutyCycle(7.5)
    p25.stop
    time.sleep(0.5)
    GPIO.cleanup()
'''