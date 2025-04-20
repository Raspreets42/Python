import threading
import time


def get_mail(tsk):
    time.sleep(8)
    print(f"to {tsk}")

def walk_dog(name,surname):
    time.sleep(2)
    print(f"You are {name} {surname}")

def take_out_trash(tim):
    time.sleep(4)
    print(F"You take {tim}")

mul1 = threading.Thread(target=walk_dog,args=("Raspreet","Singh"))
mul1.start()
mul2 = threading.Thread(target=take_out_trash,args=("2 min",))
mul2.start()
mul3 = threading.Thread(target=get_mail,args=("mail",))
mul3.start()

mul1.join()
mul2.join()
mul3.join()

print("Done")