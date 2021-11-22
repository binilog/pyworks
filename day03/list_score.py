score = [100, 98, 95, 38, 60]
count = len(score)
sum_v = 0
avg = 0.0

print(sum(score))
for i in score:
    sum_v += i

avg = sum_v / count

max_v = score[0]
for i in score:
    if max_v < i:
        max_v = i
min_v = score[0]
for i in score:
    if min_v > i:
        min_v = i

print("개수 :", count)
print("합계 :", sum(score))
print("평균 :", avg)
print("최고점수 :", max_v)
print("최고점수 :", max(score))
print("최저점수 :", min_v)