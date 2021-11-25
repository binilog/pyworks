import math


def myabs(x):
    if x < 0:
        return -x
    else:
        return x


def myabs2(x):
    y = x * x
    return math.sqrt(y)


print(myabs(-9))
print(myabs2(-9))
print(abs(-9))

