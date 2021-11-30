import time

print(time.time())     #1970. 1. 1 자정 이후 초로 환산
days = round(time.time() / (24*60*60)) #초를 일로 환산
year = round(time.time() / (365*24*60*60))  #초를 년으로 환산
print("{}일".format(days))
print("{}년".format(year))

start = time.time()

for i in range(3000):
        print("***************************************************", (i), ".", (i), ".", (i), ".", (i), ".", (i), ".",
            (i), ".", (i), ".", (i), ".", (i), "초 경과",
            "현재시간은", today.year, "년", today.month, "월", today.day, "일", now.hour, "시", now.minute, "분", now.second,
            "초입니다",
            "**********************************************")
        time.sleep(1)#second
    
end = time.time()
et = math.floor(end-start)
print("for문 수행 시간 : {}초".format(et))