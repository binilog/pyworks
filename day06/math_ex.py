import math

# 2.5 초과 올림 미만 죽임
import random

print(round(2.5))
# 그냥 올림 ceil
print(math.ceil(2.2))
# 갖다 버림
print(math.floor(2.2))

print(random.Random())

print(math.floor(random.random() * 1000))


print(math.pi)

r = 4
area = math.pi * r * r
print("원의 널이 : %.2f" % area)