import RPi.GPIO as g
import sg90
import time
s=sg90.sg(17)
time.sleep(1)
try:
    f=open("students",mode="r")
except e:
    print("read error")
else:
    students=f.readlines()
    f.close()
    while True:
        cardid=input("Please input student's cardID:")
        test=0
        for student in students:
            studentinfo=student.split("_")
            if studentinfo[0]==cardid:
                print("student:",studentinfo[1])
                s.setdirection(90)
                time.sleep(3)
                s.setdirection(0)
                test=1
                break
        if test==0:
            print("No this student.Please go away!")

        
    


