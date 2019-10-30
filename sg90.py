#注意，如果舵机启动了就是start(占空比)运行了，舵机就会处于一种齿轮抖动状态，解决办法是每次调整完角度后，都使用stop来结束舵机启动
#在频率为50HZ下占空比和角度的关系是2.5--0度，5--45度，7.5--90度，10--135度，12.5--180度。
#经过运行发现，如果不在stop后重新生成新的pwm脉冲对象而直接使用start启动，会导致舵机在一个方向转动，而不是在0--180之间来回转动，因此在
#下面的sg类中的setdirection函数中先del之前的pwm而后再生成新的pwm，然后使用start设置启动后的默认占空比，当然也可以根据需要，
#使用ChangeDutyCycle函数来在运行期间改变占空比。

import RPi.GPIO as g
import time
class sg:
    def __init__(self,pin):
        g.setmode(g.BCM)
        g.setwarnings(False)
        g.setup(pin,g.OUT)
        self.pin=int(pin)
        self.direction=0
        self.pw=g.PWM(pin,50)
        self.pw.start(2.5)
        #self.pw.ChangeDutyCycle(2.5)#beginning from 0度
        time.sleep(0.6)
        self.pw.stop()
    def setdirection(self,d):
        del self.pw
        self.pw=g.PWM(self.pin,50)
        self.pw.start(2.5+d/360*20)#d可以在0到180之间，用这个式子可以转换成50HZ下的占空比
        #self.pw.ChangeDutyCycle(2.5+d/360*20)
        time.sleep(abs(int(d)-self.direction)/180*0.6)#经过测算从0到180度之间给0.6秒比较合适，这里变化的角度计算具体需要几秒。
        self.direction=int(d)
        self.pw.stop()
        