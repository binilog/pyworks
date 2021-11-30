# 일정 시간 후에 타이머 종료
import threading
import datetime

def call():
    print("타이머 종료")
    print("타이머 종료된 시점",datetime.datetime.now())
print("타이머 시작")
print(datetime.datetime.now())
timer = threading.Timer(5, call)
timer.start()



