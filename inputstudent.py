print("System to input student's information")
while True:
    cardid=input("Student's ID:")
    name=input("Student's Name:")
    room=input("Student's Class:")
    phone=input("Student's phone number:")
    try:
        f=open("students",mode="a")
    except e:
        print("write error!")
        print(e)
    else:
        studentinfo=cardid+"_"+name+"_"+room+"_"+phone+"\n"
        f.write(studentinfo)
        print("write ok!")
        f.close()
