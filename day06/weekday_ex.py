#날짜로 요일 알아내기
import datetime
import calendar
days = ["월", "화", "수", "목", "금", "토", "일"]
print(days[0])
today = datetime.date.today().weekday()
print(today)
print(days[today])
theday = datetime.date(2021, 10, 26).weekday()
print(days[theday])
calendar.prmonth(2021, 10)
