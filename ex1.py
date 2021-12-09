import time
import datetime
import threading

# print(time.time())     #1970. 1. 1 자정 이후 초로 환산
days = round(time.time() / (24*60*60)) #초를 일로 환산
year = round(time.time() / (365*24*60*60))  #초를 년으로 환산
# print("{}일".format(days))
# print("{}년".format(year))

start = time.time()
now = datetime.datetime.now()
today =datetime.date.today()
def call():
    print("타이머 종료")
    print("타이머 종료된 시점",datetime.datetime.now())
print("타이머 시작")
print("타이머 시작된 시점",datetime.datetime.now())

for i in range(48600):
        print("***************************************************", (i), ".", (i), ".", (i), ".", (i), ".", (i), ".",
            (i), ".", (i), ".", (i), ".", (i), "초 경과", "***************************************************", "\n",
            "**********************************************",
            "타이머 시작한 시간은", today.year, "년", today.month, "월", today.day, "일", now.hour, "시", now.minute, "분", now.second,
            "초입니다",
            "**********************************************")
        time.sleep(0.2)#second

# for a in range(50):
#     print("--------------------------------------------------", (a), ".", (a), ".", (a), ".", (a), ".", (a), ".",
#           (a), ".", (a), ".", (a), ".", (a), "분 경과", "--------------------------------------------------", "\n",
#           "-----------------------------------------------------------------------------------------------------------------------------------")
#     time.sleep(60)  # second


print("for문 수행 시간 : {}초".format(et))
timer = threading.Timer(10, call)
timer.start()
end = time.time()
et = math.floor(end-start)


