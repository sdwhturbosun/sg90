#注意，如果舵机启动了就是start(占空比)运行了，舵机就会处于一种齿轮抖动状态，解决办法是每次调整完角度后，都使用stop来结束舵机启动
#在频率为50HZ下占空比和角度的关系是2.5--0度，5--45度，7.5--90度，10--135度，12.5--180度。
#经过运行发现，如果不在stop后重新生成新的pwm脉冲对象而直接使用start启动，会导致舵机在一个方向转动，而不是在0--180之间来回转动，因此在
#下面的sg类中的setdirection函数中先del之前的pwm而后再生成新的pwm，然后使用start设置启动后的默认占空比，当然也可以根据需要，
#使用ChangeDutyCycle函数来在运行期间改变占空比。

#sg90舵机最大支持频率是50hz，即每秒发送50个脉冲，每个脉冲持续时间20ms，利用每个脉冲时间高电平的占空比来转到到某个角度，他转速0.002秒/度，转动180度需要0.36秒
#占空比与角度对应关系
'''
 脉冲高电平持续时间              角度     占空比
 0.5ms--------------------------0度；    2.5%
 1.0ms-------------------------45度；     5.0%
 1.5ms-------------------------90度；     7.5%
 2.0ms------------------------135度；    10.0%
 2.5ms------------------------180度；    12.5%
'''
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
        self.pw.start(0)
        self.pw.ChangeDutyCycle(2.5)#占空比2.5,
        #self.pw.ChangeDutyCycle(2.5)#beginning from 0度
        time.sleep(0.36)#sg90转动60度需要0.12秒，他最大转动角度180度，因此回到起点有0.36秒足够，这是机械转动需要的时间，和脉冲周期时间无关
        self.pw.ChangeDutyCycle(0)#sg90停止，不会有抖动
    def setdirection(self,d,speed=10):#这里默认每下调整10度，推荐10度,d：0～180
        if d>self.direction:
            p=self.direction+10
            while p<d:
                self.direction=p
                duty=2.5+10*p/180
                self.pw.ChangeDutyCycle(duty)
                time.sleep(0.02)#停留20ms，等待脉冲周期结束再进行下一个角度的调整
                p=p+10
        else:
            p=self.direction-10
            while p>d:
                self.direction=p
                duty=2.5+10*p/180
                self.pw.ChangeDutyCycle(duty)
                time.sleep(0.02)
                p=p-10
        self.direction=d
        duty=2.5+10*d/180
        self.pw.ChangeDutyCycle(duty)
        time.sleep(0.02)
        self.pw.ChangeDutyCycle(0)
        

        
