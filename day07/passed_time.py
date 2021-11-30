#시작일 ~ 종료일 기간 계산하는 프로그램
import datetime

print("지금까지 몇 일?")
start_day = datetime.date(2021, 10, 26)
print("개강일은",start_day.month,"월",start_day.day,"일")

today =datetime.date.today()
print("오늘날은",today.month,"월",today.day,"일")


passed_time = today - start_day
print("개강일로부터 {}일이 경과되었습니다.".format(passed_time.days))

now = datetime.datetime.now()
print("현재시간은",today.year,"년",today.month,"월",today.day,"일",now.hour,"시",now.minute,"분",now.second,"초입니다")