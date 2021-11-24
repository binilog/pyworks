score = [100, 40, 50, 60, 0, 20]
count = len(score)
sum_v = 0
avg = 0.0

for i in score:
    sum_v += i

avg = sum_v / count

# max_v = score[0]
# for i in score:
#     if max_v < i:
#         max_v = i
# min_v = score[0]
# for i in score:
#     if min_v > i:
#         min_v = i

print("평균 :", avg)
print(len(score))