import time
import datetime
import threading

# print(time.time())     #1970. 1. 1 자정 이후 초로 환산
days = round(time.time() / (24 * 60 * 60))  # 초를 일로 환산
year = round(time.time() / (365 * 24 * 60 * 60))  # 초를 년으로 환산
# print("{}일".format(days))
# print("{}년".format(year))

start = time.time()
now = datetime.datetime.now()
today = datetime.date.today()


print("타이머 시작")
print("타이머 시작된 시점", datetime.datetime.now())

for i in range(200):
    print(i, ".", (i), ".", (i), ".", (i), ".", (i), ".", (i), ".", (i), ".", (i), ".", (i), ".",
          (i), ".", (i), ".", (i), ".", (i), ".", (i), ".", (i), ".", (i), ".", (i), ".", (i), ".",
          (i), ".", (i), ".", (i), ".", (i), ".", (i), ".", (i), ".", (i), ".", (i), ".", (i), ".", (i), ".", (i), ".",
          (i), ".", (i), ".", (i), ".", (i), ".", (i), ".", (i), ".", (i), ".", (i), ".", (i), ".", (i), ".", (i), ".",
          (i), ".",
          (i), ".", (i), ".", (i), ".", (i), ".", (i), ".", (i), ".", (i), ".", (i), ".", (i), ".", (i), ".",
          (i), ".", (i), ".", (i), ".", (i), ".", i)
    time.sleep(0.2)  # second
if:
    i == 200:
    break
    print("타이머 종료")
    print("쉬는시간")
    print("쉬는시간")
    print("쉬는시간")
    print("쉬는시간")
    print("쉬는시간")
    print("쉬는시간")
    print("쉬는시간")
    print("쉬는시간")
    print("쉬는시간")
    print("쉬는시간")
    print("쉬는시간")
    print("쉬는시간")
    print("쉬는시간")
    print("쉬는시간")
    print("쉬는시간")
    print("쉬는시간")
    print("쉬는시간")
    print("쉬는시간")
    print("쉬는시간")
    print("쉬는시간")
    print("쉬는시간")
    print("쉬는시간")
    print("쉬는시간")
    print("쉬는시간")
    print("쉬는시간")
    print("쉬는시간")
    print("쉬는시간")
    print("쉬는시간")
    print("타이머 종료된 시점", datetime.datetime.now())


print("for문 수행 시간 : {}초".format(et))
timer = threading.Timer(10, call)
timer.start()
end = time.time()
et = math.floor(end - start)
