students = [
    {'name':'김하나"', 'kor':80, 'math':70, 'eng':90},
    {'name':'김하나"', 'kor':60, 'math':50, 'eng':40},
    {'name':'김하나"', 'kor':90, 'math':90, 'eng':100}
]
# sum_v = 0
print(" 이름 총점 평균")
for s in students:
    sum_v = s['kor'] + s['math'] + s['eng']
    avg = sum_v / 3
    print("%s %d %.1f" % (s['name'], sum_v, avg))

sum_kor = 0
    for s in students:
        sum_kor += s['kor']

print("국어 합계 : %d점" % sum_kor)