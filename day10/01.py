import threading
import random
import time
# a = random.randint(1,200)
# print(a)
def timerz():
    a = random.randint(100000,999999)
    print(a)
    global timer
    timer = threading.Timer(2, timerz)
    timer.start()
    
timer = threading.Timer(1,timerz) 
timer.start()
timer.sleep(10)
timer.cancel()
